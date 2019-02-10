# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 23:10:15 2018
Machine learning logistic regression in python with an example
@author: SHASHANK
"""

# Importing the libraries
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

class Model:
    X = None
    Y = None
    standardScaler = None
   
    # Importing the dataset
    def importData(self):
        dataset = pd.read_csv('supermall.csv')
        self.X = dataset.iloc[:, [2,3]].values
        self.Y = dataset.iloc[:, 4].values

    # Applying feature scaling on the train data
    def doFatureScaling(self):
        self.standardScaler = StandardScaler()
        self.X = self.standardScaler.fit_transform(self.X)

    def isBuying(self):
        self.importData()
        self.doFatureScaling()
        
        # Fitting the Simple Linear Regression to the Training set
        classifier = LogisticRegression(random_state = 0)
        classifier.fit(self.X, self.Y)    
        
        userAge = float(raw_input("Enter the user's age? "))
        userSalary = float(raw_input("What is the salary of user? "))
        
        # Applying feature scaling on the test data
        testData = self.standardScaler.transform([[userAge, userSalary]])    
        prediction = classifier.predict(testData)
        
        print 'This user is most likely to buy the product' if  prediction[0] == 1 else 'This user is not gonna buy the your product.'

model = Model()
model.isBuying()
