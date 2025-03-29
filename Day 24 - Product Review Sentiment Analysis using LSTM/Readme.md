# Product Review Sentiment Analysis with LSTM

## Objective
Classify Amazon food reviews as positive or negative using an LSTM model, leveraging NLP preprocessing and GloVe embeddings for enhanced text representation.

## Data Overview
- **Dataset:** 568k+ Amazon food reviews (Reviews.csv)
  - [Amazon Fine Food Reviews Dataset](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews)
- **Key Features:**
  - Score (1–5 ratings)
  - Review Text (content of the review)
- **Class Imbalance:**
  - 64% 5-star, 9% 1-star
  - Addressed via stratification and oversampling

## Workflow
### Data Preprocessing
- **Cleaning:**
  - Convert text to lowercase
  - Remove URLs, numbers, and punctuation
  - Remove stopwords (nltk), apply stemming (PorterStemmer)
  - Handle repeated characters (e.g., "goooood" → "good")

### Exploratory Analysis
- **Class Distribution:** Visualized using count plots and pie charts.
- **Word Clouds:** Highlighted key terms for each rating (e.g., "delicious" for 5-star, "awful" for 1-star).

### Text Vectorization
- **Tokenization:** Converted text to sequences using TensorFlow/Keras.
- **Padding:** Standardized sequence length for LSTM input.
- **GloVe Embeddings:** Loaded pre-trained 100D vectors (glove.6B.100d.txt) and created an embedding matrix.
  - [GloVe Embeddings (100D)](https://www.kaggle.com/datasets/danielwillgeorge/glove6b100dtxt)

## LSTM Model
### Architecture
- **Embedding Layer:** Pre-trained GloVe weights (non-trainable)
- **LSTM Layer:** 64–128 units
- **Dense Layers:** Includes dropout for regularization

### Training
- Train/test split (80/20), ensuring stratified sampling.
- **Optimizer:** Adam
- **Loss Function:** Sparse categorical cross-entropy

## Evaluation
- **Metrics:** Accuracy, Precision, Recall, F1-score (to handle class imbalance effectively).
- **Confusion Matrix:** Visualized True Positives, True Negatives, False Positives, and False Negatives.
- **Training Curves:** Monitored loss and accuracy over epochs.

## Results
- Achieved **~X%** test accuracy (replace with actual results).
- Key Insight: LSTM effectively captured context (e.g., "not good" vs. "good").
- **Error Analysis:** LSTM struggled with sarcasm and neutral-toned reviews.

## Tools & Libraries
- **NLP:** nltk, regex, WordCloud
- **Embeddings:** Pre-trained GloVe vectors
- **Modeling:** TensorFlow/Keras (LSTM, tokenization, padding)
- **Visualization:** matplotlib, seaborn

## Why This Approach?
- **LSTM:** Ideal for sequential data and context preservation.
- **GloVe Embeddings:** Better semantic understanding compared to training embeddings from scratch.
- **Stratification:** Balanced dataset for robust model evaluation.

## Key Takeaways
- Preprocessing techniques (stemming, embeddings) significantly impact model performance.
- Class imbalance needs careful handling (F1-score > accuracy for evaluation).
- LSTM excels in sentiment understanding but struggles with nuanced language like sarcasm.

## Kaggle Notebook
You can find the complete implementation and code in the following Kaggle Notebook:
[Product Review Sentiment Analysis using LSTM](https://www.kaggle.com/code/jayantkathuria/product-review-sentiment-analysis-using-lstm)
