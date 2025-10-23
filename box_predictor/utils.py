# utils.py

INPUT_CATEGORIES = [
    "Category_100cc",
    "Category_1100ml",
    "Category_12 weight|kg",   # fixed name
    "Category_150g",
    "Category_4240cc",
    "Category_500G",
    "Category_5lbs",
    "Category_710ml",
    "Category_8150ml",
    "Category_900ml",
    "Category_C box 16*12*11.5"  # fixed name
]

# All features must match training order exactly
ALL_FEATURES = [
    "Total No. Of Quantity",
    "Avg Quantity",
    "Max Quantity"
] + INPUT_CATEGORIES

# Outputs (box dimensions) must also match training order
BOX_DIMENSIONS = [
    "10x10x10", "12x18x10", "12x8x20", "18x17x27", "20x20x34", "30x30x29",
    "32x20x17", "38x30x20", "40x30x29", "40x30x34", "40x40x34", "42x42x30",
    "48x34x27", "60x30x30", "8x22x13", "8x8x13"
]
