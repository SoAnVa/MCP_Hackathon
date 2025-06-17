import pickle

# read blob from file
with open("./data/alice_profile.pkl", "rb") as f:
    blob = f.read()

out = pickle.loads(blob)
print(out)
