import requests
from pymed import PubMed
import os

class MedicalTools:
    def __init__(self):
        self.pubmed = PubMed(tool="MedicalAssistant", email="assistant@example.com")

    def search_pubmed(self, query):
        results = self.pubmed.query(query, max_results=3)
        articles = []
        for a in results:
            articles.append(f"Titre: {a.title}\nRésumé: {a.abstract[:300]}...\nLien: https://pubmed.ncbi.nlm.nih.gov/{a.pubmed_id}/")
        return "\n\n".join(articles) if articles else "Aucun article trouvé."

    def get_drug_info(self, drug_name):
        url = f"https://api.fda.gov/drug/label.json?search=openfda.brand_name:{drug_name}&limit=1"
        try:
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()["results"][0]
                return f"Médicament: {drug_name}\nIndications: {data.get('indications_and_usage', ['N/A'])[0][:500]}\nEffets secondaires: {data.get('adverse_reactions', ['N/A'])[0][:500]}"
            return "Médicament non trouvé."
        except:
            return "Erreur lors de la recherche du médicament."

    def get_who_stats(self, query):
        # Simulation de l'API WHO (OData)
        return f"Statistiques WHO pour '{query}': Les données mondiales indiquent une tendance stable pour cette pathologie en 2024."

    def get_medical_news(self):
        return "Dernière minute : Avancée majeure dans le traitement du diabète de type 1 via l'immunothérapie."
