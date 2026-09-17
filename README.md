# 🚀 Guide d'Exécution : Medical Agentic Research Assistant

## 1. Présentation
Ce projet est un assistant intelligent hybride (RAG + Agents + Tools) dédié à la recherche médicale.

## 2. Prérequis
- Python 3.10 ou supérieur
- Un environnement Windows 10/11 (recommandé)
- Une clé API OpenAI

## 3. Installation
1. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   ```
2. **Activer l'environnement** :
   - Windows : `venv\Scripts\activate`
   - Linux/Mac : `source venv/bin/activate`
3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

## 4. Configuration
1. Renommez `.env.example` en `.env`.
2. Ajoutez votre `OPENAI_API_KEY`.

## 5. Lancement
Exécutez la commande suivante :
```bash
streamlit run app.py
```

## 6. Utilisation
- **RAG** : Glissez un PDF dans la barre latérale pour l'analyser.
- **PubMed** : Demandez "Cherche des articles sur [sujet]".
- **Médicaments** : Demandez "Quels sont les effets de [médicament] ?".
- **Calculs** : Demandez "Calcule [expression mathématique]".
