import argparse
import os
import numpy as np
import pandas as pd
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from utils import list_images

def preprocess(img, target_size=(224, 224)):
    img = img.convert("RGB").resize(target_size)
    arr = img_to_array(img) / 255.0
    return np.expand_dims(arr, axis=0)

def main():
    parser = argparse.ArgumentParser(description="Run inference with a trained face-mask CNN.")
    parser.add_argument("--model", required=True, help="Path to Keras .h5/.keras model")
    parser.add_argument("--input", required=True, help="Path to an image or directory")
    parser.add_argument("--output", default="predictions.csv", help="Where to write predictions CSV")
    parser.add_argument("--class-names", nargs="+", default=["with_mask", "without_mask"], help="Class order in the model output")
    args = parser.parse_args()

    model = load_model(args.model)
    files = list_images(args.input)
    rows = []

    for fp in files:
        try:
            with Image.open(fp) as im:
                x = preprocess(im)
                probs = model.predict(x, verbose=0)[0]
                idx = int(np.argmax(probs))
                pred = args.class_names[idx] if idx < len(args.class_names) else str(idx)
                rows.append({"file": fp, "prediction": pred, "confidence": float(np.max(probs))})
        except Exception as e:
            rows.append({"file": fp, "prediction": "ERROR", "confidence": 0.0})

    df = pd.DataFrame(rows)
    df.to_csv(args.output, index=False)
    print(f"Wrote {len(df)} predictions to {args.output}")

if __name__ == "__main__":
    main()
