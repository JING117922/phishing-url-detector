\# Phishing URL Detector



A simple machine learning demo for detecting phishing websites using classic ML algorithms (Logistic Regression \& Decision Tree) based on public dataset.



\## Project Structure



phishing-url-detector/

│

├── main.py                  # Main script for model training and evaluation  

├── data/                    # Folder to store dataset  

│   └── phishing\_site\_urls.csv  

├── images/                  # Visual assets (ROC curve, Confusion Matrix)  

│   ├── roc\_curve.png  

│   └── confusion\_matrix.png  

├── README.md                # Project description  



\## Features Used



\- URL Length  

\- Use of @ symbol  

\- Number of dots in domain  

\- Use of https  

\- Domain age  

\- ... and more!



\## How to Run



1\. Install dependencies:



&nbsp;  pip install pandas scikit-learn matplotlib



2\. Run the script:



&nbsp;  python main.py



\## Output Example



\- Accuracy: 94.2%  

\- AUC Score: 0.96  

\- Confusion Matrix and ROC Curve saved in `images/` folder



\## Screenshots



(Please upload these images to the images/ folder and they will show here on GitHub)



!\[ROC Curve](images/roc\_curve.png)  

!\[Confusion Matrix](images/confusion\_matrix.png)



\## Dataset Source



This project uses the "Phishing Website Detector" dataset from Kaggle:  

https://www.kaggle.com/datasets/sid321axn/phishing-website-detector



\## Motivation



This project is a hands-on practice for applying Machine Learning in Cybersecurity. It simulates a basic phishing URL classification scenario, inspired by real-world detection systems. It is part of a preparation portfolio for URV’s CSAI program (Cybersecurity \& AI).



\## To-Do (Optional)



\- Add Random Forest / XGBoost comparison  

\- Export model via joblib for reuse  

\- Try with TfidfVectorizer on raw URLs (NLP-based)

