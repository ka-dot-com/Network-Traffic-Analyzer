import pickle
from sklearn.ensemble import RandomForestClassifier

def load_predictor(model_path):
    # Load the trained model, fall back to default if missing
    try:
        with open(model_path, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Model file not found, using default.")
        return RandomForestClassifier()