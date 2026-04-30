# ⚛️ Quantum vs Classical Volatility Framework

A research-driven framework comparing **classical financial models** (GARCH, Monte Carlo) with **quantum approaches** (QAE, VQC) for volatility estimation, probabilistic forecasting, and risk analysis.

---

## 🚀 Overview

This project investigates whether **quantum algorithms provide practical advantages** over classical methods in financial modeling.

It evaluates models across:

- 📊 Volatility Estimation  
- 📈 Trend Prediction  
- 🔁 Reversal Detection  
- 🧠 Bayesian Forecasting  

Using both **real-world data (SPY ETF)** and **synthetic datasets (GBM)**.

---

## 🧠 Models Implemented

### 🔵 Classical Models
- GARCH (1,1)
- EGARCH
- Historical Volatility
- Monte Carlo Simulation
- Logistic Regression (Trend/Reversal)

### 🟣 Quantum Models
- Quantum Amplitude Estimation (QAE)
- Quantum Monte Carlo (Q-MC)
- Variational Quantum Circuits (VQC)
- Quantum Bayesian Circuit

---

## 📊 Evaluation Metrics

- MSE, MAE, RMSE  
- KL Divergence  
- VaR / CVaR  
- Correlation  
- Bias  
- KS Test  

---

## 📈 Results (Key Insights)

- ✅ Classical models outperform quantum methods in **accuracy and stability**
- ❌ Quantum models suffer from:
  - Barren plateaus  
  - Encoding inefficiencies  
  - Simulation overhead  

> ⚠️ Quantum advantage remains theoretical under current NISQ constraints.

---

## 📸 Sample Outputs

### Predicted vs Realized Volatility
![Volatility](results/figures/predicted_vs_actual.png)

### Error Comparison
![Errors](results/figures/error_comparison.png)

### Distribution Analysis
![Distribution](results/figures/distribution_comparison.png)

---

## 🧪 Project Structure

```bash
vol_framework
├── data
├── models
│   ├── classical
│   └── quantum
├── evaluation
├── visualization
├── run_experiment.py
├── demo_standalone.py
├── requirements.txt
└── README.md
```
---

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```
### 2.Run experiment
```bash
python run_experiment.py
```
---
## ⚛️ Quantum Circuit Example

- Uses **Hadamard gates** to create superposition  
- Applies **rotation gates (RY / RZ)** for probability encoding  
- Introduces **entanglement (CNOT)** to capture dependencies  
- Measures qubits to obtain **probability distributions**

---

## 📌 Key Takeaways

- ✅ Classical methods remain dominant in real-world financial modeling  
- ❌ Quantum models are currently limited by:
  - Barren plateaus in training  
  - Inefficient data encoding  
  - Simulator and hardware noise  

---

## 🚀 Future Work

- Hybrid **quantum-classical models**
- Execution on **real quantum hardware**
- Improved **VQC optimization strategies**
- Advanced **stochastic and probabilistic modeling**

---

## 📚 References

- Bollerslev (1986) — GARCH  
- Brassard et al. (2000) — Quantum Amplitude Estimation (QAE)  
- Preskill (2018) — NISQ Era  
- Glasserman (2003) — Monte Carlo Methods in Finance  

---

## 👨‍💻 Author

**Punith V**
