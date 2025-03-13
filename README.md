# Aplicació de Frases Relacionades (RAG)

Aquesta aplicació permet obtenir una frase relacionada amb una entrada de text proporcionada per l'usuari. La funcionalitat principal es basa en la cerca de paraules clau dins de l'entrada de text i la devolució d'una frase predefinida que coincideixi amb aquestes paraules clau utilitzant tècniques de vectorització i similaritat cosinus.

## Estructura del Projecte

El projecte està organitzat de la següent manera:


### [main.py](gh_rag/main.py)

Aquest arxiu conté la funció principal de l'aplicació. Demana a l'usuari que introdueixi una entrada de text i després utilitza la classe `Rag` de l'arxiu `rag.py` per obtenir la frase relacionada.

```python
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
