from random import *
import playsound

moves = ['rock', 'paper', 'scissor']

class RockPaperScissor:
	def __init__(self):
		self.playerScore = 0
		self.botScore = 0
		self.total_moves = 0

	def nextMove(self, move):
		botMove = randint(0,2)
		try:
			playerMove = int(moves.index(move))
		except Exception as e:
			print("Invalid Move! Try Again")
			return

		print('Bot:', moves[botMove])
		self.total_moves += 1

		if botMove==playerMove:
			self.botScore += 1
			self.playerScore += 1
			return
		elif botMove==0:
			if playerMove==1:
				self.playerScore += 1
			else:
				self.botScore += 1
		elif botMove==1:
			if playerMove==2:
				self.playerScore += 1
			else:
				self.botScore += 1
		else:
			if playerMove==0:
				self.playerScore += 1
			else:
				self.botScore += 1

	def whoWon(self):
		result = ""
		if self.playerScore == self.botScore:
			result = "The match is draw !\n"
		elif self.playerScore > self.botScore:
			result = "You won the match Sir! Well Done !\n"
		else:
			result = "You lose the match Sir! Haha!\n"
		result += "You won " +str(self.playerScore)+"/"+str(self.total_moves)+" matches."
		return result

class LuckyTrivia:
	def __init__(self):
		self.totalScore = 0

	def nextQuestion(self, ques, options, correct):
		print("\nQ:", ques)
		for i in range(len(options)):
			print(i+1,options[i])
		
		try:
			ans = int(input("Ans: "))
			if ans==correct:
				print("You're Right!")
				playsound.playsound('extrafiles/wow.mp3')
				self.totalScore += 1
			else:
				playsound.playsound('extrafiles/suspense.mp3')	
				print("You're Wrong!")
				print("Correct Answer: ", options[correct-1])
		except Exception as e:
			print("e")

	def showResult(self):
		return "Your Total Score is " + str(self.totalScore)

def isContain(text, lst):
	for word in lst:
		if word in text:
			return True
	return False

def play(gameName):
	if isContain(gameName, ['dice','die']):
		result = "You got " + str(randint(1,6))
		return result

	elif isContain(gameName, ['coin']):
		playsound.playsound('extrafiles/Coin Drop Test.mp3')
		p = randint(-10,10)
		if p>0: return "You got Head"
		else: return "You got Tail"

	elif isContain(gameName, ['rock','paper','scissor','first']):
		n = int(input("How many matches you want to play? "))
		r = RockPaperScissor()
		for i in range(n):
			move = input('Your Move: ')
			r.nextMove(move)
			print()
		result = r.whoWon()
		return result

	elif isContain(gameName, ['lucky','trivia','second']):
		l = LuckyTrivia()
		with open("extrafiles/lucky.txt", "r") as file:
			for line in file:
				line = line.strip().split(';')
				l.nextQuestion(line[0],list(line[1:-1]), int(line[-1]))
		result = l.showResult()
		return result
	else:
		print("Game Not Available")


def showGames():
	print("----------------")
	print("Available Games")
	print("----------------")

	print("Rock Paper Scissor\nLucky Trivia\n\n")
