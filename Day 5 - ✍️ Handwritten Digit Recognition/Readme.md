# MNIST Handwritten Digit Classification

## 📌 Project Overview
This project is a **handwritten digit classification** model built using **TensorFlow and Keras**. The goal is to train a neural network to recognize and classify digits (0-9) from the **MNIST dataset**. This is part of my **30 Days of Machine Learning Challenge (Day 5).**

## 📊 Dataset: MNIST Handwritten Digits
The MNIST dataset is a collection of **70,000 grayscale images** of handwritten digits, each **28x28 pixels** in size. It consists of:
- **Training Set:** 60,000 images
- **Test Set:** 10,000 images
- **Classes:** 10 (digits 0-9)

Each image represents a single digit, and the task is to classify it correctly.

## 🛠️ Technologies Used
- **Python** (Programming Language)
- **TensorFlow & Keras** (Deep Learning Frameworks)
- **NumPy** (Numerical Computing)
- **Matplotlib & Seaborn** (Data Visualization)

## 🔧 Project Workflow
### 1️⃣ Import Dependencies
We start by importing the necessary libraries, including TensorFlow, NumPy, and Matplotlib for visualization.

### 2️⃣ Load & Preprocess Data
- Load the MNIST dataset using `tensorflow.keras.datasets.mnist.load_data()`.
- Normalize pixel values to the range **[0,1]** by dividing by 255.
- Reshape data if necessary for model input.

### 3️⃣ Build the Neural Network Model
A simple **feedforward neural network** (fully connected) is used:
1. **Flatten Layer**: Converts the 28x28 image into a 1D vector (784 features).
2. **Hidden Layers**: Two dense layers with **ReLU activation**.
3. **Output Layer**: A softmax layer with 10 neurons (one for each class).

```python
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])
```

### 4️⃣ Compile the Model
The model is compiled with:
- **Loss Function:** `sparse_categorical_crossentropy` (for multi-class classification)
- **Optimizer:** `adam` (adaptive learning rate optimization)
- **Metric:** `accuracy`

```python
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
```

### 5️⃣ Train the Model
The model is trained using **`model.fit()`** for 10 epochs:
```python
history = model.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
```

### 6️⃣ Evaluate Performance
- Model performance is evaluated using **accuracy & loss curves**.
- The trained model is tested on unseen data (**x_test**).

### 7️⃣ Visualizing Model Predictions
We visualize sample predictions to check model correctness.

## 📈 Results & Accuracy
- Achieved around **98% accuracy** on the training set.
- Test accuracy is around **97%**, indicating a well-generalized model.

## 🔥 Key Takeaways
✔️ Preprocessing improves model performance (normalization).  
✔️ `ReLU` activation works well for deep networks.  
✔️ `softmax` activation in the output layer is crucial for multi-class classification.  
✔️ Adam optimizer provides faster convergence.  
✔️ Adding **dropout layers** in future versions may reduce overfitting.  

## 🚀 Future Improvements
- Implement **CNNs** for better feature extraction.
- Use **Dropout & Batch Normalization** to improve generalization.
- Fine-tune hyperparameters using Keras `Tuner`.

## 📝 How to Run the Project
1. Install dependencies:  
   ```bash
   pip install tensorflow numpy matplotlib seaborn
   ```
2. Run the Python script:  
   ```bash
   python mnist_classification.py
   ```
3. View model accuracy and sample predictions.

## 📂 File Structure
```
📦 mnist-classification
 ┣ 📜 mnist_classification.py  # Main script
 ┣ 📜 README.md                # Documentation
 ┣ 📜 requirements.txt         # Dependencies
 ┗ 📂 images                   # Sample output images
```

## 🤝 Contributing
Feel free to fork this repo, make improvements, and submit a pull request! 🚀

## 📌 Project Status
✅ Completed (Base Model)  
🔄 Future improvements planned (CNNs, Hyperparameter Tuning)



