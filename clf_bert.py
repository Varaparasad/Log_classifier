import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress TensorFlow INFO and WARNING messages
import logging
logging.getLogger('tensorflow').setLevel(logging.ERROR)  # Suppress TF logger warnings
import warnings
warnings.filterwarnings('ignore')         # Suppress Python warnings
import joblib
from sentence_transformers import SentenceTransformer



model_embedding = SentenceTransformer('all-MiniLM-L6-v2')
model_classifier=joblib.load('./Models/log_classifier.joblib')

def classify_with_bert(log_message):
    embeddings=model_embedding.encode([log_message])
    probabilities=model_classifier.predict_proba(embeddings)[0]
    if max(probabilities) < 0.5:
        return "Unclassified"
    predicted_label = model_classifier.predict(embeddings)[0]

    return predicted_label


if __name__ == "__main__":
    logs = [
        "alpha.osapi_compute.wsgi.server - 12.10.11.1 - API returned 404 not found error",
        "GET /v2/3454/servers/detail HTTP/1.1 RCODE   404 len: 1583 time: 0.1878400",
        "System crashed due to drivers errors when restarting the server",
        "A random log message",
        "Multiple login failures occurred on user 6454 account",
        "Server A790 was restarted unexpectedly during the process of data transfer"
    ]
    for log in logs:
        label = classify_with_bert(log)
        print(log, "->", label)
