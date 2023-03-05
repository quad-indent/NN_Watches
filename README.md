# WatchAndLearn

This program utilises machine learning to help to predict whether a customer of certain age and income is likely to purchase a watch based on past purchasing habits of other customers.

## It includes three modules:
- A decision tree model (**MLer.py**) which seems very suitable for the task, as the data is quite limited and there are only two labels. It reaches the accuracy of around **0.82**
- A sequential neural network model (**MLer_NN.py** and **MLer_NN_trained.py**) which has still managed to beat the accuracy of the decision tree model, scoring **0.94**
- The module **MLer_NN.py** includes methods for preprocessing the data, constructing, and training the model. It also allows for saving the model and the scaler, as well as playing around with the resulting model
- The module **MLer_NN_trained.py** is adapted for the actual user and seeks to load the trained model and scaler and offers error handling as well as more easily-readable output

The scaler, the trained model folder, and the Customers.csv dataset should be placed in the same directory as the programs in order to work
