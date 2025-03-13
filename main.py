from rag import Rag

def main():
    # Intentem carregar el model desat
    try:
        rag = Rag.load("rag_model.pkl")
        print("Model carregat des de rag_model.pkl")
    except FileNotFoundError:
        print("Model no trobat, s'entrena un de nou.")
        rag = Rag()
        rag.save("rag_model.pkl")
        print("Model guardat a rag_model.pkl")

    print("Benvingut al sistema RAG!")
    while True:
        user_input = input("Escriu una consulta (o 'sortir' per acabar): ")
        if user_input.lower() == "sortir":
            print("Fins aviat!")
            break
        result = rag.query(user_input)
        print("Frase més relacionada:", result)

if __name__ == "__main__":
    main()
