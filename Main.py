
from Game import Game
from Model import BasicModel
import numpy as np

def main():
    game = Game()
    model = BasicModel(3, 128, 52)
    model.build()
    model.printModel()
    print("Playing Rounds")
    inp, out = game.playRounds(50000)
    print("Training")
    model.model.fit(inp, out, validation_split=0.2, steps_per_epoch=64, epochs=16, validation_steps=64)
    model.model.save_weights('poker.h5')
    #model.model.load_weights('poker.h5')
    #pair
    hand = np.zeros(52)
    hand[10] = 1
    hand[23] = 1
    hand[11] = 1
    hand[24] = 1
    hand[5] = 1
    print(model.predict(hand))

if __name__ == "__main__":
    main()
