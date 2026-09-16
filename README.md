# 🛡️ Adaptive Zero-Day Network Intrusion Detection System

### AI-powered network anomaly detection using Isolation Forest, XGBoost, and LSTM Autoencoder

An end-to-end **Network Intrusion Detection System (NIDS)** designed to identify abnormal and potentially unseen network activity using a combination of **machine learning, deep learning, anomaly detection, and an interactive Streamlit dashboard**.

The system combines supervised and unsupervised approaches to provide a layered view of network traffic rather than relying on a single detection model.

---

## 🚨 Problem Statement

Traditional intrusion detection systems often depend heavily on known attack signatures.

This creates a challenge when:

* A new or previously unseen attack occurs
* Network traffic differs from previously observed patterns
* Attack signatures are unavailable
* A model needs to detect anomalous behaviour rather than only known labels

This project explores an AI-based approach for detecting suspicious network behaviour using both **known attack classification** and **anomaly/novelty detection** techniques.

---

## 💡 Proposed Solution

The system uses three complementary models:

```text
                    Network Traffic
                           │
                           ▼
                  Data Preprocessing
                           │
                           ▼
                    Feature Scaling
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
      Isolation Forest   XGBoost   LSTM Autoencoder
             │             │             │
             └─────────────┼─────────────┘
                           │
                           ▼
                  Detection / Analysis
                           │
                           ▼
                  Streamlit Dashboard
```

### Models used

| Model                | Purpose                                              |
| -------------------- | ---------------------------------------------------- |
| **Isolation Forest** | Unsupervised anomaly detection                       |
| **XGBoost**          | Supervised network attack classification             |
| **LSTM Autoencoder** | Deep-learning-based reconstruction/novelty detection |

The combination allows the project to examine network traffic from different modelling perspectives.

---

## 🔍 Key Features

* 🧠 **Multi-model intrusion detection**
* 🔎 **Anomaly / novelty detection**
* 🌲 Isolation Forest for unsupervised detection
* ⚡ XGBoost for supervised classification
* 🧬 LSTM Autoencoder for sequence-based anomaly detection
* 📊 Interactive Streamlit monitoring dashboard
* 🎚️ Adjustable risk threshold
* 🟢 Live monitoring interface
* ☑️ Selectable active detection models
* 📁 Saved trained models for inference
* 📈 Evaluation and detection reports
* 🧪 Separate testing workflow

---

## 📊 Model Performance

### XGBoost Evaluation

The XGBoost model achieved the following results on the evaluated test data:

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **99.89%** |
| Precision | **99.65%** |
| Recall    | **99.72%** |
| F1-Score  | **99.68%** |

These results reflect the evaluated dataset/split used during development and should not be interpreted as production-world attack detection performance.

### Earlier Multi-Model Evaluation

The project also included a multi-model evaluation on a larger CICIDS2017-derived dataset.

| Class   | Precision | Recall | F1-Score |
| ------- | --------: | -----: | -------: |
| Normal  |      0.91 |   0.93 |     0.92 |
| Anomaly |      0.63 |   0.57 |     0.60 |

Overall accuracy for that evaluation was approximately **86%**.

The difference between these evaluations highlights why dataset composition, class balance, sampling, and evaluation methodology are important when assessing intrusion-detection models.

---

## 🧠 Why Multiple Models?

A single model can have limitations.

### Isolation Forest

Isolation Forest treats unusual observations as potential anomalies.

It is useful when:

* Attack labels are unavailable
* Previously unseen behaviour needs investigation
* The system needs an unsupervised detection component

### XGBoost

XGBoost provides supervised classification using labelled network traffic.

It is useful for:

* Learning known attack patterns
* Producing strong classification performance
* Comparing predicted traffic against known classes

### LSTM Autoencoder

The LSTM Autoencoder learns patterns in network-traffic sequences and attempts to reconstruct them.

A larger reconstruction error can indicate that traffic differs from the learned normal behaviour.

This adds a deep-learning perspective to the detection pipeline.

---

## 🖥️ Streamlit Dashboard

The project includes an interactive dashboard for controlling and monitoring the detection system.

The interface includes:

* **Risk Threshold** control
* **Live Monitoring** toggle
* Active model selection
* Isolation Forest
* XGBoost
* LSTM Autoencoder
* Network-security monitoring interface

The dashboard is designed to make the underlying ML pipeline easier to interact with than running individual notebook cells.

---

## 📁 Project Structure

```text
Adaptive-Zero-Day-NIDS/
│
├── Adaptive_NIDS.ipynb
│       └── Main NIDS development workflow
│
├── testing.ipynb
│       └── Model testing and evaluation
│
├── model_saving.ipynb
│       └── Model preparation and artifact saving
│
├── app.py
│       └── Streamlit dashboard
│
├── models/
│   ├── isolation_forest.pkl
│   ├── lstm_autoencoder.keras
│   ├── scaler.pkl
│   ├── xgboost_model.pkl
│   └── y_test.csv
│
├── reports/
│   ├── multi_model_consensus_results.csv
│   └── novelty_detection_results.csv
│
└── .gitignore
```

