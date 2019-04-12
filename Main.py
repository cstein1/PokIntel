
from Game import Game

def main():
    a = Game()
    for hand in a.players.values():
        print(str(hand))

if __name__ == "__main__":
    main()
