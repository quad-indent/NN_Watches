import os
from tensorflow import keras
from sklearn.preprocessing import MinMaxScaler
from pickle import load

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def predictor(model, scaler):
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
        scorer = round(model.predict(scaler.transform([[age, salary]]), verbose=0)[0][0] * 100, 2)
        print(f"┎{'─' * len(str(scorer))}────────────────────────────────────────────┒")
        print(f"| Predicted {scorer}% chance of purchasing the watch |")
        print(f"└{'─' * len(str(scorer))}────────────────────────────────────────────┘")

def main():
    model, scaler = None, None
    try:
        model = keras.models.load_model(os.path.join(__location__, "trainedModel"))
        print("Model loaded")
    except:
        print("Critical error! Could not load model!")
        return
    try:
        scaler = load(open(os.path.join(__location__, "scaler"), 'rb'))
        print("Scaler loaded")
    except:
        print("Critical error! Could not load scaler!")
        return
    predictor(model, scaler)
    return

if __name__ == "__main__":
    main()