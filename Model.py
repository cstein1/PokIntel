import keras
from keras import Model
from keras.layers import Dense, Input
import numpy as np

class BasicModel:
    def __init__(self, numLayers: int, layerWidth: int, inputSize: int):
        self.numLayers = numLayers
        self.layerWidth = layerWidth
        self.inputSize = inputSize
        self.model = None

    def build(self):
        inp = Input(shape=[self.inputSize,])
        x = Dense(self.layerWidth, activation='relu')(inp)
        for num in range(1, self.numLayers):
            x = Dense(self.layerWidth, activation='relu')(x)
        out = Dense(1, activation='sigmoid')(x)

        self.model = Model(inp, out)
        self.model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    def printModel(self):
        if self.model == None:
            print("Not built")
        else:
            print(self.model.summary())

    #deals with reshaping for single or multiple inputs
    def predict(self, inp):
        if len(inp.shape) == 1:
            return self.model.predict(np.array(inp).reshape(1,-1))[0]
        else:
            return self.model.predict(np.array(inp))
