# Shogi

Shogi, often called Japanese Chess, is a two-player strategy board game that is a popular variant of chess in Japan. Unlike Western chess, Shogi allows players to reuse captured pieces as their own, adding a dynamic layer of strategy. The objective is to capture the opponent's king, using a unique set of pieces with distinct movement rules and promotion mechanics. This project explores the game of Shogi through AI modeling, coin detection.

-----------------------------------------------------------------------------------------------------------------

# ♟️ Shogi Coin Detection with YOLOv8

This project focuses on detecting and classifying coins (pieces) in the traditional Japanese board game Shogi using YOLOv8. The dataset was prepared using Roboflow with extensive preprocessing and augmentation techniques to improve model accuracy across various lighting conditions.
📁 Dataset Preparation

    Annotated and labeled using Roboflow

    Extracted and trained in YOLOv8 format

🔧 Preprocessing Steps

    Auto-Orient

    Resize – Stretch to 640x640

    Grayscale

🎨 Augmentation Techniques

    Rotation: ±10°

    Shear: ±5° (Horizontal & Vertical)

    Hue: ±13°

    Brightness: ±20%

    Exposure: ±6%

    Blur: Up to 1.5px

    Noise: Up to 1.01% of pixels

    💡 Use brightness.py to generate image variations under different lighting conditions.

-----------------------------------------------------------------------------------------------------------------

Ultralytics-Yolo V8 model codes are available in 

https://docs.ultralytics.com/modes/train/#usage-examples

-----------------------------------------------------------------------------------------------------------------

📦 Dataset Versioning

    Maximum version size: 3x

🧠 Model Training

    Use training.ipynb to train the YOLOv8 model on the preprocessed dataset.

🎯 Inference

    Sample code to predict coins from both images and videos is included in training.ipynb.

📂 Extra

    Some dataset generation and manipulation code is available in dataset_codes.ipynb.

-----------------------------------------------------------------------------------------------------------------