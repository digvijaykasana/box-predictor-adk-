# box_predictor/agent.py

import os
import joblib
import numpy as np
from typing import List
from google.adk.agents import Agent

from .utils import INPUT_CATEGORIES, ALL_FEATURES, BOX_DIMENSIONS

MODEL_FILENAME = "optuna_random_forest_model2.pkl"
MODEL_PATH = os.path.join(os.path.dirname(__file__), MODEL_FILENAME)

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    raise RuntimeError(f"Failed to load model from {MODEL_PATH}: {e}")

def _build_feature_row(categories: List[str], quantities: List[int]) -> np.ndarray:
    if len(categories) != len(quantities):
        raise ValueError("categories and quantities must have the same length")

    feats = {name: 0 for name in ALL_FEATURES}

    for cat, qty in zip(categories, quantities):
        if cat in INPUT_CATEGORIES:
            feats[cat] = int(qty) if qty is not None else 0

    total_qty = sum(int(q or 0) for q in quantities) if quantities else 0
    feats["Total No. Of Quantity"] = total_qty
    feats["Avg Quantity"] = (total_qty / len(quantities)) if quantities else 0
    feats["Max Quantity"] = max(int(q or 0) for q in quantities) if quantities else 0

    row = [feats[name] for name in ALL_FEATURES]
    return np.array([row], dtype=float)

def predict_boxes(categories: List[str], quantities: List[int]) -> dict:
    try:
        X = _build_feature_row(categories, quantities)
        y = model.predict(X)[0]
        cleaned = [max(0, int(round(v))) for v in y]
        predictions = {dim: cnt for dim, cnt in zip(BOX_DIMENSIONS, cleaned)}
        formatted = "📦 Predicted Box Counts:\n" + "\n".join([f"{dim}: {cnt}" for dim, cnt in predictions.items()])

        return {
            "status": "success",
            "predictions": formatted
}
    except Exception as e:
        return {"status": "error", "message": str(e)}

root_agent = Agent(
    name="box_predictor",
    model="gemini-2.0-flash",
    description="Predicts packing box counts from category quantities.",
    instruction=(
        "You are a box prediction agent. "
        "When the user provides categories and quantities, call the tool "
        "`predict_boxes` with two arguments: `categories` (list[str]) and "
        "`quantities` (list[int]). If something is missing, ask for it."
    ),
    tools=[predict_boxes],
)
