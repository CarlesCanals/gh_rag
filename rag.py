import pickle
import numpy as np

try:
    import faiss
except ModuleNotFoundError:
    try:
        import faiss_cpu as faiss
    except ModuleNotFoundError:
        raise ImportError("No s'ha pogut importar faiss ni faiss_cpu. Assegura't d'instal·lar faiss-cpu.")

from sentence_transformers import SentenceTransformer

class Rag:
    def __init__(self):
        # Definim cinc frases amb continguts molt diferents
        self.sentences = [
            "El cel és blau durant el dia.",
            "Les muntanyes ofereixen paisatges espectaculars.",
            "La tecnologia avança a un ritme accelerat.",
            "El teatre clàssic té una riquesa cultural immensa.",
            "Les receptes de cuina italiana són molt variades."
        ]
        # Inicialitzem el model amb "all-MiniLM-L6-v2"
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        # Generem els embeddings per a les frases (com a array de numpy)
        self.embeddings = self.model.encode(self.sentences, convert_to_numpy=True)
        # Obtenim la dimensió dels embeddings i construïm l'índex FAISS
        self.dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.embeddings)

    def query(self, input_text):
        # Generem l'embedding per la consulta
        query_embedding = self.model.encode([input_text], convert_to_numpy=True)
        # Cerquem el veí més proper (k=1)
        k = 1
        distances, indices = self.index.search(query_embedding, k)
        best_match_index = int(indices[0][0])
        return self.sentences[best_match_index]
    
    def save(self, filename):
        # Desa l'objecte utilitzant pickle
        with open(filename, "wb") as f:
            pickle.dump(self, f)
    
    @staticmethod
    def load(filename):
        # Carrega l'objecte desat
        with open(filename, "rb") as f:
            return pickle.load(f)
    
    def __getstate__(self):
        # Exclou el model i l'índex per evitar problemes de serialització
        state = self.__dict__.copy()
        if 'model' in state:
            del state['model']
        if 'index' in state:
            del state['index']
        return state
    
    def __setstate__(self, state):
        # Restaura l'estat i reconstrueix el model i l'índex.
        # Si l'atribut 'embeddings' no existeix, es recalcula.
        self.__dict__.update(state)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        if not hasattr(self, 'embeddings') or self.embeddings is None:
            self.embeddings = self.model.encode(self.sentences, convert_to_numpy=True)
        self.dimension = self.embeddings.shape[1]
        self.index = faiss.IndexFlatL2(self.dimension)
        self.index.add(self.embeddings)
