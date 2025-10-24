# Box Predictor — ADK Agent (Optima)

This repository is the **ADK (Google Gemini) agent** that wraps the trained **Optima** model for **box-packing prediction**. 


## What it does
- Accepts **natural-language prompts** (via Google ADK → Gemini).
- Parses and validates request parameters (items, quantities, sizes, constraints).
- Loads the **Optima** model artifacts and returns **box counts/sizes** in text and/or JSON.

## Repos in the system
- **Training**: `box-predictor-notebooks` (Optima) — exports `model.joblib`, `preprocess.joblib`, `schema.json`.
- **Agent (this repo)**: wraps those artifacts with the ADK/Gemini reasoning layer.
- **UI**: `box-predictor-streamlit` — calls this agent and renders results.

---

## Folder structure (unchanged)
```
box_predictor/              # your existing package
  ├─ __init__.py
  ├─ agent.py               # ADK agent / entry (your file)
  ├─ utils.py               # helpers (your file)
  └─ ...                    # any other modules kept intact
artifacts/                  # placeholder only (see below)
README.md
.env.example                # create .env from this
.gitignore
requirements.txt
```



---

## Requirements
Ensure these (add to `requirements.txt` if missing):
```
google-adk
python-dotenv
joblib
pandas
numpy
scikit-learn
xgboost
```

---

## Setup
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pip install -U google-adk        # if not already installed
cp .env.example .env
```

### .env (create from `.env.example`)
```
GOOGLE_API_KEY=your_gemini_api_key
MODEL_PATH=./artifacts/model.joblib
PREPROCESS_PATH=./artifacts/preprocess.joblib
SCHEMA_PATH=./artifacts/schema.json
```

### Model artifacts
Download/export these from **box-predictor-notebooks (Optima)** and place them in `./artifacts/`:
- `model.joblib`
- `preprocess.joblib`
- `schema.json`

> We include `artifacts/README_PLACEHOLDER.md` and `.gitkeep` so the folder exists but **no heavy files are tracked**.

---

## Run
**Web UI (ADK)**
```bash
adk web
```

**CLI**
```bash
adk run
# or if you prefer a direct module entry:
python -m box_predictor.agent
```

---

## Prompt examples
**Natural**
> Predict boxes for 20 whey 2kg tubs and 6 shakers.

**What‑if**
> If all item volumes increase by 15%, how many boxes now? Return JSON only.

**Expected JSON (illustrative)**
```json
{
  "boxes": [{"size":"Large","count":3},{"size":"Medium","count":1}],
  "note": "Optima model with volume adjustment applied."
}
```

---

## Debugging
- `FileNotFoundError` → check `MODEL_PATH` / `PREPROCESS_PATH` / `SCHEMA_PATH`.
- `KeyError` / shape mismatch → verify `schema.json` matches features used at training time.
- ADK import issues → `pip install -U google-adk`.

---

## Push to GitHub
```bash
git init
git add .
git commit -m "Initial commit: Box Predictor — ADK Agent (Optima)"
git branch -M main
git remote add origin https://github.com/digvijaykasana/box-predictor-adk.git
git push -u origin main
```
