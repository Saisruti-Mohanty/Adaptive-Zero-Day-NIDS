# 🛡️ Adaptive Zero-Day Network Intrusion Detection System

### Multi-Model Anomaly Detection • Explainable AI • Adaptive Risk Scoring

An AI-powered **Network Intrusion Detection System (NIDS)** designed to identify anomalous and potentially previously unseen network behavior using a combination of **unsupervised machine learning, supervised learning, deep learning, Explainable AI, and adaptive risk analysis**.

The system combines **Isolation Forest, XGBoost, LSTM Autoencoder, and SHAP** to analyze network traffic from the **CICIDS2017** dataset and presents the results through an interactive **Streamlit security dashboard**.

---

## 🚀 Project Overview

Traditional intrusion detection systems often depend heavily on predefined attack signatures. This can make identifying unusual or previously unseen behavior challenging.

This project explores a hybrid AI-based approach that combines:

* 🔍 Unsupervised anomaly detection
* 🤖 Supervised attack classification
* 🧠 Deep-learning reconstruction
* 🧩 Multi-model consensus
* 📊 Adaptive **0–100 risk scoring**
* 🔎 SHAP-based Explainable AI
* 🧪 Novel/rare attack-category testing
* 🎛️ Interactive What-If risk simulation
* 📈 Streamlit-based security dashboard

The goal is to answer three important questions:

> **Is this network traffic suspicious?**
> **How risky is it?**
> **Why did the model consider it suspicious?**

---

# 🧠 System Architecture

```text
                         CICIDS2017
                              │
                              ▼
                  ┌─────────────────────┐
                  │ Data Cleaning & EDA │
                  └──────────┬──────────┘
                             │
                             ▼
                    Feature Preparation
                             │
                             ▼
                       Data Scaling
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
       Isolation Forest    XGBoost    LSTM Autoencoder
       Unsupervised       Supervised    Deep Learning
       Anomaly Detection  Classification Reconstruction
              │              │              │
              │              │              │
              │              ▼              │
              │           SHAP              │
              │       Explainability        │
              │              │              │
              └──────────────┼──────────────┘
                             ▼
                   Multi-Model Consensus
                             │
                             ▼
                    Adaptive Risk Score
                          0 – 100
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
             Risk Classification   What-If
                                  Simulation
                    │                 │
                    └────────┬────────┘
                             ▼
                   Streamlit Dashboard
```

---

# 🎯 Key Features

## 1. 🔍 Multi-Model Detection

The system uses three complementary detection approaches:

### 🌲 Isolation Forest

An unsupervised anomaly detection algorithm used to identify network traffic that differs from learned normal behavior.

```text
Normal Flow      →  1
Anomalous Flow   → -1
```

Isolation Forest is particularly useful when the system needs to identify suspicious behavior without relying entirely on predefined attack labels.

---

### 🚀 XGBoost

XGBoost is used as the supervised classification component.

It learns from labeled network traffic and distinguishes between:

```text
Normal Traffic
       VS
Attack Traffic
```

The model's prediction probability is also incorporated into the project's risk-analysis workflow.

---

### 🧠 LSTM Autoencoder

The LSTM Autoencoder learns patterns from normal network traffic and attempts to reconstruct the input sequence.

```text
Normal Behavior
       ↓
Low Reconstruction Error
       ↓
Likely Normal


Unusual Behavior
       ↓
High Reconstruction Error
       ↓
Potential Anomaly
```

The reconstruction error is used as an anomaly signal.

---

# 🧩 Multi-Model Consensus

Instead of depending on a single detector, the project combines signals from:

```text
Isolation Forest
       +
XGBoost
       +
LSTM Autoencoder
       ↓
Multi-Model Analysis
       ↓
Consensus / Detection Result
```

The purpose is to obtain a broader view of network behavior by combining:

* Unsupervised anomaly detection
* Supervised classification
* Deep-learning reconstruction

This allows the system to compare different perspectives on the same network flow.

