## Introduction
Sentiment Analysis on Twitter Data . Classifying them based on polarity into positive, negative and neutral Using Classical Machine Learning methods.
This project is a part of **IIT-K Machine Learning and Data Science Internship (2020)**


## Aim of Project

This project addresses the problem of sentiment analysis on twitter data. The goal of our project is to build a sentiment analysis model on the given data. Our main area of focus is on the **Classical Machine Learning methods**. 

## Authors

* [**Varshini P J**](https://github.com/Varshinipj)
* [**Dharineesh Karthikeyan**](https://github.com/Dharineesh-Karthikeyan)

## Project Report
The project report is a detailed analysis report of our project. It has the details of the performance of different models we used, consists of the the details about the data cleaning, analysis,word embeddings used, model selection, hyper parameter tuning and grid search and additional features we added to the model to improve the performance.

Click [here](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/Project_Report.pdf) to read the report !!

## How to run the project
This is a basic explanation of the functionalities of each folder, and purpose of each of the python files.
The order of execution, for the sake of simplicity we named the python files with the according number.

**Python files:**\
   Order of Execution and Functionality:
   1. [Data Cleaning.ipynb](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/1_Data_Cleaning.ipynb):
       * Cleans the data and creates new csv files containing clean data.
   2. [Data Analysis.ipynb](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/2_Data_Analysis.ipynb):
       * Analysing the data and providing study results.
   3. [Model Selection.ipynb](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/3_Model%20Selection.ipynb):
       * To compare different models and select the best.
   4. [Hyperparameter tuning.ipynb](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/4_Hyperparameter%20tuning.ipynb):
       * Hyperparameter tuning of the selected models.
   5. [Detector.py](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/5_Detector.py):
       * Contains classes for Emoticon and Word Detection. (Imported to other files)
   6. [Additional Features.ipynb](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/6_Additional_Features.ipynb):
       * Extracts additional features and creates new csv files containing Additional Features.
   7. [Final Model.ipynb](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/7_Final%20Model.ipynb):
       * The final code to predict the outputs

**Folders:**
   * [Data](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/tree/master/Data):\
     Contains all the datasets and files used in the codes. They contain the following:
     * given datasets - train.txt , test_samples.txt
     * cleaned datasets (From Data_Cleaning.ipynb) - train_clean_data.csv, test_clean_data.csv
     * added features datasets ( From Additional Features.ipynb) - train_added_features.csv , test_added_features.csv
     * list of emoticons and words - emoticons.txt, words.txt
	
	
   * [Plots](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/tree/master/Plots):\
     Contains a png of every graph or representation used in the codes.


**Submission file:**\
[submission.csv](https://github.com/Dharineesh-Karthikeyan/nlp-tweet-sentiment-analysis/blob/master/submission.csv) is the final submitted file on kaggle


## Kaggle In-class Competition

As metioned before, this project was a part of the IIT-K Machine Learning and Data Science Internship (2020).
The link to the [kaggle competition](https://www.kaggle.com/c/sentiment-analysis-of-tweets)
* Our team name was "Project Code" and we placed 5th in the kaggle competition with a public score of **0.71051** and a private score of **0.71018**.


## Acknowledgments

* All acknowledgments are mentioned in the end page of the report 


