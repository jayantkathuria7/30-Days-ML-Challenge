# Brain Tumor Classification using CNN

## Overview
This project focuses on classifying brain tumors from MRI images using a **Convolutional Neural Network (CNN)**. The model is trained on a publicly available dataset and achieves a **test accuracy of 93.49%**.

## Dataset
- **Name:** Brain Tumor MRI Dataset
- **Source:** [Kaggle](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
- **Description:** The dataset contains MRI images labeled as **tumor** or **non-tumor**.
- **Categories:** Glioma Tumor, Meningioma Tumor, Pituitary Tumor, No Tumor

## Project Pipeline
### 1. Data Preprocessing
- Loaded the dataset and performed image augmentation.
- Resized images to **224x224** for consistency.
- Normalized pixel values to **[0,1]**.

### 2. Model Architecture
The CNN model consists of:
- **Convolutional Layers** with ReLU activation
- **MaxPooling Layers** for dimensionality reduction
- **Dropout Layers** to prevent overfitting
- **Fully Connected Dense Layers** for classification
- **Softmax Activation** for multi-class output

### 3. Training Process
- **Loss Function:** Categorical Crossentropy
- **Optimizer:** Adam
- **Batch Size:** 32
- **Epochs:** 25
- **Train-Test Split:** 80-20 ratio
- **Augmentation:** Used techniques like rotation, flipping, and zooming

### 4. Evaluation
| Metric        | Value  |
|--------------|--------|
| **Test Accuracy** | **93.49%** |
| **Loss**        | Lower than training loss, indicating good generalization |

## Results
- The model successfully differentiates between tumor and non-tumor MRI scans.
- High accuracy suggests effective feature extraction and classification.
- Can be further improved by experimenting with **more layers, transfer learning, or hyperparameter tuning**.

## References
- **Dataset:** [Brain Tumor MRI Dataset](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset)
- **Kaggle Notebook:** [Brain Tumor Classification](https://www.kaggle.com/code/jayantkathuria/brain-tumor-classification)

## Future Improvements
- Implement **Transfer Learning** using pre-trained models like **VGG16, ResNet**.
- Use **more data augmentation** for robustness.
- Optimize model hyperparameters for better performance.


