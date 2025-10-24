
# 📦 Box Predictor (Python Package)

This project provides a self-contained Python module for predicting how many boxes of each dimension are required for a given order. It uses a fine‑tuned **Optuna Random Forest** model and supports integration with **Google’s ADK Agent framework** for LLM-based automation.

---

## 🧠 What It Does

- Accepts category‑wise product quantities as input.  
- Builds a structured feature vector (with total, average, and max quantities).  
- Runs predictions using the saved **Optuna‑tuned Random Forest model**.  
- Returns estimated counts for each box size used in packaging.  

---

## 📂 Project Structure

```
box_predictor/
│
├── box_predictor/
│   ├── agent.py                     # Core agent integration & prediction logic
│   ├── utils.py                     # Input schema and feature definitions
│   ├── optuna_random_forest_model2.pkl  # Model file
│   ├── optuna_random_forest1_model.pkl  # Alternate trained model
│   └── .env                         # Optional env vars (for ADK)
│
├── requirements.txt
└── venv/                            # Local environment (optional)
```

---

## ⚙️ Setup Instructions

1. **Clone or extract the folder**
   ```bash
   git clone <repo-link>
   cd box_predictor
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate       # Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Place or update your model**
   The code looks for:
   ```
   box_predictor/box_predictor/optuna_random_forest_model2.pkl
   ```
   You can download the latest fine-tuned model from your **`box-prediction-notebook` repository** and replace this file.

---

## 🚀 How to Use

### 1. Direct Python Use
```python
from box_predictor.agent import _build_feature_row, model
from box_predictor.utils import INPUT_CATEGORIES, BOX_DIMENSIONS

# Example input
quantities = [10, 0, 2, 4, 0, 3, 0, 1, 0, 0, 5]
features = _build_feature_row(INPUT_CATEGORIES, quantities)
prediction = model.predict([features])[0]

for box, count in zip(BOX_DIMENSIONS, prediction):
    print(f"{box}: {round(count)}")
```

---

### 2. Using as an ADK Agent
The `Agent` class from `google.adk.agents` can load this model into a multi-agent workflow.  
Example snippet (simplified):

```python
from box_predictor.agent import Agent, predict_boxes

agent = Agent("BoxPredictor")
result = agent.handle_input({
    "categories": INPUT_CATEGORIES,
    "quantities": [5, 1, 0, 0, 3, 0, 2, 0, 0, 1, 0]
})
print(result)
```

---

## 🧩 How It Works

1. **Feature Construction**
   - Builds total, average, and maximum quantity features.
   - Preserves input category order for consistency with training.

2. **Model Prediction**
   - Loads the `optuna_random_forest_model2.pkl` on import.
   - Predicts the required number of boxes for each defined size.

3. **Outputs**
   - Returns a 1×16 array representing counts for each box dimension:
     ```
     ["10x10x10", "12x18x10", ..., "8x8x13"]
     ```

---

## 🧾 Requirements

```
numpy
joblib
google-adk
scikit-learn
```

Add `python-dotenv` if you use `.env` for configuration.

---

## 🔧 Customization

- **Retrain Model:** You can fine-tune or replace the existing model by saving a new `.pkl` file with the same feature order.
- **Modify Features:** Edit `utils.py` to include or remove product categories.
- **Integrate Anywhere:** Works as a standalone Python module or as part of an LLM agent pipeline.

---

## 🧠 Model Source

The fine‑tuned Optuna Random Forest model used here can be downloaded from the  
**[`box-prediction-notebook`](https://github.com/yourusername/box-prediction-notebook)** repository.  
That repo contains the full Jupyter training notebook and parameter search setup.

---

## 🧭 Quick Start Summary

```bash
# 1. Setup
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# 2. Run a test prediction
python -m box_predictor.agent
```

The script will print predicted counts for all box dimensions.