### Large generated arrays

The locally generated scaled arrays:

```text
models/X_train_scaled.npy
models/X_test_scaled.npy
```

are intentionally excluded from GitHub because of their large size.

They can be regenerated from the preprocessing workflow rather than being stored directly in the repository.

---

## 🔄 Detection Pipeline

### 1. Data Preparation

Network traffic data is loaded and prepared for machine learning.

### 2. Preprocessing

The data is cleaned and transformed into a numerical feature representation.

### 3. Feature Scaling

A scaler is used to transform the network features before model inference.

### 4. Model Training

Three approaches are used:

```text
Network Traffic
      │
      ├──► Isolation Forest
      │
      ├──► XGBoost
      │
      └──► LSTM Autoencoder
```

### 5. Evaluation

Models are evaluated using metrics such as:

* Accuracy
* Precision
* Recall
* F1-score

Additional detection results are saved in the `reports/` directory.

### 6. Deployment Interface

The trained models are loaded by the Streamlit application for interactive monitoring.

---

## 🛠️ Tech Stack

### Programming

* Python

### Machine Learning

* Scikit-learn
* XGBoost

### Deep Learning

* TensorFlow
* Keras

### Data Processing

* NumPy
* Pandas

### Visualization / Dashboard

* Streamlit

### Model Persistence

* Joblib
* Keras model format

### Dataset

* CICIDS2017-derived network traffic data

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Saisruti-Mohanty/Adaptive-Zero-Day-NIDS.git
cd Adaptive-Zero-Day-NIDS
```

Install the required Python packages:

```bash
pip install numpy pandas scikit-learn xgboost tensorflow streamlit joblib
```

If a `requirements.txt` file is added later, installation can be simplified to:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

From the project directory:

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

## 🧪 Reproducing the Workflow

The notebooks are organized around different stages of the project:

### `Adaptive_NIDS.ipynb`

Main development notebook containing the NIDS experimentation and modelling workflow.

### `model_saving.ipynb`

Used to prepare/save trained model artifacts used by the application.

### `testing.ipynb`

Used for model evaluation and testing.

### `app.py`

Provides the interactive Streamlit interface using the saved model artifacts.

---

## 📈 Generated Reports

The project contains two generated result files:

```text
reports/
├── multi_model_consensus_results.csv
└── novelty_detection_results.csv
```

These files support analysis of the model outputs and novelty/anomaly detection experiments.

---

## 🎯 What Makes This Project Different?

Instead of building only a conventional binary classifier, this project explores a **hybrid intrusion-detection architecture**:

```text
                 ┌─────────────────────┐
                 │   Network Traffic   │
                 └──────────┬──────────┘
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
       Unsupervised    Supervised     Deep Learning
       Detection       Detection      Reconstruction
             │              │              │
       Isolation       XGBoost        LSTM Autoencoder
        Forest
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                  Security Analysis
                            │
                            ▼
                  Interactive Dashboard
```

This allows the project to investigate both **known attack classification** and **abnormal/novel network behaviour**.

---

## ⚠️ Limitations

This project is an academic/prototype NIDS and is not intended to be presented as a production-grade intrusion prevention system.

Important limitations include:

* Evaluation results depend on the dataset and split used.
* CICIDS2017 traffic may not represent modern production networks.
* High offline classification performance does not automatically imply equivalent real-world zero-day detection performance.
* Threshold selection affects anomaly detection results.
* Real-time deployment would require additional work around packet capture, streaming ingestion, latency, monitoring, and security hardening.

---

## 🚀 Future Improvements

Potential extensions include:

* [ ] Real-time packet/flow ingestion
* [ ] Network packet capture integration
* [ ] Adaptive threshold calibration
* [ ] SHAP-based model explanations
* [ ] Automated risk scoring
* [ ] Attack-type visualization
* [ ] Alert history and incident tracking
* [ ] PDF/CSV security reports
* [ ] Containerized deployment with Docker
* [ ] Cloud deployment
* [ ] Streaming architecture
* [ ] Continuous model monitoring
* [ ] Evaluation on additional datasets

---

## 👩‍💻 Author

**Saisruti Mohanty**

B.Tech — Computer Science & Engineering (Data Science)

Interested in:

* Artificial Intelligence
* Machine Learning
* Data Science
* Deep Learning
* Cybersecurity & AI
* Network Anomaly Detection

---

## ⭐ Project Focus

> **Detect abnormal network behaviour using a combination of machine learning, deep learning, and anomaly detection techniques.**

If you found this project useful, consider giving the repository a ⭐.
