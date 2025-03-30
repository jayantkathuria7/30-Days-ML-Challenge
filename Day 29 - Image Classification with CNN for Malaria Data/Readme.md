# Malaria Image Classification using CNN

## Overview
This project focuses on classifying malaria-infected and uninfected cell images using a Convolutional Neural Network (CNN). The model was trained on the **Cell Images for Detecting Malaria** dataset and achieved a test accuracy of **94.92%**.

## Dataset
- **Source:** [Kaggle - Cell Images for Detecting Malaria](https://www.kaggle.com/datasets/iarunava/cell-images-for-detecting-malaria)
- **Description:** The dataset consists of two categories of cell images:
  - **Parasitized:** Cells infected with malaria.
  - **Uninfected:** Healthy cells.
- **Structure:**
  - Total Images: 27,558
  - Each category contains 13,779 images.

## Data Preprocessing
- Loaded and explored the dataset.
- Resized images to **(64x64)** for uniformity.
- Applied normalization to scale pixel values between **0 and 1**.
- Used **train-test split (80-20)** to divide the dataset.

## Model Architecture
A **CNN** was implemented with the following layers:
1. **Conv2D (32 filters, 3x3, ReLU activation)**
2. **MaxPooling2D (2x2)**
3. **Conv2D (64 filters, 3x3, ReLU activation)**
4. **MaxPooling2D (2x2)**
5. **Flatten layer**
6. **Dense (128 units, ReLU activation)**
7. **Dropout (0.5) for regularization**
8. **Dense (1 unit, Sigmoid activation)**

## Training
- **Loss Function:** Binary Crossentropy
- **Optimizer:** Adam
- **Epochs:** 10
- **Batch Size:** 32

## Results
| Metric          | Value  |
|----------------|--------|
| Test Accuracy  | 94.92% |
| Training Loss  | Low    |
| Validation Loss| Low    |

## Notebook
The complete implementation is available on Kaggle: [Malaria Image Classification Notebook](https://www.kaggle.com/code/jayantkathuria/image-classification-with-cnn-for-malaria-data)

## Future Improvements
- Implement deeper CNN architectures (ResNet, EfficientNet).
- Use Transfer Learning to further enhance accuracy.
- Experiment with additional data augmentation techniques.
