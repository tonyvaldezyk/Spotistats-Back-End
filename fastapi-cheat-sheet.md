## Guide pour Créer une Application FastAPI

---

### Étape 1 : Installer FastAPI et Uvicorn
Commencez par installer **FastAPI** et **Uvicorn**, un serveur ASGI utilisé pour exécuter l'application.

```bash
pip install fastapi uvicorn
```

---

### Étape 2 : Configurer votre répertoire de projet
Créez une structure de répertoire pour votre projet. Par exemple :

```
fastapi_project/
    ├── main.py
```

---

### Étape 3 : Créer l'application principale FastAPI
Dans le fichier `main.py`, écrivez le code suivant :

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bienvenue sur FastAPI !"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

**Explications :**
- `FastAPI()` crée une instance de l'application.
- `@app.get("/")` définit un point d'accès GET pour l'URL racine.
- `@app.get("/items/{item_id}")` définit un point d'accès dynamique qui accepte un `item_id`.

---

### Étape 4 : Exécuter l'application
Exécutez l'application avec **Uvicorn** :

```bash
uvicorn main:app --reload
```

- `main` est le nom du fichier (sans `.py`).
- `app` est l'instance FastAPI.
- `--reload` active le rechargement automatique pendant le développement.

Rendez-vous sur `http://127.0.0.1:8000` dans votre navigateur pour voir l'application FastAPI en action.

---

### Étape 5 : Tester votre API
FastAPI fournit automatiquement une documentation interactive de l'API. Vous pouvez y accéder via :
- Swagger UI : `http://127.0.0.1:8000/docs`
- ReDoc : `http://127.0.0.1:8000/redoc`

---

### Étape 6 : Ajouter des points d'accès supplémentaires (optionnel)
Ajoutez plus de routes à votre API. Par exemple :

```python
@app.post("/items/")
def create_item(item: dict):
    return {"message": "Item créé avec succès", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"message": "Item mis à jour avec succès", "item_id": item_id, "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} supprimé avec succès"}
```

---

### Étape 7 : Exécuter en production (optionnel)
Pour un environnement de production, utilisez un serveur plus robuste comme **Gunicorn** avec des workers Uvicorn :

```bash
pip install gunicorn
gunicorn -k uvicorn.workers.UvicornWorker main:app
```

---

C'est tout ! Vous avez maintenant une application **FastAPI** fonctionnelle. Faites-moi savoir si vous souhaitez ajouter une intégration de base de données, une authentification ou déployer votre application !
