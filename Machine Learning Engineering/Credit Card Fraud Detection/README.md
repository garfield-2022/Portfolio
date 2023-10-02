The importance of Credit Card Fraud Detection can not be over stated. For example, the Federal Trade Commision Sentinel Report(https://tinyurl.com/2dpae443) 
shows that Credit Card Fraud Detetion is the most Identity Theft Type in 2023. Credit Card Fraud Detection can help maintain account security and reduce the 
chances of credit card fraud. It can also save a significant amount of money that would traditionally be lost to fraud. 

This is a Kaggle project (https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). The dataset contains transactions made by credit cards in September 2013 by European cardholders. The dataset is highly unbalanced, where there are 492 frauds out of 284,807 transactions. Due to confidentiality issues, 28 of the original features have been transformed by PCA to be numerical input variables. The 'Time' and 'Amount' features are not transformed. Feature 'Time' contains the seconds elapsed between each transation and the first transaction in the dataset. Feature 'Amount' is the transaction amount. Feature 'Class' is the response variable and it takes value 1 in case of fraud and 0 otherwise.

The project comprises the following files:

1. data-analysis.ipynb. 28 of 31 features are decomposed by PCA. No missing values in dataset. Amount distribution by class, as well as data points distribution by time, are explored. 
2. building-models-statsmodels-scikit-learn.ipynb. P-values indicate that all the features are statistically significant. Logistic regression is chosen as the classificiation algorithm. But the same procedure can be applied to other classification algorithms. SMOTE is adopted to deal with imbalanced dataset. Evaluation metrics include balanced accuracy score, f1 score, auc score, precision-recall curve.
3. MLflow-scikit-learn.ipynb. MLflow experiments are created. Parameters, Metrics and Artifacts are logged. This part of deployment is built for CI/CD.
4. MLflow-deploy-localhost.ipynb: batch querying and making predictions one batch at a time on local host. MLflow-deploy-VM-GCP: on Google Cloud platform, storage bucket, virtual machine instance as well as firewall rules are created. Now the model is deployed on GCP and accessed through external IP address. VM instance on GCP: steps to achieve GCP deployment. 
5. model.py. Logistic Regression model is dumped into model.pkl by pickle for building web application use.
6. app.py. Deploy the model to a web application using Flask. CSS and HTML templates are also provided. Prediction can be obtained by inputing variables on the webpage.
7. api.py. A Flask app is built with Swagger. Two types of predictions, single transaction and group transactions, are made. The app is also run using Docker. All the steps are included in Dockerfile.txt, from which we build the Docker image and run the container. 
8. Kubernetes Engine on GCP. Steps to achieve deployment on GCP Kubernetes Engine.
9. Wrap-up and Improvement. A brief wrap-up of the project and areas where improvements can be made are shown.

Main references:
1. An Introduction to Statistical Learning with Applications in Python by Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani and Jonathan Taylor.
2. Deploy Machine Learning Models to Production -- With Flask, Streamlit, Docker, and Kubernetes on Google Cloud Platform by Pramod Singh;
3. Beginning MLOps with MLFlow -- Deploy Models in AWS SageMaker, Google Cloud, and Microsoft Azure by Sridhar Alla and Suman Kalyan Adari;
4. Credit Card Fraud Detection in Python -- Learn how to build a model that is able to detect fraudulent credit card transactions with high accuracy, recall and F1 score using Scikit-learn in Python, "https://thepythoncode.com/article/credit-card-fraud-detection-using-sklearn-in-python".
5. Credit Fraud || Dealing with Imbalanced Datasets, "https://www.kaggle.com/code/janiobachmann/credit-fraud-dealing-with-imbalanced-datasets";
6. Project 10. Credit Card Fraud Detection using Machine Learning in Python | Machine Learning Projects, "https://www.youtube.com/watch?v=NCgjcHLFNDg";