---

# 📊 Adaptive Risk Score

The system converts model outputs into an interpretable **0–100 security risk score**.

| Risk Score | Risk Level    |
| ---------: | ------------- |
|   **0–30** | 🟢 Low        |
|  **31–60** | 🟡 Suspicious |
|  **61–80** | 🟠 High       |
| **81–100** | 🔴 Critical   |

The risk score combines signals from the active detection models and their outputs.

### Why use a risk score?

Raw machine-learning outputs can be difficult for a security analyst to interpret.

Instead of displaying only:

```text
Prediction = 1
```

the system provides an easier-to-understand analytical indicator:

```text
Risk Score: 78 / 100
Risk Level: HIGH
```

> The risk score is an analytical aggregation of model outputs and should not be interpreted as a calibrated probability of compromise.

---

# 🔎 Explainable AI with SHAP

A major component of the project is **Explainable AI using SHAP**.

**SHAP (SHapley Additive exPlanations)** is used to understand the contribution of individual features to the XGBoost prediction.

Instead of treating the model as a black box:

```text
Network Flow
      ↓
    XGBoost
      ↓
Attack Prediction
      ↓
     SHAP
      ↓
Feature Contributions
```

SHAP helps answer questions such as:

* Which network features influenced the prediction?
* Which features increased attack probability?
* Which features reduced attack probability?
* What characteristics of the traffic contributed to the decision?

This adds an interpretability layer to the intrusion detection pipeline.

---

# 🧪 Novel / Unknown Attack Detection

The project also evaluates the anomaly-detection pipeline using rare or held-out attack categories.

One experiment tested **Heartbleed traffic** as a rare attack category.

### Observed Result

```text
Heartbleed samples tested : 11
Detected as anomaly       : 11
```

This experiment demonstrates that the anomaly-detection component was able to flag the selected rare/held-out attack samples as anomalous in the evaluation data.

> **Important:** This does not prove that the system can detect every possible real-world zero-day attack. It demonstrates anomaly/novelty detection on the selected evaluation data.

---

# 🧪 What-If Risk Simulator

The Streamlit dashboard includes an interactive **What-If Risk Simulator**.

The simulator allows network-flow feature values to be modified and the resulting model assessment to be observed.

```text
Modify Network Feature
          ↓
    Preprocess Input
          ↓
    Run Model Analysis
          ↓
 Update Attack Probability
          ↓
   Update Risk Score
          ↓
    Update Risk Level
```

This provides an interactive way to investigate how changes in network-flow characteristics can affect the security assessment.

---

# 📈 Model Results

## 🌲 Isolation Forest

Evaluation on the test traffic produced:

| Metric           |   Score |
| ---------------- | ------: |
| Accuracy         | **86%** |
| Attack Precision | **63%** |
| Attack Recall    | **57%** |
| Attack F1        | **60%** |
| Normal Precision | **91%** |
| Normal Recall    | **93%** |
| Normal F1        | **92%** |

Isolation Forest is used primarily as an **unsupervised anomaly-detection component**, rather than as the only detector in the system.

---

## 🚀 XGBoost

The initial random stratified evaluation produced:

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **99.89%** |
| Precision | **99.65%** |
| Recall    | **99.72%** |
| F1 Score  | **99.68%** |

> These results come from a random train/test split. Network datasets can contain highly similar flows across splits, which can produce optimistic results. Therefore, these metrics should not be interpreted as direct evidence of zero-day performance. A strict time-based or attack-category holdout evaluation is more appropriate for measuring generalization to unseen attacks.

---

# 🧠 LSTM Autoencoder

The LSTM Autoencoder was trained using normal network traffic.

### Architecture

```text
Input Sequence
      ↓
LSTM Encoder
      ↓
Latent Representation
      ↓
RepeatVector
      ↓
LSTM Decoder
      ↓
Reconstructed Sequence
      ↓
Reconstruction Error
```

