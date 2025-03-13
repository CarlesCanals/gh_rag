from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

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
        # Creem el vectoritzador i vectoritzem les frases
        self.vectorizer = TfidfVectorizer()
        self.sentence_vectors = self.vectorizer.fit_transform(self.sentences)

    def query(self, input_text):
        # Vectoritzem la consulta
        query_vector = self.vectorizer.transform([input_text])
        # Calculem la similaritat cosinus entre la consulta i cada frase
        similarities = cosine_similarity(query_vector, self.sentence_vectors).flatten()
        # Troba l'índex de la frase amb la major similaritat
        best_match_index = similarities.argmax()
        return self.sentences[best_match_index]
