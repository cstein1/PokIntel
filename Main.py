
from Game import Game
from Model import BasicModel

def main():
    game = Game()
    model = BasicModel(1, 128, 52)
    model.build()
    model.printModel()
    print("Playing Rounds")
    inp, out = game.playRounds(20000)
    print("Training")
    model.model.fit(inp, out, validation_split=0.2, steps_per_epoch=64, epochs=8, validation_steps=64)

if __name__ == "__main__":
    main()
