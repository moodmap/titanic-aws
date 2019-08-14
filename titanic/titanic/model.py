import pickle
from sklearn.ensemble import RandomForestClassifier

def predict(x):
    filename = 'titanic_model.sav'
    randomforest = pickle.load(open(filename, 'rb'))
    result = randomforest.predict(x)
    if result == 0:
        result = 'Not survived'
    elif result == 1:
        result = 'Survived'
    else:
        result = 'Error'
    return result
