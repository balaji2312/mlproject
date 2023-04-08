# Student Mark Prediction

This ML Model will predict the Maths mark of a student based on students data.

I have solved this problem by using `Regression Analysis`

Dataset Source Link : <a href="https://www.kaggle.com/datasets/whenamancodes/students-performance-in-exams" target="_blank">Student Mark Prediction (Kaggle Data set)</a>

The dataset consist of 7 independent variables:

 *  **Gender**(`Category`) : Gender of the Student (*'M','F'*)
 * **Group**(`Category`): To which subject Group they belong (*'A','B','C','D'*)
 * **parental_level_of_education** (`Category`) : Qualification of the parents of those students(*'some college','high school' etc.,*)
 * **lunch** (`Category`) : Flag field. It will say wheather Student taken lunch or not before going to exam.
 * **test_preparation_course** (`Category`) : Student has completed all the mandatory course or not before exams.
 * **Reading_Score** (`Int`) : Students mark in Oral Test.
 * **Writing_Score** (`Int`) : Student mark in writting Test.

Target Variable:

* **Maths_Score**(`Int`) : Student mark in Maths subject.



### AWS Deployment Link :

Deployed the ML model in AWS Elastic BeanStalk :  http://studentmarkprediction-env.eba-m3gjw3ms.us-east-1.elasticbeanstalk.com/predictdata

### Screen Shot of UI :

![Screen Shot of UI.](Images/Student%20Mark%20Prediction%20UI_Page.png)

### Methodology:


#### Data Ingestion:
*  Utilized the Raw dataset present in the Kaggle and Split those data into train and test datasets and store the files under the artifacts folder.
* This act as a main file from where we will call all the other `.py` files.
#### Data Transformation:
* Some of the Feature Engineering and Scalling techniques has been used in this file.
* Used some of the techniques like *Simple Imputer, One Hot Encoding,Standard Scaler* during Preprocessing.
#### Model Trainer:
* Splited the train and test datasets and validated with different model along with Hyperparameter tuning.
* calculated `r2_Score` for all the validated model and which one has better score taken that model into consideration.
* Stored the best model in the pikle file.
#### Predict Pipeline:
 * This pipeline converts given data into dataframe and has various functions to load pickle files and predict the final results in python
#### Flask App:
  * Flask app is created with User Interface to predict the Student Maths Mark inside a Web Application.

### Exploratory Data Analysis Notebook :

Link : <a href="notebook/EDA STUDENT PERFORMANCE.ipynb" target="_blank">EDA Notebook</a>
