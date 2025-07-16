import fastapi
import dotenv
import groq
import sentence_transformers
import joblib
import pandas
import sklearn
from importlib.metadata import version


if __name__ == "__main__":
    print("fastapi:", fastapi.__version__)
    print("python-dotenv:", version("python-dotenv"))
    print("groq:", groq.__version__)
    print("sentence-transformers:", sentence_transformers.__version__)
    print("joblib:", joblib.__version__)
    print("pandas:", pandas.__version__)
    print("scikit-learn:", sklearn.__version__)
