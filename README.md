
# Fake Job Post Detection

This is a **Machine Learning-based Web Application** built using **Python** and **Flask** to detect fake job postings. The project uses an **SVM classifier** to classify job posts as genuine or fake based on their descriptions. The web app allows users to input a job description and get a result indicating whether the job post is genuine or fake.

## Features
- **Job Post Description Input**: Users can input a job description to check if it is genuine or fake.
- **Model**: The application uses an **SVM classifier** trained on job posting data to classify the descriptions.
- **Real-time Predictions**: Predictions are made on the fly based on the user's input.

## Project Structure

```plaintext
Fake-Job-Post-Detection/
├── app/
│   ├── templates/
│   │   ├── home.html       # HTML form to submit job descriptions
│   │   ├── result.html     # HTML page to show prediction results
│   ├── static/
│   │   ├── styles.css      # Custom CSS styles
│   ├── app.py              # Flask app backend
├── model/
│   ├── train_model.py      # Script to train the SVM model
│   ├── job_post_detector.pkl  # Trained model file
│   ├── vectorizer.pkl      # TF-IDF Vectorizer for job descriptions
├── data/
│   ├── fake_job_postings.csv  # Dataset of job posts
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
```

## Prerequisites

- Python 3.x
- pip (for installing dependencies)

## Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/username/Fake-Job-Post-Detection.git
   cd Fake-Job-Post-Detection
   ```

2. **Install required dependencies**:

   Install the necessary packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**:

   Before running the web application, you need to train the model using the dataset. Run the following command:

   ```bash
   python model/train_model.py
   ```

   This will train the SVM model using the `fake_job_postings.csv` dataset and save the trained model and vectorizer in the `model` directory.

4. **Start the Flask app**:

   Run the Flask application with the following command:

   ```bash
   python app/app.py
   ```

   The application will start on `http://127.0.0.1:5000/`.

5. **Access the web application**:

   Open your web browser and go to:

   ```plaintext
   http://127.0.0.1:5000/
   ```

   You can enter a job description in the input box, and the model will predict whether it is genuine or fake.

## Dataset

The dataset used for training the model is a CSV file containing job postings, including columns like `title`, `location`, `description`, and `fraudulent` (label: 1 for genuine, 0 for fake). You can find the dataset in the `data/fake_job_postings.csv` file.

## Files

- `app.py`: The backend Flask application that handles the user input and serves predictions.
- `train_model.py`: The script to train the model using the dataset.
- `fake_job_postings.csv`: The dataset containing job posts and labels.
- `job_post_detector.pkl`: The trained SVM model.
- `vectorizer.pkl`: The TF-IDF vectorizer used to convert job descriptions into numerical features.

## Technologies Used

- **Python**: Programming language for the backend and machine learning.
- **Flask**: A lightweight web framework for building the web application.
- **scikit-learn**: A library for machine learning used to train the SVM model.
- **pandas**: A library for data manipulation and analysis.
- **BeautifulSoup** and **requests**: Used for web scraping if needed.

## Future Enhancements

- Improve model accuracy by using more advanced NLP techniques such as **word embeddings** (e.g., GloVe, Word2Vec).
- Implement more advanced scraping capabilities to continuously update the dataset with new job postings.
- Add user authentication for personalized results.

