
__NLP Project for Disaster Tweet Classification__

Disaster Tweet Classification project aims to predict whether a given tweet is related to a disaster or not using machine learning. The trained model is then deployed as a web application using Flask, allowing users to input tweets and receive real time predictions.

__Prerequisites__

Before running the project, we need to ensure that we have the following dependencies installed:
Python (version 3.6 or higher)
Flask (pip install Flask)
Sklearn (pip install scikit-learn)
Pandas (pip install pandas)
numpy (pip install numpy)
regression and classification models (as per the dataset)
TF-IDF Vectorizer or CountVectorizer
Wordcloud etc.

__Project Structure__

The project is structured as follows:

|--app/

| |--static/ 

| | |--wordcloud.png

| |--templates/

| | |--base.html

| | |--dashboard.html

| | |--error.html

| | |--prediction.html

| | |--wordcloud.html

| |--app.py

| |--requests.py

| |--requirements.txt

| |--mylogisticmodel.joblib

| |--vectorizer.joblib

|--flask dashboard for twitter disaster.pdf

|--final_df_for_dashboard.csv


|--Project Solution Task 1.ipynb

|--Project Solution Task 2.ipynb

|--Project Solution Task 3.ipynb


|--README.md

|--Twitter Disaster.pdf

__Training the Model__

4 models have been trained..Random Forest Classifier, Logistic Regression, Support Vector and Neural Network but Logistic Regression Model has the highest accuracy. So this model only has been used for making Flask Dashboard.

__Running the Web App__

Navigate to the app/directory and it can be run by running the app.py(python file) by giving the command __flask run__

This is the link for [Twitter Dashboard](http://127.0.0.1:5000/)





