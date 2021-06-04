# Diabetes Prediction
[Website of our project](https://checkyourdiabetes.herokuapp.com/)

![Image](https://github.com/Shobhitthebeginner/DiabetesWithDjango/blob/master/static/img/diabetes1.jpg)


Our objective is to predict whether an individual have diabetes or not using machine learning algorithms.
A large dataset is considered and this predictor is modelled to analyse the diabetes possiblity of a person through different parameters like Glucose,BloodPressure,
Skin Thickness,Insulin etc.
All these parameters will be analysed through Machine Learning algorithms which will helps us to predict whether person is diabetic or not. 
Output obtained would further be checked for correctness and model will be optimized accordingly. 
We have to create a beautiful interface for interaction between the user and our ML model which is done through the Django framework.


## Dataset Description

We have taken our datasets from UCI Machine learning Repository. 
This diabetes dataset is from AIM'94
There are total 768 number of instances and 8 attributes which are as follows:-
1. Body Mass Index
2. Insulin
3. Skin Thickness 
4. Blood Pressure 
5. Age
6. Pregnancies 
7. Diabetes Pedigree Function
8. Outcome

## Technology Used
1. Python programming Language
2. Advanced Python libraries:

       a. Pandas      
       b. matplotlib      
       c. numpy      
       d. scikit-learn
      
3. Machine Learning Algorithms 
4. Django Framework
5. HTML
6. CSS

## Methodology

We have followed a step by step procedure for the analysis of our dataset. We have undertaken the following steps while performing data analysis:

1. Data Pre-Processing
2. Data Visualization
3. Applying Machine Learning Algorithms
4. Building an Interface using Django

## Results 

Accuracy from Decision Tree Classifier is 70.00 %

Accuracy from RandomForestClassifier is 76.43 %

Accuracy from Logistic Regression is 79.76 %

Accuracy from Gradient Boosting Algorithm is 82.89 %

Accuracy from XGBoost Classifier is 79.43 %

Accuracy from Naive Bayes is 74.36 %

Accuracy from K-Nearest Neighbours is 78.06 %

Accuracy from Support Vector Machine algorithm is 70.36 %

## Conclusion
The Dataset consist of 8 attributes. One (Outcome) is dependent variable and the others are predictors. The experiments show that the value of the dependent variable can be predicted more accurately if only important features are considered in prediction rather than considering all features.
In this work, machine learning techniques are used to determine wheter a person has diabetes or not. We have analysed that there are some variables which have a strong effect on our output variables and they are: Insulin, BMI, Age and Blood Pressure. After applying all the Machine Learning Algorithms, we have realised that Gradient Boosting Algorithm gives the best result in terms of accuracy of 82.89 %.

## Developers
Shwetank Dixit

Shobhit Mishra
