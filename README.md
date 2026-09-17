# 🧬 Medical Agentic Research Assistant

Assistant intelligent de recherche médicale combinant **LLM + Agents + RAG + outils externes + outils internes**.

> ⚠️ **Avertissement important** : ce projet est un prototype académique/technique destiné à la recherche, à l'apprentissage et à l'exploration de documents et de sources médicales. Il ne remplace pas l'avis d'un médecin, d'un pharmacien ou d'un professionnel de santé et ne doit pas être utilisé seul pour poser un diagnostic, prescrire un traitement ou prendre une décision médicale.

## 📌 Sommaire

- [🎯 Présentation](#-présentation)
- [✨ Fonctionnalités](#-fonctionnalités)
- [🏗️ Architecture](#️-architecture)
- [📁 Structure du projet](#-structure-du-projet)
- [⚙️ Installation](#️-installation)
- [🔐 Configuration](#-configuration)
- [▶️ Lancement](#️-lancement)
- [💬 Exemples d'utilisation](#-exemples-dutilisation)
- [🧪 Vérification](#-vérification)
- [📊 État réel de l'implémentation](#-état-réel-de-limplémentation)
- [⚠️ Limites connues](#️-limites-connues)
- [🚀 Évolutions recommandées](#-évolutions-recommandées)
- [📚 Documentation](#-documentation)
- [👨‍💻 GitHub](#-github)

## 🎯 Présentation

Le **Medical Agentic Research Assistant** est une application Python avec interface Streamlit. Elle permet à l'utilisateur de poser des questions en langage naturel et de charger des documents PDF médicaux afin de rechercher de l'information dans une base de connaissances locale.

Le cœur du système est un agent LangChain utilisant un modèle de langage OpenAI. L'agent dispose de plusieurs outils :

- 🔎 recherche bibliographique PubMed ;
- 💊 recherche d'informations sur les médicaments via OpenFDA ;
- 🌍 accès à une fonction WHO actuellement simulée ;
- 📄 recherche sémantique dans les PDF indexés ;
- 🧮 calcul ;
- 📝 résumé simplifié ;
- 🩺 analyse de symptômes simplifiée.

## ✨ Fonctionnalités

### ✅ Fonctionnalités présentes dans le code

- 🖥️ Interface web Streamlit.
- 📤 Import de fichiers PDF médicaux.
- 📚 Extraction du texte avec `PyPDFLoader`.
- ✂️ Découpage en chunks de 1000 caractères avec chevauchement de 100.
- 🧠 Embeddings OpenAI avec `text-embedding-3-small`.
- 🗂️ Index vectoriel FAISS persistant localement.
- 🤖 Agent LangChain avec outils.
- 🔎 Recherche PubMed.
- 💊 Recherche OpenFDA.
- 🧮 Calculatrice interne.
- 📝 Mémoire conversationnelle.

### 🟡 Fonctionnalités partielles ou simplifiées

- 🌍 WHO : le code fourni retourne actuellement une réponse simulée, pas une requête réelle vers une API WHO.
- 📝 Résumé : le résumeur tronque le texte à 200 caractères ; ce n'est pas un véritable résumé génératif.
- 🩺 Analyse de symptômes : la fonction retourne une suggestion générique ; elle ne réalise pas un raisonnement clinique validé.
- 📰 News : une fonction existe mais elle retourne un texte statique et n'est pas configurée comme outil de l'agent.

### ❌ Fonctionnalités annoncées dans le cahier des charges mais absentes du code actuel

- 🌦️ API météo réellement connectée.
- 🌐 API Wikipedia réellement connectée.
- 🧠 Interpréteur Python complexe réel.
- 🧩 Moteur de décision explicite séparé : le routage est actuellement confié à l'agent LangChain et à ses descriptions d'outils.
- 🧾 Système robuste de citations/sources automatiques pour toutes les réponses.

## 🏗️ Architecture

```text
                    👤 Utilisateur
                          │
                          ▼
                  🖥️ Streamlit UI
                          │
                          ▼
                 🤖 MedicalAgent
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
           📄 RAG      🌐 APIs      🧰 Outils
             │            │            │
          FAISS      PubMed/FDA    Calcul/Résumé/
             │                       Symptômes
             └────────────┬────────────┘
                          ▼
                    🧠 LLM OpenAI
                          │
                          ▼
                  💬 Réponse finale
```

### Flux RAG

```text
PDF → extraction → chunking → embeddings → FAISS
                                         ↓
Question → similarity search → contexte récupéré → Agent/LLM
```

## 📁 Structure du projet

```text
.
├── app.py
├── .env.example
├── README.md
├── data/
│   └── medical_pdfs/
├── modules/
│   ├── agent.py
│   └── rag.py
├── tools/
│   ├── medical_apis.py
│   └── internal_tools.py
├── ui/
├── utils/
├── docs/
│   ├── cahier_des_charges.md
│   ├── rapport_final.md
│   ├── latex/
│   ├── 01_SOMMAIRE.md
│   ├── 02_GUIDE.md
│   ├── 03_PRESENTATION_COMPLETE.md
│   ├── 04_COMMANDES.md
│   ├── 05_DEFINITIONS.md
│   └── 06_ANALYSE_TECHNIQUE.md
└── requirements.txt
```

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone <URL_DU_DEPOT>
cd <NOM_DU_DEPOT>
```

### 2. Créer l'environnement virtuel

```bash
python -m venv venv
```

Windows :

```bash
venv\Scripts\activate
```

Linux/macOS :

```bash
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la clé OpenAI

Windows :

```bash
copy .env.example .env
```

Linux/macOS :

```bash
cp .env.example .env
```

Puis renseigner au minimum :

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## 🔐 Configuration

Le fichier `.env` contient les secrets. **Il ne doit jamais être commité dans GitHub.**

Le fichier `.env.example` sert uniquement de modèle.

## ▶️ Lancement

```bash
streamlit run app.py
```

Après lancement, Streamlit fournit l'adresse locale de l'application dans le terminal, généralement sous la forme :

```text
http://localhost:8501
```

## 💬 Exemples d'utilisation

### 📄 Interroger un PDF

1. Ouvrir l'application.
2. Charger un PDF médical depuis la barre latérale.
3. Attendre le message d'indexation.
4. Poser une question liée au document.

Exemple :

```text
Résume les résultats principaux de cette étude.
```

### 🔎 Rechercher dans PubMed

```text
Cherche des articles sur le diabète de type 2.
```

### 💊 Rechercher un médicament

```text
Donne les indications et les effets indésirables de l'ibuprofène.
```

### 🧮 Utiliser la calculatrice

```text
Calcule 120 / 80 puis multiplie le résultat par 100.
```

## 🧪 Vérification

Vérifier la syntaxe Python :

```bash
python -m py_compile app.py modules/rag.py modules/agent.py tools/medical_apis.py tools/internal_tools.py
```

## 📊 État réel de l'implémentation

| Composant | État | Commentaire |
|---|---|---|
| Streamlit | ✅ | Interface de chat et upload PDF |
| Agent LangChain | ✅ | Agent avec outils OpenAI |
| OpenAI LLM | ✅ | `gpt-4o-mini` dans le code fourni |
| RAG | ✅ | PDF → chunks → embeddings → FAISS |
| PubMed | ✅ | Recherche via `pymed` |
| OpenFDA | ✅ | Requête label médicament |
| WHO | 🟡 | Simulation dans le code |
| Météo | ❌ | Non implémentée |
| Wikipedia | ❌ | Non implémentée |
| News | 🟡 | Fonction statique, non branchée comme outil |
| Résumeur | 🟡 | Troncature simplifiée |
| Analyse symptômes | 🟡 | Règle générique, non clinique |
| Calculatrice | 🟡 | `eval` restreint mais non adapté à la production |
| Citations automatiques | 🟡 | Promesse dans le prompt, pas de mécanisme structuré |

## ⚠️ Limites connues

1. Le projet ne contient pas de `requirements.txt` dans l'archive d'origine ; un fichier minimal est fourni avec cette documentation.
2. Plusieurs variables du `.env.example` ne sont pas utilisées par le code fourni.
3. L'adresse e-mail PubMed est générique (`assistant@example.com`) et devrait être remplacée par une identité de contact adaptée.
4. La réponse WHO est simulée.
5. Le calculateur repose sur `eval`; même avec des restrictions, cette approche doit être renforcée avant tout usage en production.
6. Le chargement FAISS utilise `allow_dangerous_deserialization=True`, à réserver à des index locaux de confiance.
7. Les réponses RAG renvoient du texte mais ne conservent pas explicitement les métadonnées des pages pour produire des références propres.
8. Le projet doit être considéré comme un prototype pédagogique et non comme un dispositif médical.

## 🚀 Évolutions recommandées

### Phase 1 — Stabilisation

- Ajouter des versions de dépendances dans `requirements.txt`.
- Ajouter une gestion centralisée des erreurs.
- Ajouter des timeouts aux requêtes HTTP.
- Valider les variables d'environnement au démarrage.
- Ajouter des tests unitaires.

### Phase 2 — Amélioration RAG

- Conserver les métadonnées `source`, `page`, `document`.
- Retourner les passages sources avec chaque réponse.
- Ajouter éventuellement un reranker.
- Gérer la suppression/réindexation des documents.

### Phase 3 — Outils externes

- Remplacer la simulation WHO par une vraie source de données.
- Implémenter réellement les outils météo/news/Wikipedia annoncés.
- Structurer les sorties des APIs en objets ou schémas explicites.

### Phase 4 — Sécurité et qualité

- Éliminer `eval` au profit d'un moteur de calcul sûr.
- Ajouter des garde-fous médicaux.
- Ajouter un filtrage des requêtes et des logs.
- Ajouter des tests sur des cas médicaux contrôlés.

## 📚 Documentation

- 📑 [Sommaire détaillé](docs/01_SOMMAIRE.md)
- 📘 [Guide d'installation et d'utilisation](docs/02_GUIDE.md)
- 🎤 [Présentation complète du projet](docs/03_PRESENTATION_COMPLETE.md)
- 💻 [Commandes utiles](docs/04_COMMANDES.md)
- 📖 [Définitions](docs/05_DEFINITIONS.md)
- 🔍 [Analyse technique](docs/06_ANALYSE_TECHNIQUE.md)
- 📋 [Cahier des charges](docs/cahier_des_charges.md)
- 📝 [Rapport final](docs/rapport_final.md)

## 👨‍💻 GitHub

Avant le premier `git push`, vérifier notamment :

```bash
git status
git add .
git commit -m "docs: add complete project documentation"
git push origin main
```

Ne jamais publier `.env`, une clé API, un secret ou une base de données contenant des données sensibles.
