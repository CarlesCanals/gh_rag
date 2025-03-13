from rag import Rag

def main():
    rag = Rag()
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
