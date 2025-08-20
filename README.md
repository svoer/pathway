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
- 🎨 Et tout autre diagramme pris en charge par [Mermaid.js](https://mermaid.js.org/)

👉 Tu décris ton besoin avec une phrase simple, l’IA fait le reste.

---

## ⚡ Installation en 2 minutes
Clone le repo (ou télécharge en ZIP) :

```bash
git clone https://github.com/svoer/pathway.git
cd pathway


---

## ✨ Ce que tu peux faire
- **Générer** du Mermaid depuis un prompt (via API Mistral) ou écrire à la main.
- **Prévisualiser** en direct le rendu.
- **Thèmes** (15+ palettes) qui recolorisent **lignes, boîtes, acteurs, clusters, notes** et le **fond**.
- **Personnaliser** la couleur principale & la police (Inter, Work Sans, Manrope, Montserrat, JetBrains Mono…).
- **Dicter** ton prompt (Web Speech API, FR).
- **Exporter** en **SVG** (vectoriel), **PNG** (fond transparent), **JPEG** (fond blanc).

> ⚠️ Par design, l’export **.mmd** n’est pas exposé dans l’UI (on garde le focus sur les rendus finaux).

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

> *Selon la version de Mermaid embarquée, d’autres types peuvent être dispos (p.ex. quadrantChart).

---

## 🖌️ Thèmes & personnalisation
- **Sélecteur de thème** : applique des palettes complètes (lignes **et** boîtes : nœuds, acteurs, clusters, notes) + **fond du canvas**.
- **Couleur** : tu peux surcharger la couleur principale des liens.
- **Police** : Inter, Work Sans, Manrope, Montserrat, JetBrains Mono (monospace).

Astuce : pour un rendu cohérent, pars d’un thème puis ajuste seulement la **couleur principale**.

---

## 📤 Exports
- **SVG** : vectoriel (impeccable pour Figma/Illustrator).
- **PNG** : bitmap **transparent** (présentations, web).
- **JPEG** : bitmap fond **blanc** (documents bureautiques).

> Les exports utilisent un pipeline **fiable** (SVG → Canvas → toBlob) pour éviter les soucis de polices et d’échelle.

---

## ⌨️ Raccourcis
- **Ctrl/Cmd + Entrée** : Générer depuis le prompt (si l’API est configurée).

---

## 🏗️ Démarrage rapide
1. Clone le repo et ouvre **`index.html`** dans ton navigateur.  
   > 💡 Pour éviter les restrictions CORS locales, lance un mini serveur :  
   > `python3 -m http.server 8080` puis va sur `http://localhost:8080`.
2. (Optionnel) Configure l’API Mistral pour la génération automatique :
   - UI : bouton **Paramètres** → saisis **Base URL** et **API Key**.
   - **Backend attendu** (à implémenter côté serveur) :
     - `GET /api/mistral/models` → liste des modèles
     - `POST /api/settings/mistral` → stocke base_url/api_key
     - `POST /api/generate` → `{ prompt, model } → { mermaid }`
3. Tape/colle du **Mermaid** → choisis un **thème** → **Export** en 1 clic.

> ⚠️ En production, installe **Tailwind** en **PostCSS/CLI** (évite le CDN).

---

## 🧪 Démo rapide (copier/coller)
```mermaid
sequenceDiagram
  autonumber
  participant Patient
  participant GAMME as GAMME (Gestion Admission)
  participant DPI as DPI (Dossier Patient Informatisé)
  Patient->>GAMME: ADT^A01 (Admission)
  GAMME->>DPI: ADT^A01 (Création dossier patient)
```

---

## 🗺️ Architecture (très simple)
- **Frontend** : HTML + Alpine.js + Mermaid v10 + Tailwind (CDN pour dev).
- **Intégrations** : Web Speech API (dictée FR).
- **Exports** : SVG direct, PNG/JPEG via Canvas `toBlob`.
- **Backend (optionnel)** : endpoints REST minces pour parler à l’API Mistral.

---

## 📌 Roadmap (idées)
- Palette **brand-lock** (verrouiller la couleur pour certains thèmes).
- **Templates** réutilisables (snippets Mermaid prêts à l’emploi).
- **Historique**/versions du code Mermaid.
- **Import .mmd** (glisser-déposer).

---

## 🤝 Contribuer
PR bienvenues ! Style code : clair, minimal, compos discret.  
Design : sobre, “2025”, accessible (contrastes et tailles lisibles).

---

## 📄 Licence
MIT — fais-toi plaisir ✌️

---

## 🙌 Crédits
- [Mermaid](https://mermaid.js.org/) pour le moteur de rendu
- Merci à toutes les personnes qui aiment les jolis schémas ❤️
