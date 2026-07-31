from sklearn.ensemble import IsolationForest

def detect(data):
    model = IsolationForest()
    model.fit(data)
    return model.predict(data)
