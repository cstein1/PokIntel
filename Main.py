
from Game import Game
from Model import *
import numpy as np

def main():
    # Hand Model Training
    # game = Game()
    # model = BasicModel(3, 128, 52)
    # model.build()
    # model.printModel()
    # print("Playing Rounds")
    # inp, out = game.playRounds(50000)
    # print("Training")
    # model.model.fit(inp, out, validation_split=0.2, steps_per_epoch=64, epochs=16, validation_steps=64)
    # model.model.save_weights('poker.h5')
    # #model.model.load_weights('poker.h5')
    # #pair
    # hand = np.zeros(52)
    # hand[10] = 1
    # hand[23] = 1
    # hand[11] = 1
    # hand[24] = 1
    # hand[5] = 1
    # print(model.predict(hand))


    # Discard Model Training
    # game = Game()
    # model = DiscardModel(2,256,52)
    # model.build()
    # model.printModel()
    # print("Playing Rounds")
    # # inp, out = game.playDiscards(10000)
    # # np.save('out.npy', out)
    # # np.save('inp.npy', inp)
    # inp = np.load('inp_10k.npy')
    # out = np.load('out_10k.npy')
    # model.model.fit(inp, out, validation_split=0.1, steps_per_epoch=64, epochs=4, validation_steps=64)
    # #[0., 0., 0., 1., 0.]
    # print(model.predict(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0,
    #     0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
    #     0, 0, 0, 0, 0, 0, 0, 0])))
    # #[1., 0., 1., 1., 1.]
    # print(model.predict(np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1,
    #     0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
    #     0, 0, 0, 0, 0, 0, 0, 0])))
    # model.model.save_weights('discard.h5')

    game = Game()
    model = DiscardModel(2,256,52)
    model.build()
    model.model.load_weights('discard.h5')
    game.playDiscardAgainstRandom(model, 1000)


if __name__ == "__main__":
    main()
