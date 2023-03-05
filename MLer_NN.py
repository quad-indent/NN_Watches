import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras import models
from keras import layers
from keras import optimizers
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from pickle import dump


__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def prepareData(filename='Customers.csv'):
    df = pd.read_csv(os.path.join(__location__, "Customers.csv"))
    df.reset_index(drop=True, inplace=True)

    X = df[['Age', 'Salary']]
    Y = df['Purchased']

    scaler = MinMaxScaler()
    X = scaler.fit_transform(X.values)

    X, X_dev, Y, Y_dev = train_test_split(X, Y, train_size=0.9)

    return X, X_dev, Y, Y_dev, scaler

def buildModel():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(2,)))
    model.add(layers.Dropout(0.1))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(8, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    return model

def main():
    X, X_dev, Y, Y_dev, scaler = prepareData()
    
    model = buildModel()
    model.compile(optimizer=optimizers.Adam(learning_rate=0.0001), loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X, Y, epochs=15, batch_size=1, validation_data=(X_dev, Y_dev), verbose=1)

    print(model.evaluate(X_dev, Y_dev))

    shouldSave = input("Save model? (1/0): ")
    if shouldSave == "1":
        model.save(os.path.join(__location__, "trainedModel"))
        dump(scaler, open(os.path.join(__location__, "scaler"), 'wb'))
        
    
    while(True):
        age = int(input("Age: "))
        if (age == 1):
            model.save(os.path.join(__location__, "trainedModel"))
            dump(scaler, open(os.path.join(__location__, "scaler"), 'wb'))
        salary = int(input("Salary: "))
        print(model.predict(scaler.transform([[age, salary]])))

if __name__ == "__main__":
    main()