An anomaly threshold is derived from reconstruction errors observed on normal training data.

The basic principle is:

```text
Low Reconstruction Error
        ↓
Similar to learned normal behavior


High Reconstruction Error
        ↓
Potentially unusual behavior
```

---

# 📂 Dataset

This project uses the:

### CICIDS2017 — Canadian Institute for Cybersecurity Intrusion Detection System 2017

The dataset contains network-flow traffic representing normal activity and multiple attack categories.

Examples include:

* DoS
* DDoS
* PortScan
* Bot
* Brute Force
* Web Attacks
* Infiltration
* Heartbleed

---

## Dataset Processing Pipeline

```text
Raw CICIDS2017 CSV Files
          ↓
Column Cleaning
          ↓
Missing-Value Handling
          ↓
Infinite-Value Handling
          ↓
Duplicate Removal
          ↓
Feature Preparation
          ↓
Exploratory Data Analysis
          ↓
Feature Scaling
          ↓
Model-Ready Dataset
```

The original large CICIDS2017 CSV files are intentionally **not included in this repository**.

---

# 🛠️ Technology Stack

## Programming

* Python
* Jupyter Notebook

## Machine Learning

* Scikit-learn
* XGBoost

## Deep Learning

* TensorFlow
* Keras
* LSTM Autoencoder

## Explainable AI

* SHAP

## Data Processing

* Pandas
* NumPy

## Visualization

* Matplotlib
* Seaborn
* Plotly

## Dashboard / Interface

* Streamlit

## Model Serialization

* Joblib

## Version Control

* Git
* GitHub

---

# 📁 Project Structure

```text
Adaptive-Zero-Day-NIDS/
│
├── app.py
│
├── Adaptive_NIDS.ipynb
├── model_saving.ipynb
├── testing.ipynb
│
├── models/
│   ├── isolation_forest.pkl
│   ├── xgboost_model.pkl
│   ├── scaler.pkl
│   ├── lstm_autoencoder.keras
│   └── y_test.csv
│
├── reports/
│   ├── multi_model_consensus_results.csv
│   └── novelty_detection_results.csv
│
├── .gitignore
└── README.md
```

### Large local files

Large generated arrays such as:

```text
models/X_train_scaled.npy
models/X_test_scaled.npy
```

are intentionally excluded from GitHub because of their size.

They remain local development artifacts and are ignored through `.gitignore`.

---

# 📓 Notebook Workflow

## `Adaptive_NIDS.ipynb`

Main development and experimentation notebook containing the NIDS workflow.

It covers the data-processing and model-development stages of the project.

---

## `model_saving.ipynb`

Used to prepare and save trained model artifacts and preprocessing components.

---

## `testing.ipynb`

Used for model testing, evaluation, novelty experiments, and analysis of detection results.

---

## `app.py`

The Streamlit application that brings the trained NIDS components together into an interactive security dashboard.

---

# 📊 Reports

The project contains generated CSV reports for analysis.

### `multi_model_consensus_results.csv`

Contains results associated with the multi-model detection/consensus workflow.

### `novelty_detection_results.csv`

Contains results from the novelty/anomaly detection experiments.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/Saisruti-Mohanty/Adaptive-Zero-Day-NIDS.git
```

```bash
cd Adaptive-Zero-Day-NIDS
```

---

## 2. Create a virtual environment

On Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

---

## 3. Install dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install the main dependencies:

```bash
pip install streamlit pandas numpy scikit-learn xgboost tensorflow shap joblib matplotlib seaborn plotly
```

---

# ▶️ Running the Dashboard

From the project directory:

```bash
streamlit run app.py
```

The Streamlit dashboard provides an interactive environment for:

* Network-flow analysis
* Model selection
* Anomaly detection
* Attack classification
* Risk scoring
* Model consensus
* SHAP-based explanation
* What-If simulation
* Security analysis

---

# 🖥️ Dashboard Workflow

```text
Select / Input Network Flow
            ↓
     Feature Preparation
            ↓
       Data Scaling
            ↓
      Run Active Models
            ↓
    Calculate Model Signals
            ↓
      Generate Consensus
            ↓
     Calculate Risk Score
            ↓
      Assign Risk Level
            ↓
      Generate Explanation
            ↓
       Display Results
