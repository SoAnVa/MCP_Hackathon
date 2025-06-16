# Utiliser une image Python officielle
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de configuration et le code dans l'image
COPY . .

# Install uv
RUN pip install --no-cache-dir fastapi uvicorn smolagents[litellm] duckduckgo_search 
# Exposer le port sur lequel Uvicorn tournera
EXPOSE 8000

# Lancer l'application avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
