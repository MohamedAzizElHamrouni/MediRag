import math

class InternalTools:
    @staticmethod
    def calculator(expression):
        try:
            # Sécurisation minimale pour l'exemple
            allowed_names = {"math": math, "sqrt": math.sqrt, "pow": pow}
            return str(eval(expression, {"__builtins__": None}, allowed_names))
        except Exception as e:
            return f"Erreur de calcul : {str(e)}"

    @staticmethod
    def summarizer(text):
        # Logique simplifiée (en production, utiliser un LLM dédié)
        return f"Résumé : {text[:200]}..."

    @staticmethod
    def symptom_analyzer(symptoms):
        return f"Analyse des symptômes : {symptoms}. Suggestion : Consulter un spécialiste pour ces symptômes."
