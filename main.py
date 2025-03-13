# main.py
from rag import get_phrase

def main():
    entrada = input("Introdueix una entrada per obtenir la frase relacionada: ")
    resultat = get_phrase(entrada)
    print("\nFrase trobada:")
    print(resultat)

if __name__ == "__main__":
    main()