```

---

# 🔐 Security Risk Levels

### 🟢 Low — 0–30

Traffic appears broadly consistent with learned normal behavior.

### 🟡 Suspicious — 31–60

Some anomalous or attack-like signals are present.

### 🟠 High — 61–80

Multiple signals indicate potentially malicious behavior.

### 🔴 Critical — 81–100

Strong model signals indicate highly suspicious traffic.

> These levels are analytical indicators and are not a replacement for human security investigation.

---

# ⚠️ Limitations

This project is a **research/academic NIDS prototype**, not a production-ready enterprise intrusion detection system.

Important limitations include:

* CICIDS2017 is a benchmark dataset and may not represent current real-world network traffic.
* Random train/test splits can produce optimistic results when highly similar network flows appear in both sets.
* Zero-day detection cannot be guaranteed for arbitrary future attacks.
* Anomaly detectors can produce false positives.
* The LSTM Autoencoder operates on fixed-length sequences constructed from network flows.
* The adaptive risk score is an analytical aggregation rather than a calibrated probability of compromise.
* Real-world deployment would require continuous monitoring, threshold calibration, retraining, and validation on current network traffic.

---

# 🔮 Future Improvements

Possible future extensions include:

* 📡 Real-time packet capture using Scapy
* 🌐 Live network-flow ingestion
* ⚡ Streaming anomaly detection
* 🧪 Strict unseen-attack evaluation
* ⏱️ Time-based model evaluation
* 🔄 Automatic model retraining
* 🚨 Real-time alert notifications
* 🏢 SOC/SIEM integration
* 🌍 Threat-intelligence integration
* 📑 Automated SHAP security reports
* 📄 PDF incident reports
* 🐳 Docker deployment
* ☁️ Cloud deployment
* 🔐 Authentication and analyst roles

---

# 📌 Project Development Phases

```text
Phase 1   → Data Cleaning
Phase 2   → Exploratory Data Analysis
Phase 3   → Feature Preparation
Phase 4   → Isolation Forest
Phase 5   → XGBoost
Phase 6   → LSTM Autoencoder
Phase 7   → Multi-Model Consensus
Phase 8   → Adaptive Risk Score
Phase 9   → Novelty / Rare Attack Testing
Phase 10  → SHAP Explainable AI
Phase 11  → What-If Risk Simulator
Phase 12  → Streamlit Dashboard
Phase 13  → Model Packaging & Deployment Preparation
```

---

# 🎓 Project Objective

The main objective of this project is to develop an adaptive network-security system that combines:

```text
Detection
    +
Anomaly Analysis
    +
Attack Classification
    +
Explainability
    +
Risk Scoring
    +
Interactive Investigation
```

Rather than relying on a single binary prediction, the system provides multiple signals that can help analyze suspicious network behavior.

---

# ⭐ Key Takeaway

**Adaptive Zero-Day NIDS** combines:

> **Isolation Forest + XGBoost + LSTM Autoencoder + SHAP + Adaptive Risk Scoring + What-If Simulation + Streamlit**

to create an interactive AI-based network-security analysis platform.

The project demonstrates an end-to-end workflow from **network-flow preprocessing and machine-learning detection to explainability, risk assessment, novelty testing, and interactive visualization.**

---

# 👩‍💻 Author

### Saisruti Mohanty

**B.Tech — Computer Science & Engineering (Data Science)**

Interests:

* Artificial Intelligence
* Machine Learning
* Data Science
* Explainable AI
* Deep Learning
* Cybersecurity

---

## 📌 Repository

**Adaptive-Zero-Day-NIDS**

Built as an academic/research project exploring AI-driven network intrusion and anomaly detection.
