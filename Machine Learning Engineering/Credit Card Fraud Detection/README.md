The importance of Credit Card Fraud Detection can not be over stated. For example, the Federal Trade Commision Sentinel Report(https://tinyurl.com/2dpae443) shows that Credit Card Fraud Detetion is the most Identity Theft Type in 2023. Credit Card Fraud Detection can help maintain account security and reduce the chances of credit card fraud. It can also save a significant amount of money that would traditionally be lost to fraud. 

This is a Kaggle project (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). The dataset contains transactions made by credit cards in September 2013 by European cardholders. The dataset is highly unbalanced, where there are 492 frauds out of 284,807 transactions. Due to confidentiality issues, 28 of the original features have been transformed by PCA to be numerical input variables. The 'Time' and 'Amount' features are not transformed. Feature 'Time' contains the seconds elapsed between each transation and the first transaction in the dataset. Feature 'Amount' is the transaction amount. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

This folder comprises the following files:
1. data-analysis. 28 of 31 features are decomposed by PCA. No missing values in dataset. Amount distribution by class, as well as data points distribution by time, are explored. 
2. model building scikit-learn
3. MLflow
4. batch deployment on local host
5. web deployment

Main references:
1. Project 10. Credit Card Fraud Detection using Machine Learning in Python | Machine Learning Projects, "https://www.youtube.com/watch?v=NCgjcHLFNDg";
2. Credit Fraud || Dealing with Imbalanced Datasets, "https://www.kaggle.com/code/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets";
3. Beginning MLOps with MLFlow -- Deploy Models in AWS SageMaker, Google Cloud, and Microsoft Azure by Sridhar Alla and Suman Kalyan Adari;
4. Deploy Machine Learning Models to Production -- With Flask, Streamlit, Docker, and Kubernetes on Google Cloud Platform by Pramod Singh;
5. Credit Card Fraud Detection in Python -- Learn how to build a model that is able to detect fraudulent credit card transactions with high accuracy, recall and F1 score using Scikit-learn in Python, "https://thepythoncode.com/article/credit-card-fraud-detection-using-sklearn-in-python".
