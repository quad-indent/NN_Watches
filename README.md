# NN_Watches

This program utilises machine learning to help to predict whether a customer of certain age and income is likely to purchase a watch based on past purchasing habits of other customers.

## It includes two modules:
- A sequential neural network model (**MLer_NN.py** and **MLer_NN_trained.py**) which has managed to beat the accuracy of an initially implemented decision tree model, scoring **0.94** (comparedto **0.82**)
- The module **MLer_NN.py** includes methods for preprocessing the data, constructing, and training the model. It also allows for saving the model and the scaler, as well as playing around with the resulting model
- The module **MLer_NN_trained.py** is adapted for the actual user and seeks to load the trained model and scaler and offers error handling as well as more easily-readable output

The scaler, the trained model folder, and the Customers.csv dataset should be placed in the same directory as the programs in order to work
