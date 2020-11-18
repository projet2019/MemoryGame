import sys
from game import Game

def main(args=None):
  game = Game()
  game.play()

if __name__ == "__main__":
  sys.exit(main(sys.argv[1:]))


