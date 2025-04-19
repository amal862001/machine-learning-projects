# Email PII Detection and Classification System

## 1. Introduction to the Problem Statement

The project addresses the critical need for automated detection and masking of Personally Identifiable Information (PII) in email communications. The system is designed to:
- Identify and mask sensitive personal information in email content
- Classify emails based on their content
- Provide a REST API interface for real-time processing

Key requirements:
- Detection of 8 types of PII: full names, email addresses, phone numbers, DOB, Aadhar numbers, credit/debit card numbers, CVV, and card expiry dates
- Accurate masking of detected PII while preserving email context
- Email classification for content categorization
- Real-time processing capability through API endpoints

## 2. Approach for PII Masking and Classification

### 2.1 PII Detection and Masking
- Implemented regex-based pattern matching for PII detection
- Each PII type has a specific regex pattern:
  ```python
  patterns = {
      'full_name': r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b',
      'email': r'\b[\w.-]+@[\w.-]+\.\w+\b',
      'phone_number': r'\b\d{10}\b',
      'dob': r'\b\d{2}/\d{2}/\d{4}\b',
      'aadhar_num': r'\b\d{12}\b',
      'credit_debit_no': r'\b\d{16}\b',
      'cvv_no': r'\b\d{3}\b',
      'expiry_no': r'\b\d{2}/\d{2}\b'
  }
  ```
- Entity tracking includes position, classification, and original text
- Masked text replaces PII with standardized tags (e.g., [full_name])

### 2.2 Classification System
- Two-step process:
  1. Text vectorization using TF-IDF
  2. Classification using Random Forest Classifier
- Modular design allowing easy model updates and maintenance

## 3. Model Selection and Training Details

### 3.1 Text Vectorization
- Selected TF-IDF (Term Frequency-Inverse Document Frequency) vectorizer
- Advantages:
  - Captures word importance in context
  - Handles varying email lengths
  - Reduces impact of common words

### 3.2 Classification Model
- Chosen model: Random Forest Classifier
- Rationale for selection:
  - Handles high-dimensional data well
  - Resistant to overfitting
  - Good performance with text classification tasks
  - Provides probability scores for predictions

### 3.3 Training Process
```python
def train_model(X_train, y_train, save_dir='model'):
    vectorizer = TfidfVectorizer()
    classifier = RandomForestClassifier()
    
    X_train_vectorized = vectorizer.fit_transform(X_train)
    classifier.fit(X_train_vectorized, y_train)
```
- Dataset split: 80% training, 20% testing
- Models saved separately for vectorizer and classifier
- Performance evaluation using accuracy score

## 4. Challenges Faced and Solutions Implemented

### 4.1 PII Detection Challenges
1. **Variable PII Formats**
   - Challenge: Different formats for same PII type
   - Solution: Flexible regex patterns and pattern testing

2. **False Positives**
   - Challenge: Numbers matching multiple patterns
   - Solution: Context-specific pattern matching and validation

### 4.2 System Architecture Challenges
1. **Model Loading**
   - Challenge: Model loading failures in production
   - Solution: Implemented error handling and graceful degradation
   ```python
   try:
       vectorizer, classifier = load_models()
   except Exception as e:
       print(f"Error loading models: {e}")
   ```

2. **API Performance**
   - Challenge: Processing large emails in real-time
   - Solution: Optimized regex matching and model inference

### 4.3 Future Improvements
1. Enhanced PII Detection:
   - Add support for international phone formats
   - Implement ML-based entity recognition
   - Add more PII types

2. System Optimization:
   - Implement batch processing
   - Add caching for frequent requests
   - Model compression for faster inference

## 5. API Usage

```python
# Example API request
payload = {
    "email_body": "Email content with PII"
}

# Example response
{
    "input_email_body": "Original text",
    "list_of_masked_entities": [
        {
            "position": [start, end],
            "classification": "entity_type",
            "entity": "matched_text"
        }
    ],
    "masked_email": "Masked text",
    "category_of_the_email": "predicted_category"
}
```

The system provides a robust solution for PII detection and email classification while maintaining extensibility for future improvements.
