# Aplicació de Frases Relacionades

Aquesta aplicació permet obtenir una frase relacionada amb una entrada de text proporcionada per l'usuari. La funcionalitat principal es basa en la cerca de paraules clau dins de l'entrada de text i la devolució d'una frase predefinida que coincideixi amb aquestes paraules clau.

## Estructura del Projecte

El projecte està organitzat de la següent manera:


### [main.py](gh_rag/main.py)

Aquest arxiu conté la funció principal de l'aplicació. Demana a l'usuari que introdueixi una entrada de text i després utilitza la funció `get_phrase` de l'arxiu `rag.py` per obtenir la frase relacionada.

```python
from rag import get_phrase

def main():
    entrada = input("Introdueix una entrada per obtenir la frase relacionada: ")
    resultat = get_phrase(entrada)
    print("\nFrase trobada:")
    print(resultat)

if __name__ == "__main__":
    main()
