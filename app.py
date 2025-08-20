from flask import Flask, render_template, request, jsonify
import requests
import os
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration en mémoire
config = {
    'mistral_base_url': os.getenv('MISTRAL_BASE_URL', 'https://api.mistral.ai'),
    'mistral_api_key': os.getenv('MISTRAL_API_KEY', ''),
    'ollama_base_url': os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434'),
}

SYSTEM_PROMPT = """Tu convertis une description FR/EN en code Mermaid v10 **valide**.
Règles :
- Détecte type pertinent : flowchart, sequence, class, state, er, gantt.
- Réponds **UNIQUEMENT** par un bloc de code Mermaid (sans prose/commentaires).
- Identifiants sûrs (A, A1, a-b, etc.).
- Labels FR si prompt FR.
- Header YAML si pertinent :
---
title: ...
---"""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        engine = data.get('engine', 'ollama')
        model = data.get('model', 'mistral')
        
        if not prompt.strip():
            return jsonify({'error': 'Prompt requis'}), 400
            
        if engine == 'ollama':
            return generate_ollama(prompt, model)
        elif engine == 'mistral':
            return generate_mistral(prompt, model)
        else:
            return jsonify({'error': 'Moteur non supporté'}), 400
            
    except Exception as e:
        return jsonify({'error': f'Erreur serveur: {str(e)}'}), 500

def generate_ollama(prompt, model):
    try:
        url = f"{config['ollama_base_url']}/api/generate"
        payload = {
            "model": model,
            "prompt": f"{SYSTEM_PROMPT}\n\nDescription: {prompt}",
            "stream": False
        }
        
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        
        result = response.json()
        mermaid_code = result.get('response', '').strip()
        
        if not is_valid_mermaid(mermaid_code):
            return jsonify({'error': 'Réponse invalide: pas de code Mermaid détecté'}), 422
            
        return jsonify({'mermaid': mermaid_code})
        
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout: Ollama ne répond pas'}), 408
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Impossible de se connecter à Ollama'}), 503
    except Exception as e:
        return jsonify({'error': f'Erreur Ollama: {str(e)}'}), 500

def generate_mistral(prompt, model):
    try:
        if not config['mistral_api_key']:
            return jsonify({'error': 'Clé API Mistral manquante dans la configuration'}), 401
            
        url = f"{config['mistral_base_url']}/v1/chat/completions"
        headers = {
            'Authorization': f"Bearer {config['mistral_api_key']}",
            'Content-Type': 'application/json'
        }
        payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": f"Description: {prompt}"}
            ],
            "temperature": 0.1,
            "max_tokens": 2000
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=60)
        
        # Debug logging
        print(f"Mistral API Status: {response.status_code}")
        if response.status_code != 200:
            print(f"Mistral API Error: {response.text}")
        
        response.raise_for_status()
        
        result = response.json()
        mermaid_code = result['choices'][0]['message']['content'].strip()
        
        # Nettoyer le code Mermaid des balises markdown
        if mermaid_code.startswith('```mermaid'):
            lines = mermaid_code.split('\n')
            mermaid_code = '\n'.join(lines[1:-1]) if len(lines) > 2 else mermaid_code
        elif mermaid_code.startswith('```'):
            lines = mermaid_code.split('\n')
            mermaid_code = '\n'.join(lines[1:-1]) if len(lines) > 2 else mermaid_code
        
        mermaid_code = mermaid_code.strip()
        
        if not is_valid_mermaid(mermaid_code):
            print(f"⚠️ Code Mermaid invalide généré: {mermaid_code[:100]}...")
            return jsonify({'error': 'Réponse invalide: pas de code Mermaid détecté'}), 422
            
        return jsonify({'mermaid': mermaid_code})
        
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout: Mistral ne répond pas dans les délais'}), 408
    except requests.exceptions.HTTPError as e:
        if hasattr(e, 'response') and e.response is not None:
            if e.response.status_code == 401:
                return jsonify({'error': 'Clé API Mistral invalide ou expirée'}), 401
            elif e.response.status_code == 403:
                return jsonify({'error': 'Accès non autorisé à l\'API Mistral'}), 403
            elif e.response.status_code == 429:
                return jsonify({'error': 'Limite de débit API Mistral atteinte'}), 429
            else:
                return jsonify({'error': f'Erreur API Mistral: {e.response.status_code}'}), 503
        return jsonify({'error': f'Erreur HTTP Mistral: {str(e)}'}), 503
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Erreur de connexion Mistral: {str(e)}'}), 503
    except KeyError as e:
        return jsonify({'error': f'Réponse API Mistral malformée: {str(e)}'}), 502
    except Exception as e:
        return jsonify({'error': f'Erreur Mistral: {str(e)}'}), 500

