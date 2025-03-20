# CIFAR-10 Image Classification using MobileNetV2

## 📌 Project Overview
This project focuses on classifying images from the CIFAR-10 dataset using the MobileNetV2 architecture. MobileNetV2 is an efficient deep learning model optimized for mobile and edge devices, balancing accuracy and computational efficiency.

---

## 📂 Dataset Information
The **CIFAR-10 dataset** consists of **60,000 images** (32x32 pixels, 10 classes):
- **Classes**: Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, Truck.
- **Training Data**: 50,000 images.
- **Testing Data**: 10,000 images.

📌 **Dataset Source:** [CIFAR-10 Dataset](https://www.cs.toronto.edu/~kriz/cifar.html)

---

## 🛠️ Technologies & Tools Used
- **Python**
- **TensorFlow/Keras**
- **MobileNetV2**
- **Matplotlib & Seaborn (for Visualization)**
- **NumPy & Pandas**

---

## 🔧 Project Workflow

### 1️⃣ Data Preprocessing
✔️ Loaded CIFAR-10 dataset from Keras datasets module.
✔️ Normalized pixel values (0 to 1) for better model convergence.
✔️ Converted labels into categorical format (one-hot encoding).

### 2️⃣ Model Architecture: MobileNetV2
✔️ Used **MobileNetV2** as a feature extractor.
✔️ Added custom **fully connected layers** for classification.
✔️ Implemented **GlobalAveragePooling** for efficiency.

### 3️⃣ Model Compilation & Training
✔️ **Optimizer:** Adam (Adaptive Learning Rate Optimization)
✔️ **Loss Function:** Categorical Crossentropy
✔️ **Metrics:** Accuracy
✔️ **Batch Size:** 64
✔️ **Epochs:** 20

### 4️⃣ Model Evaluation & Visualization
✔️ Evaluated model performance on test data.
✔️ Generated accuracy & loss curves.
✔️ Displayed a confusion matrix for detailed performance insights.
✔️ Visualized sample predictions.

---

## 📈 Performance Metrics
- **Training Accuracy:** Achieved over **85%** accuracy.
- **Test Accuracy:** Approximately **80%**.
- **Loss Trend:** Decreasing trend indicating good learning.

---

## 📊 Results & Insights
🔹 MobileNetV2 performed well with high accuracy while maintaining computational efficiency.
🔹 Misclassifications observed in visually similar classes (e.g., Cats vs. Dogs).
🔹 Further improvements could include **data augmentation** or **fine-tuning additional layers**.

---

## 📌 How to Run the Project
1. Install dependencies:
   ```bash
   pip install tensorflow numpy matplotlib seaborn
   ```
2. Run the Jupyter Notebook:
   ```bash
   jupyter notebook Cifar_10_Image_Classification_using_MobileNetv2.ipynb
   ```

---

## 📚 References
- MobileNetV2 Paper: [Sandler et al., 2018](https://arxiv.org/abs/1801.04381)
- TensorFlow Keras Documentation: [TensorFlow Guide](https://www.tensorflow.org/guide/keras)
- CIFAR-10 Dataset: [Krizhevsky, 2009](https://www.cs.toronto.edu/~kriz/cifar.html)


