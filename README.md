# 🤖 Pathway From idea to diagram in seconds

Bienvenue dans **Pathway Editor**, un outil qui transforme en temps réel tes idées en **diagrammes intelligents** ✨  
Ici, tu n’as plus besoin d’écrire toi-même du code Mermaid : tu demandes à l’**IA** ce que tu veux (un organigramme, un Gantt, un mindmap, etc.), et le graphique est **généré instantanément** pour toi. 🚀

---

## 🧠 Ce que l’IA peut générer pour toi
En quelques secondes, tu peux obtenir :
- 🌀 **Flowcharts** – Processus, parcours utilisateurs, décisions
- 📊 **Gantt charts** – Plannings et roadmaps projet
- 🤝 **Sequence diagrams** – Interactions entre systèmes
- 🏷️ **Class & Entity diagrams** – UML et bases de données
- 🧠 **Mindmaps** – Brainstorming, organisation d’idées
- 📈 **State diagrams** – États d’un système
👉 Tu décris ton besoin avec une phrase simple, l’IA fait le reste.

---

## ⚡ Installation rapide

### Prérequis
- **Python 3.8+** : [Télécharger Python](https://www.python.org/downloads/)
  - ⚠️ **Important lors de l'installation** : Cochez la case **"Add Python to PATH"** !
- **Clé API Mistral AI** (personnelle) : [Obtenir une clé](https://console.mistral.ai)

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

## 🧪 Démo rapide (copier/coller)

```mermaid
sequenceDiagram
  autonumber
  participant Patient
  participant GAM as GAM (Gestion Admission)
  participant DPI as DPI (Dossier Patient Informatisé)
  Patient->>GAM: ADT^A01 (Admission)
  GAM->>DPI: ADT^A01 (Création dossier patient)
```

---

## 🗺️ Architecture (très simple)

* **Frontend** : HTML + Alpine.js + Mermaid v10 + Tailwind (CDN pour dev).
* **Intégrations** : Web Speech API (dictée FR).
* **Exports** : SVG direct, PNG/JPEG via Canvas `toBlob`.
* **Backend (optionnel)** : endpoints REST minces pour parler à l’API Mistral.

---

## 📌 Roadmap (idées)

* Palette **brand-lock** (verrouiller la couleur pour certains thèmes).
* **Templates** réutilisables (snippets Mermaid prêts à l’emploi).
* **Historique**/versions du code Mermaid.
* **Import .mmd** (glisser-déposer).

---

## 🤝 Contribuer

PR bienvenues ! Style code : clair, minimal, compos discret.
Design : sobre, “2025”, accessible (contrastes et tailles lisibles).

---

## 📄 Licence

MIT — fais-toi plaisir ✌️

---

## 🙌 Crédits

* [Mermaid](https://mermaid.js.org/) pour le moteur de rendu
* Merci à toutes les personnes qui aiment les jolis schémas ❤️

```
```
