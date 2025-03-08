# Système de Détection du Paludisme

## Description du projet
Le paludisme est une maladie mortelle causée par des parasites transmis à l'homme par les piqûres de moustiques infectés. Le diagnostic et le traitement précoces sont essentiels pour réduire la morbidité et la mortalité. 

Ce projet vise à développer un système de détection du paludisme à partir d'images sanguines en utilisant des techniques de vision par ordinateur et d'apprentissage automatique.

## Technologies utilisées
- **TensorFlow/Keras** : Pour l'implémentation et l'entraînement du modèle de classification d'images
- **Flask** : Pour le déploiement du modèle sous forme d'application web
- **Bootstrap** : Pour la conception de l'interface utilisateur

## Structure du projet
```
Système_Detection_Paludisme/
│── data/
│   ├── Parasitized/
│   ├── Uninfected/
│   ├── test/
│── models/
│   ├── best_prediction_model_for_paludisme.keras
│   ├── prediction-model-for-malaria-infected-cells.h5
│── notebooks/
│   ├── Paludisme.ipynb
│── static/
│   ├── css/
│   │   ├── style.css
│   ├── images/
│   ├── scripts/
│   ├── upload/
│── templates/
│   ├── index.html
│── .gitignore
│── app.py
│── requirements.txt
│── test.py
│── Projet5 - IA_ Système de Détection du paludisme.pdf
```

## Métriques du Modèle
Les performances du modèle sont les suivantes :
- **Précision (Precision)** : 0.94 - Proportion de prédictions positives correctes parmi toutes les prédictions positives.
- **Recall (Rappel)** : 0.98 - Proportion des cas positifs correctement identifiés par le modèle.
- **Accuracy (Précision globale)** : 0.96 - Pourcentage total de prédictions correctes (positives et négatives) par rapport à l'ensemble des données.
- **AUC (Area Under Curve)** : 0.99 - Indicateur de la capacité du modèle à distinguer entre les classes infectées et non infectées.

## Installation et exécution
### Prérequis
Assurez-vous d'avoir **Python 3.8+** installé ainsi que `pip`.

### Installation des dépendances
```bash
pip install -r requirements.txt
```

### Lancer l'application
```bash
python app.py
```
L'application sera accessible sur **http://127.0.0.1:5000/**.

## Fonctionnalités
- Chargement d'images sanguines 
- Prédiction de l'infection (Paludisme ou Non infecté)
- Interface utilisateur intuitive via Flask et Bootstrap

## Auteur
Nom : Abdoul Wahab Soumare Ingénieur en Bio-informatique / Data scientist 
Email : soumarewahab@gmail.com  


