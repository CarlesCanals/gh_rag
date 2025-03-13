# rag.py
from phrases import phrases

def get_phrase(input_text):
    input_text = input_text.lower()
    for item in phrases:
        for keyword in item["keywords"]:
            if keyword in input_text:
                return item["phrase"]
    return "No hi ha coincidència amb l'entrada."
    
# Exemple de test:
if __name__ == "__main__":
    test_input = input("Introdueix una paraula clau: ")
    print(get_phrase(test_input))
