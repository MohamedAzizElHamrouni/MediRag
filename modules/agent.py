from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from modules.rag import MedicalRAG
from tools.medical_apis import MedicalTools
from tools.internal_tools import InternalTools

class MedicalAgent:
    def __init__(self):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
        self.rag = MedicalRAG()
        self.med_tools = MedicalTools()
        self.internal = InternalTools()
        self.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        self.executor = self._init_agent()

    def _init_agent(self):
        tools = [
            Tool(name="pubmed", func=self.med_tools.search_pubmed, description="Recherche PubMed"),
            Tool(name="drug_info", func=self.med_tools.get_drug_info, description="Infos médicaments FDA"),
            Tool(name="who_stats", func=self.med_tools.get_who_stats, description="Stats WHO"),
            Tool(name="rag_search", func=self.rag.query, description="Recherche dans les PDF locaux"),
            Tool(name="calculator", func=self.internal.calculator, description="Calculatrice médicale"),
            Tool(name="summarizer", func=self.internal.summarizer, description="Résumeur de texte"),
            Tool(name="symptom_analysis", func=self.internal.symptom_analyzer, description="Analyse de symptômes")
        ]

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Tu es le 'Medical Agentic Research Assistant'. Utilise tes outils pour aider les médecins et étudiants. Sois précis et cite tes sources."),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])

        agent = create_openai_tools_agent(self.llm, tools, prompt)
        return AgentExecutor(agent=agent, tools=tools, memory=self.memory, verbose=True)

    def run(self, user_input):
        return self.executor.invoke({"input": user_input})["output"]
