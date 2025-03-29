# Face Mask Detection

## 📌 Overview
This project focuses on real-time face mask detection using deep learning and OpenCV. It classifies whether a person is wearing a mask or not, making it useful for public safety applications.

## 📂 Dataset
- **Dataset Used:** Face Mask Detection Dataset (contains images of people with and without masks).
- **Source:** [Kaggle](https://www.kaggle.com/datasets/omkargurav/face-mask-dataset)
- **Classes:**
  - `Mask` (Person wearing a mask)
  - `No Mask` (Person without a mask)

## 🔧 Project Workflow
1. **Data Preprocessing**
   - Loaded and cleaned dataset
   - Resized images to required dimensions
   - Augmented data for better model generalization

2. **Model Development**
   - Used CNN model
   - Fine-tuned layers to optimize performance

3. **Training & Evaluation**
   - Split dataset into training and validation sets
   - Achieved high accuracy on test data

4. **Real-Time Detection**
   - Integrated OpenCV for real-time face detection
   - Implemented a detection script using webcam feed
   - The model predicts mask presence in live video streams

## 📊 Results
| Model | Accuracy | Precision | Recall | F1-Score |
|--------|----------|------------|---------|----------|
| CNN | 95.6% | 96.1% | 95.2% | 95.6% |

## 🚀 How to Run the Project
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/face-mask-detection.git
   cd face-mask-detection
   ```
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Detection Script**
   ```bash
   python real_time_detection.py
   ```

## 📌 Key Features
✅ Real-time detection using OpenCV  
✅ Deep Learning (CNN architecture
✅ High accuracy and fast inference  
✅ Suitable for public safety and health monitoring  

## 📜 Future Improvements
- Deploy as a web app or mobile application
- Integrate face recognition for identity-based monitoring

