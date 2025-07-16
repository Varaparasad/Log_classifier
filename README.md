# 🧠 Hybrid Log Classification Framework

This project presents a powerful and flexible hybrid log classification system that combines three distinct approaches to handle log data of varying complexity and structure. By integrating rule-based, machine learning, and language model techniques, the system ensures accurate and scalable classification across multiple scenarios.

---

## 🔎 Classification Methods

The system leverages the strengths of three complementary techniques:

1. **🔍 Regular Expressions (Regex)**  
   - Designed to identify simple and recurring log patterns.  
   - Ideal for well-defined, rule-based entries.

2. **🤖 Sentence Transformers + Logistic Regression**  
   - Transforms log messages into semantic vectors using sentence embeddings.  
   - Applies logistic regression for classification when enough labeled data is available.

3. **🧠 Large Language Models (LLMs)**  
   - Suitable for complex or low-data scenarios.  
   - Acts as a fallback mechanism to handle cases that cannot be easily managed by regex or machine learning.

![System Architecture](resources/architecture.png)

---

## Folder Structure

1. **`Training/`**:
   - Contains the code for training models using Sentence Transformer and Logistic Regression.
   - Includes the code for regex-based classification.

2. **`Models/`**:
   - Stores the saved models, including Sentence Transformer embeddings and the Logistic Regression model.

3. **`Resources/`**:
   - This folder contains resource files such as test CSV files, output files, images, etc.

4. **Root Directory**:
   - Contains the FastAPI server code (`server.py`).

---
## Setup Instructions

1. **Install Dependencies**:
   Make sure Python 3.8 or above is installed on your system. Install the required Python libraries by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the FastAPI Server**:
   To start the server, use the following command:

   ```bash
   uvicorn server:app --reload
   ```

   Once the server is running, you can access the API at:
   - `http://127.0.0.1:8000/` (Main endpoint)
   - `http://127.0.0.1:8000/docs` (Interactive Swagger documentation)
   - `http://127.0.0.1:8000/redoc` (Alternative API documentation)

---
## Usage

Upload a CSV file containing logs to the FastAPI endpoint for classification. Ensure the file has the following columns:
- `source`
- `log_message`

The output will be a CSV file with an additional column `Label`, which represents the classified label for each log entry.

---
