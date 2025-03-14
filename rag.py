import pickle
import numpy as np

# Intentem importar FAISS
try:
    import faiss
except ModuleNotFoundError:
    try:
        import faiss_cpu as faiss
    except ModuleNotFoundError:
        raise ImportError("No s'ha pogut importar ni faiss ni faiss_cpu. Instal·la 'faiss-cpu'.")

from sentence_transformers import SentenceTransformer
from PyPDF2 import PdfReader

def load_pdf_content(pdf_path):
    """Llegeix el PDF i retorna una llista de textos, un per pàgina."""
    reader = PdfReader(pdf_path)
    parts = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            parts.append(text.strip())
    return parts

class Rag:
    def __init__(self, pdf_path="normativa-fp.pdf"):
        # Carrega el contingut del PDF en parts (una per pàgina)
        self.parts = load_pdf_content(pdf_path)
        if not self.parts:
            raise ValueError("No s'ha pogut extreure contingut del PDF.")
        # Inicialitza el model amb "all-MiniLM-L6-v2"
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        # Genera els embeddings per a cada part
        self.embeddings = self.model.encode(self.parts, convert_to_numpy=True)
        # Obté la dimensió dels embeddings i construeix l'índex FAISS
        self.dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.embeddings)

    def query(self, input_text):
        # Genera l'embedding per la consulta
        query_embedding = self.model.encode([input_text], convert_to_numpy=True)
        # Cerquem el veí més proper (k=1)
        k = 1
        distances, indices = self.index.search(query_embedding, k)
        best_match_index = int(indices[0][0])
        return self.parts[best_match_index]
    
    def save(self, filename):
        # Desa l'objecte amb pickle (excloent el model i l'índex)
        with open(filename, "wb") as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load(filename):
        # Carrega l'objecte desat
        with open(filename, "rb") as f:
            return pickle.load(f)
    
    def __getstate__(self):
        state = self.__dict__.copy()
        # Exclou els atributs que es reconstruiran
        if 'model' in state:
            del state['model']
        if 'index' in state:
            del state['index']
        return state
    
    def __setstate__(self, state):
        self.__dict__.update(state)
        # Reconstrueix el model i l'índex
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        if not hasattr(self, 'embeddings') or self.embeddings is None:
            self.embeddings = self.model.encode(self.parts, convert_to_numpy=True)
        self.dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.embeddings)