def is_valid_mermaid(text):
    """Vérifie si le texte contient du code Mermaid valide"""
    if not text:
        return False
    
    # Nettoyer le texte des balises markdown
    text = text.strip()
    
    # Supprimer les balises markdown si présentes
    if text.startswith('```mermaid'):
        lines = text.split('\n')
        text = '\n'.join(lines[1:-1]) if len(lines) > 2 else text
    elif text.startswith('```'):
        lines = text.split('\n')
        text = '\n'.join(lines[1:-1]) if len(lines) > 2 else text
    
    # Patterns Mermaid courants
    patterns = [
        r'flowchart\s+(TD|LR|TB|RL|BT)',
        r'sequenceDiagram',
        r'classDiagram',
        r'stateDiagram',
        r'erDiagram',
        r'gantt',
        r'pie\s+title',
        r'graph\s+(TD|LR|TB|RL|BT)',
        r'journey',
        r'gitgraph'
    ]
    
    return any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns)

@app.route('/api/ollama/models')
def ollama_models():
    try:
        url = f"{config['ollama_base_url']}/api/tags"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        models = [model['name'] for model in data.get('models', [])]
        
        return jsonify({'models': models})
        
    except requests.exceptions.ConnectionError:
        return jsonify({'error': 'Ollama non disponible'}), 503
    except Exception as e:
        return jsonify({'error': f'Erreur lors de la récupération des modèles Ollama: {str(e)}'}), 500

@app.route('/api/mistral/models')
def mistral_models():
    try:
        # Vérifier si on a des headers de test (pour la fonction testMistralConnection)
        test_key = request.headers.get('X-Test-Key')
        test_url = request.headers.get('X-Test-URL')
        
        if test_key and test_url:
            # Mode test : utiliser les paramètres passés en headers
            api_key = test_key
            base_url = test_url
        else:
            # Mode normal : utiliser la config
            if not config['mistral_api_key']:
                return jsonify({'error': 'Clé API Mistral manquante'}), 401
            api_key = config['mistral_api_key']
            base_url = config['mistral_base_url']
            
        url = f"{base_url}/v1/models"
        headers = {
            'Authorization': f"Bearer {api_key}",
            'Content-Type': 'application/json'
        }
        
        print(f"🔍 DEBUG Mistral - URL: {url}")
        print(f"🔍 DEBUG Mistral - Headers: Authorization Bearer {api_key[:10]}...")
        
        response = requests.get(url, headers=headers, timeout=10)
        
        print(f"🔍 DEBUG Mistral - Status: {response.status_code}")
        print(f"🔍 DEBUG Mistral - Response: {response.text[:200]}...")
        
        response.raise_for_status()
        
        data = response.json()
        
        # D'après la doc Mistral, la structure est : {"object": "list", "data": [...]}
        models_data = data.get('data', [])
        models = [model['id'] for model in models_data if 'id' in model]
        
        print(f"🔍 DEBUG Mistral - Models found: {models}")
        
        return jsonify({'models': models})
        
    except requests.exceptions.Timeout:
        return jsonify({'error': 'Timeout: Mistral ne répond pas'}), 408
    except requests.exceptions.HTTPError as e:
        error_msg = f"Erreur HTTP {e.response.status_code}"
        if e.response.status_code == 401:
            error_msg = 'Clé API Mistral invalide ou manquante'
        elif e.response.status_code == 403:
            error_msg = 'Accès non autorisé à l\'API Mistral'
        elif e.response.status_code == 429:
            error_msg = 'Limite de débit API Mistral atteinte'
        
        print(f"🔍 DEBUG Mistral Error - {error_msg}: {e.response.text}")
        return jsonify({'error': error_msg}), e.response.status_code
    except requests.exceptions.RequestException as e:
        print(f"🔍 DEBUG Mistral - Request Error: {str(e)}")
        return jsonify({'error': 'Erreur de connexion à l\'API Mistral'}), 503
    except Exception as e:
        print(f"🔍 DEBUG Mistral - General Error: {str(e)}")
        return jsonify({'error': f'Erreur lors de la récupération des modèles Mistral: {str(e)}'}), 500

@app.route('/api/settings')
def get_settings():
    return jsonify({
        'engine': os.getenv('ENGINE', 'ollama'),
        'mistral_base_url': config['mistral_base_url'],
        'has_mistral_key': bool(config['mistral_api_key'])
    })

@app.route('/api/settings/mistral', methods=['POST'])
def update_mistral_settings():
    try:
        data = request.json
        
        if 'base_url' in data:
            config['mistral_base_url'] = data['base_url'].rstrip('/')
            
        if 'api_key' in data:
            config['mistral_api_key'] = data['api_key']
            
        return jsonify({
            'success': True,
            'mistral_base_url': config['mistral_base_url'],
            'has_mistral_key': bool(config['mistral_api_key'])
        })
        
    except Exception as e:
        return jsonify({'error': f'Erreur lors de la mise à jour: {str(e)}'}), 500

if __name__ == '__main__':
    host = os.getenv('HOST', '127.0.0.1')
    port = int(os.getenv('PORT', 5173))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    print(f"🚀 Mermaid Flask AI démarré sur http://{host}:{port}")
    app.run(host=host, port=port, debug=debug)