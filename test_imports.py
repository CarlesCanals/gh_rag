import torch
import faiss
import numpy as np

print("Versions:")
print("  NumPy:", np.__version__)
print("  Torch:", torch.__version__)
print("  faiss?:", getattr(faiss, '__version__', 'Desconeguda'))

print("Importacions correctes sense segfault")
