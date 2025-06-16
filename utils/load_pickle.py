import pickle

# read blob from file
with open("alice_profile.pkl", "rb") as f:
    blob = f.read()
    
import pickle
out = pickle.loads(blob)
print(out)
