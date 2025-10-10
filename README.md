# Enovacom Pathway

**Application web interne** pour la création de diagrammes professionnels par intelligence artificielle.

> **From idea to diagram in seconds**

## Présentation

**Enovacom Pathway** est une application web développée en interne pour les collaborateurs Enovacom. Elle permet de générer automatiquement des diagrammes professionnels (Mermaid.js) à partir de descriptions en langage naturel, grâce à l'intelligence artificielle Mistral AI.

### Cas d'usage
- **Architecture technique** : Diagrammes de séquence, diagrammes de classes
- **Processus métier** : Flowcharts, diagrammes d'états
- **Gestion de projet** : Gantt, timelines
- **Documentation** : Diagrammes ER, mindmaps
- **Présentations clients** : Tous types de diagrammes personnalisables

### Avantages
- ✅ **Gain de temps** : Génération instantanée par IA
- ✅ **Qualité professionnelle** : 30+ thèmes, export haute qualité
- ✅ **Simplicité** : Pas besoin de connaître la syntaxe Mermaid
- ✅ **Personnalisation** : Couleurs, polices, styles entièrement configurables
- ✅ **Sécurité** : Données stockées localement, aucun serveur central

---

## ⚡ Installation

### Prérequis

#### 1. Python 3.8+
- **Télécharger** : [python.org/downloads](https://www.python.org/downloads/)
- ⚠️ **Important** : Lors de l'installation, cochez la case **"Add Python to PATH"**

#### 2. Clé API Mistral AI (gratuite)

**Mistral AI offre un test d'API gratuit** pour tester l'API, suffisant pour générer des centaines de diagrammes.

**Étapes pour créer votre compte gratuit :**

1. **Créer un compte** : Rendez-vous sur [console.mistral.ai](https://console.mistral.ai)
2. **S'inscrire** : Utilisez votre email professionnel Enovacom
3. **Vérifier votre email** : Cliquez sur le lien de confirmation
4. **Accéder à la console** : Connectez-vous à [console.mistral.ai](https://console.mistral.ai)
5. **Créer une clé API** :
   - Cliquez sur **"API Keys"** dans le menu
   - Cliquez sur **"Create new key"**
   - Donnez un nom à votre clé (ex: "Enovacom Pathway")
   - Copiez la clé générée (elle ne sera affichée qu'une seule fois !)
6. **Conserver votre clé** : Sauvegardez-la dans un endroit sûr

> 💡 **Astuce** : Les 5€ gratuits permettent environ 500 générations de diagrammes. Au-delà, vous pouvez ajouter des crédits selon vos besoins (tarifs très compétitifs).

> 🔒 **Sécurité** : Votre clé API est stockée uniquement dans le localStorage de votre navigateur. Elle n'est jamais transmise aux serveurs Enovacom.

### Installation Windows (automatique)

```bash
# 1. Cloner le repository
git clone https://github.com/enovacom/pathway.git
cd pathway

# 2. Double-cliquer sur start.bat (ou lancer en ligne de commande)
start.bat
```

**C'est tout !** Le script `start.bat` fait automatiquement :
- ✅ Création de l'environnement virtuel Python
- ✅ Installation des dépendances (Flask, requests, python-dotenv)
- ✅ Lancement de l'application
- ✅ Ouverture automatique dans votre navigateur

L'application s'ouvre sur `http://127.0.0.1:5173`

> 💡 **Astuce** : Si vous obtenez une erreur "Python n'est pas reconnu", c'est que Python n'est pas dans le PATH. Réinstallez Python en cochant "Add Python to PATH".

### Installation Linux/Mac

```bash
# Cloner le repository
git clone https://github.com/enovacom/pathway.git
cd pathway

# Lancer le script d'installation
chmod +x linux/start.sh
./linux/start.sh
```

Le script fait tout automatiquement (environnement virtuel, dépendances, lancement).

---

## 🔧 Configuration

### Première utilisation

Lors du premier lancement de l'application :

1. **Ouvrir l'application** : L'application s'ouvre automatiquement sur `http://127.0.0.1:5173`
2. **Cliquer sur "Paramètres"** : Bouton dans le header de l'application
3. **Configurer Mistral AI** :
   - **Base URL** : Laisser `https://api.mistral.ai` (par défaut)
   - **API Key** : Coller votre clé API Mistral créée précédemment
4. **Tester la connexion** : Cliquez sur "Tester" pour vérifier que tout fonctionne
5. **Sauvegarder** : Cliquez sur "Sauvegarder" pour enregistrer vos paramètres

✅ **C'est prêt !** Vous pouvez maintenant générer des diagrammes par IA.

### Sélection du modèle

L'application charge automatiquement la liste des modèles Mistral AI disponibles. Nous recommandons :

- **`mistral-large-latest`** : Le plus puissant, meilleure qualité de génération
- **`mistral-medium-latest`** : Bon équilibre qualité/coût
- **`mistral-small-latest`** : Rapide et économique pour tests

> 💡 **Conseil** : Commencez avec `mistral-small-latest` pour tester, puis passez à `mistral-large-latest` pour la production.

---

## 🧩 Types de diagrammes Mermaid supportés

Mermaid permet beaucoup de formats. Tu peux mixer les exemples ci-dessous directement dans l’app.

### 1) Flowchart (processus)

```mermaid
flowchart LR
  A[Arrivée patient] --> B{Urgence ?}
  B -- Oui --> C((Triage prioritaire))
  B -. Non .-> D[Accueil standard]
  C ==> E[Consultation]
  D --> E
  style C fill:#E8F5F4,stroke:#0C4A45,stroke-width:2px,color:#0e1f1c
```

**Flèches rapides** : `-->` pleine · `-.->` pointillée · `==>` épaisse · `---` trait sans pointe
**Formes** : `[ ]` rectangle · `( )` arrondi · `(( ))` cercle · `{ }` décision · `[[ ]]` sous-routine · `[( )]` DB

---

### 2) Sequence (échanges)

```mermaid
sequenceDiagram
  autonumber
  participant P as Patient
  participant I as Infirmier
  participant M as Médecin

  P ->> I: Arrivée
  I ->> M: Dossier
  activate M
  M -->> I: Instructions
  deactivate M

  Note over P,I: Accueil & triage
  alt Urgent
    I ->> M: Appel prioritaire
  else Standard
    I ->> P: Salle d’attente
  end
```

---

### 3) Class (modèle objet)

```mermaid
classDiagram
  class Patient {
    +id: string
    +nom: string
    +admettre()
  }
  class Dossier {
    +id: string
    +etat: string
  }
  Patient "1" -- "1" Dossier : possède
  Dossier <|-- DossierUrgent : hérite
```

---

### 4) State (états)

```mermaid
stateDiagram-v2
  [*] --> EnAttente
  EnAttente --> EnCours: déclencher
  EnCours --> Terminé: finir
  state EnCours {
    [*] --> Traitement
    Traitement --> Validation
    Validation --> [*]
  }
  Terminé --> [*]
```

---

### 5) ER (entités / relations)

```mermaid
erDiagram
  PATIENT ||--o{ DOSSIER : possède
  DOSSIER ||--o{ EXAMEN : comprend
  PATIENT {
    string id PK
    string nom
  }
  DOSSIER {
    string id PK
    string etat
  }
```

---

### 6) Gantt (planning)

```mermaid
gantt
  title Parcours patient
  dateFormat  YYYY-MM-DD
  section Accueil
  Admission       :a1, 2025-04-01, 1d
  Triage          :after a1, 1d
  section Soins
  Examens         :crit, 2d
  Diagnostic      :1d
```

---

### 7) Pie (répartition)

```mermaid
pie showData
  title Répartition des actes
  "Consultation" : 40
  "Examens"      : 35
  "Urgences"     : 25
```

---

### 8) Journey (parcours UX)

```mermaid
journey
  title Parcours patient
  section Accueil
    Admission        : 4: Patient
    Triage           : 3: Infirmier
  section Soins
    Prise de sang    : 2: Laboratoire
    Diagnostic       : 5: Médecin
```

---

### 9) Timeline (chronologie)

```mermaid
timeline
  title Dossier patient
  2025-01 : Création
  2025-02 : Examens
  2025-03 : Diagnostic
  2025-04 : Traitement
```

---

### 10) Mindmap (idées)

```mermaid
mindmap
  root((Parcours))
    Accueil
      Triage
      Orientation
    Soins
      Examens
      Diagnostic
    Sortie
      Compte rendu
      Suivi
```

---

### 11) Git graph (workflows git)

```mermaid
gitGraph
  commit id: "init"
  branch feature
  checkout feature
  commit id: "WIP"
  checkout main
  merge feature
  commit id: "release"
```

> \*Selon la version de Mermaid embarquée, d’autres types peuvent être dispos (p.ex. quadrantChart).

---

## 🖌️ Thèmes & personnalisation

* **Sélecteur de thème** : applique des palettes complètes (lignes **et** boîtes : nœuds, acteurs, clusters, notes) + **fond du canvas**.
* **Couleur** : tu peux surcharger la couleur principale des liens.
* **Police** : Inter, Work Sans, Manrope, Montserrat, JetBrains Mono (monospace).

Astuce : pour un rendu cohérent, pars d’un thème puis ajuste seulement la **couleur principale**.

---

## 📤 Exports

* **SVG** : vectoriel (impeccable pour Figma/Illustrator).
* **PNG** : bitmap **transparent** (présentations, web).
* **JPEG** : bitmap fond **blanc** (documents bureautiques).

> Les exports utilisent un pipeline **fiable** (SVG → Canvas → toBlob) pour éviter les soucis de polices et d’échelle.

---

## ⌨️ Raccourcis

* **Ctrl/Cmd + Entrée** : Générer depuis le prompt (si l’API est configurée).

---

## 🗺️ Architecture (très simple)

* **Frontend** : HTML + Alpine.js + Mermaid v10 + Tailwind (CDN pour dev).
* **Intégrations** : Web Speech API (dictée FR).
* **Exports** : SVG direct, PNG/JPEG via Canvas `toBlob`.
* **Backend (optionnel)** : endpoints REST minces pour parler à l’API Mistral.

## 📄 Licence

MIT

---

## 🙌 Crédits

* [Mermaid](https://mermaid.js.org/) pour le moteur de rendu
* Merci à toutes les personnes qui aiment les jolis schémas ❤️

```
```
