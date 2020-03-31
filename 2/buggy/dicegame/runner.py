from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            #total += 1
	    #print die.value
	    total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
	runner1 = cls()
	while True:
            runner = cls()

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner1.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner1.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner1.wins, runner1.loses))
            runner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = raw_input("Would you like to play again?[Y/n]: ")

           # if prompt == 'y' or prompt == '':
  	    print prompt
	  
            if prompt == 'Y' or prompt == 'y':
                continue
            else:
		print 'No more playing!'
		break
              #  i_just_throw_an_exception()
