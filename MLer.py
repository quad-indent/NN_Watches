import os
import numpy as np
import pandas as pd
from sklearn import tree

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def prepareData(filename='Customers.csv'):
    df = pd.read_csv(os.path.join(__location__, "Customers.csv"))
    df.reset_index(drop=True, inplace=True)

    X = df[['Age', 'Salary']]
    Y = df['Purchased']

    return X, Y

def prepareModel(X, Y):
    """Very rudimentary model, seeing as there's only two features to train and the amount of data is pretty small"""

    """
    X = X[:int(len(df) * 0.8)]
    Y = Y[:int(len(df) * 0.8)]

    X_dev = df[['Age', 'Salary']]
    Y_dev = df['Purchased']
    X_dev = X_dev[int(len(df) * 0.8):]
    Y_dev = Y_dev[int(len(df) * 0.8):]
    """
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(X.values, Y.values)

    """
    print(classifier.score(X_dev, Y_dev))
    When splitting the data into training and development sets, the accuracy of the model is 0.82, though a somewhat lightweight NN model achieves over 0.9 at times
    """
    return classifier

def predictor(model):
    while(True):
        age, salary = 0, 0
        print("Please enter data for prediction. Enter 'q' to quit")
        while(True):
            tempie = input("Age: ")
            if tempie == "q":
                return
            elif tempie.isnumeric():
                if int(tempie) >= 0:
                    """Maybe it's a millionaire newborn!"""
                    age = int(tempie)
                    break
        while(True):
            tempie = input("Salary: ")
            if tempie == "q":
                return
            elif tempie.isnumeric():
                if int(tempie) >= 0:
                    salary = int(tempie)
                    break
        scorer = "" if model.predict([[age, salary]])[0] == 1 else "not "
        print(f"┎{'─' * len(str(scorer))}──────────────────────────────────────────┒")
        print(f"| This customer is {scorer}likely to buy the watch |")
        print(f"└{'─' * len(str(scorer))}──────────────────────────────────────────┘")

def main():
    X, Y = prepareData()
    classifier = prepareModel(X, Y)

    predictor(classifier)

if __name__ == "__main__":
    main()