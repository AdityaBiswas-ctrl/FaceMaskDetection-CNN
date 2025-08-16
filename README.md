# FaceMaskDetection-CNN
# Face Mask Detection (CNN)

A clean, ready-to-push GitHub repository scaffolding for a **face mask detection** project using a Convolutional Neural Network (CNN).  
It includes your uploaded notebook and a minimal Python script for inference, along with reproducible environment files and CI for formatting checks.

> Created on 2025-08-16.

## Repository Structure
```
face-mask-detection-cnn/
├── notebooks/
│   └── FaceMaskDetection(CNN)project6.ipynb   # your original notebook
├── src/
│   ├── infer.py                               # load a saved model and run on an image or folder
│   └── utils.py                               # helper functions
├── data/                                      # put datasets here (ignored by git)
├── models/                                    # trained models go here (ignored by git)
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
└── .github/workflows/python-checks.yml        # basic lint/format CI
```

## Quickstart

1. **Create and activate a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

2. **Open the notebook**
```bash
jupyter notebook notebooks/FaceMaskDetection(CNN).ipynb
```

3. **(Optional) Run inference with a saved model**
```bash
python src/infer.py --model models/best_model.h5 --input <path_to_image_or_dir> --output predictions.csv
```

## Dataset

- Place your training data under `data/` in a structure like:
```
data/
├── train/
│   ├── with_mask/
│   └── without_mask/
└── val/
    ├── with_mask/
    └── without_mask/
```
This mirrors common Keras/TensorFlow `ImageDataGenerator` directory conventions.

## Results
- Save trained weights as `models/best_model.h5` (or `.keras`) from the notebook.
- Add sample outputs to the README once you train.

## How to publish to GitHub

```bash
git init
git add .
git commit -m "Initial commit: face mask detection (CNN)"
git branch -M main
git remote add origin https://github.com/<your-username>/face-mask-detection-cnn.git
git push -u origin main
```

## License
MIT — see [LICENSE](LICENSE).
