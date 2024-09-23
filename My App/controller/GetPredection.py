def GetPredection(model, inputs: list):

    result = {
        0:"setosa",
        1:"versicolor",
        2:"virginica"}

    predections = model.predict([inputs])[0]

    return result[predections]
