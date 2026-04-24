

# 🛡️ Web Shield :Real-Time Deep Learning-Based Web Threat Detection System

## 📌 Overview

Web Shield is a real-time browser security system that leverages **Deep Learning** and intelligent heuristics to detect and prevent malicious web activities.

It is designed to identify multiple categories of cyber threats directly from webpage content, ensuring proactive protection for users during browsing.

The system integrates a **Chrome Extension frontend** with a **Deep Learning-powered backend**, enabling seamless and efficient threat detection.

---

## 🚀 Key Features

### 🔍 Multi-Class Threat Detection

Detects various web-based attacks such as:

* Phishing
* Cross-Site Scripting (XSS)
* Clickjacking
* Cookie Theft
* Safe Content Classification

---

### 🧠 Deep Learning-Based Classification

Utilizes advanced models (e.g., LSTM/CNN-based architectures) to analyze webpage content and identify hidden malicious patterns.

---

### ⚡ Real-Time Analysis

Performs instant threat evaluation as users browse websites.

---

### 🧩 Hybrid Detection Mechanism

Combines:

* Deep Learning predictions
* Rule-based DOM analysis

---

### 🎯 Risk Scoring System (0–100)

Provides a clear and interpretable threat level:

* 🟢 Safe
* 🟠 Suspicious
* 🔴 Dangerous

---

### 🌐 Browser Extension Integration

Displays:

* Live risk score
* Detected attack type
* Warning alerts for unsafe pages

---

## 🏗️ System Architecture

```
User 
  ↓
Chrome Extension 
  ↓
Content Extraction (HTML + URL)
  ↓
Background Script
  ↓
Backend API (Flask)
  ↓
Detection Engine
   ├── DOM Analysis
   └── Deep Learning Model
  ↓
Risk Score + Classification
  ↓
Extension UI (Popup + Warning)
```

---

## 🧪 Technologies Used

**Frontend:**

* Chrome Extension (JavaScript, HTML, CSS)

**Backend:**

* Flask (Python)

**Deep Learning:**

* TensorFlow / Keras / PyTorch

**Text Processing:**

* Tokenization, Embeddings

**Model Type:**

* LSTM / CNN / Hybrid Deep Learning

---


