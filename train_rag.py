from rag import Rag

def train_and_save(filename="rag_model.pkl"):
    rag = Rag()
    rag.save(filename)
    print(f"Model guardat a {filename}")

if __name__ == "__main__":
    train_and_save()
