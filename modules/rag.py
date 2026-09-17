import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

class MedicalRAG:
    def __init__(self, db_path="data/vector_db"):
        self.db_path = db_path
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.vector_db = None
        self._load_db()

    def _load_db(self):
        if os.path.exists(self.db_path) and os.listdir(self.db_path):
            self.vector_db = FAISS.load_local(
                self.db_path, 
                self.embeddings, 
                allow_dangerous_deserialization=True
            )

    def ingest_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        documents = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = splitter.split_documents(documents)
        
        if self.vector_db is None:
            self.vector_db = FAISS.from_documents(chunks, self.embeddings)
        else:
            self.vector_db.add_documents(chunks)
        
        self.vector_db.save_local(self.db_path)
        return f"Document {os.path.basename(file_path)} indexé."

    def query(self, question, k=3):
        if self.vector_db is None:
            return "Aucune base de connaissances disponible."
        docs = self.vector_db.similarity_search(question, k=k)
        return "\n\n".join([d.page_content for d in docs])
