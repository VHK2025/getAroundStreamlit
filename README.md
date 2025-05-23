---
title: GetAroundStreamlit
emoji: 🚗
colorFrom: green
colorTo: blue
sdk: docker
app_file: app.py
pinned: false
license: mit
---

# 🚗 GetAround Price Predictor

Une application Streamlit qui prédit le prix de location d'une voiture basée sur ses caractéristiques.

## 🔧 Fonctionnement

L'application utilise un modèle de machine learning (RandomForestRegressor) entraîné sur des données réelles pour estimer le prix.

### 🧠 Modèle utilisé :
- `model_getaround_real.pkl` (chargé via joblib)
- Caractéristiques prises en compte :
  - puissance moteur
  - kilométrage
  - boîte automatique
  - climatisation
  - parking privé
  - Getaround Connect
  - type de véhicule (SUV ou non)
  - type de carburant (électrique ou non)

## 🚀 Déploiement local

```bash
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Fichiers nécessaires

- `app.py` (l'application principale)
- `model_getaround.pkl` (le modèle entraîné)
- `requirements.txt` (les dépendances)
- `Dockerfile`

## 🙌 Créé avec ❤️ pour le projet GetAround
#   g e t A r o u n d S t r e a m l i t  
 