ai_name = 'jarvis'
ai_name = ai_name.lower()

'''User Created Modules'''
try:
	import game
	import normalChat
	import appControl
	import webScrapping
	import math_function
except Exception as e:
	raise e

'''System Modules'''
try:
	import speech_recognition as sr
	import pyttsx3
	import playsound
	from time import sleep
except Exception as e:
	print(e)

try:
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('voice', voices[1].id) #male
	engine.setProperty('volume', 1)
except Exception as e:
	print(e)

def speak(text):
	print('\n'+ai_name.upper()+': '+text)
	engine.say(text)
	engine.runAndWait()

def record():
	print('\nListening...')
	r = sr.Recognizer()
	r.dynamic_energy_threshold = False
	r.energy_threshold = 4000
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
		# audio = r.listen(source,timeout=4,phrase_time_limit=4)
		said = ""
		try:
			said = r.recognize_google(audio)
			print(f"\nUser said: {said}")
		except Exception as e:
			print(e)
			speak("I didn't get it, Say that again please...")
			return "None"
	
	return said.lower()

def isContain(txt, lst):
	for word in lst:
		if word in txt:
			return True
	return False


"""Main Tasks"""
def main():
	while True:
		text = record()
		if isContain(text, ['youtube','video']):
			speak('Ok Sir, here a video for you...')
			speak(webScrapping.youtube(text))
			continue

		if isContain(text, ['math','calculation','+','-']):
			speak('Ok Sir, Ask me')
			try:
				text = record()
				speak('Result is: ' + math_function.perform(text))
			except Exception as e:
				continue
			continue

		if "joke" in text:
			speak('Here is a joke...')
			speak(webScrapping.jokes())
			continue
			
		if isContain(text, ['news']):
			speak('Getting the latest news...')
			headlines,headlineLinks = webScrapping.latestNews(2)
			for head in headlines: speak(head)
			speak('Do you want to read the full news?')
			text = record()
			if isContain(text, ["no","don't"]):
				speak('No Problem Sir')
			else:
				speak('Ok Sir, Opening browser...')
				speak(webScrapping.openWebsite('https://indianexpress.com/latest-news/'))
			continue

		if isContain(text, ['weather']):
			speak(webScrapping.weather())
			continue

		if isContain(text, ['screenshot']):
			appControl.Win_Opt('screenshot')
			speak("Screen Shot Taken")
			continue

		if isContain(text, ['window']):
			appControl.Win_Opt(text)
			continue

		if isContain(text, ['tab']):
			appControl.Tab_Opt(text)
			continue

		if isContain(text, ['wiki']):
			speak('Searching Wikipedia...')
			speak(webScrapping.wikiResult(text))
			continue

		if isContain(text, ['bye','exit','quit','shutdown']):
			speak('Shutting down the System. Good Bye Sir !')
			raise SystemExit #sys.exit
		
		if isContain(text, ['voice']):
			try:
				if 'female' in text:
					engine.setProperty('voice', voices[0].id)
					speak("Hello Sir, I'm Zira, your Assistant. How may I help you?")
				else:
					engine.setProperty('voice', voices[1].id)
					speak("Hello Sir, I'm David, your Assistant. How may I help you?")
			except Exception as e:
				pass
			continue
		
		if isContain(text, ['game']):
			game.showGames()
			speak("Which game do you want to play?")
			text = record()
			if isContain(text, ["don't", "no", "cancel", "back", "never"]):
				speak("No Problem Sir, We'll play next time.")
			else:
				speak("Ok Sir, Let's Play " + text)
				result = game.play(text)
				speak(result)
			continue
		
		if isContain(text, ['hello','good','how are you','hai','morning','evening','noon']):
			if isContain(text, ["good"]):
				speak(normalChat.chat("good"))
				continue
			speak('Hello Sir, How are you ?')
			text = record()
			speak(normalChat.chat("fine"))
			continue
		
				
		if isContain(text, ['coin','dice','toss','roll','die']):
			speak("Ok Sir")
			speak(game.play(text))
			continue
		
		if isContain(text, ['time','date','day','today','month']):
			speak(normalChat.chat(text))
			continue

		if text != "None":
			speak("Do you want me to search this ?")
			text = record()
			if isContain(text, ["don't","no","dont search"]):
				speak("No Problem Sir")
			else:
				speak("Sorry Sir, This feature is not available yet !")

"""AI Activation"""
if __name__ == '__main__':
	while True:
		text = record()
		if isContain(text, ['hello','hi','hey',ai_name,'hai','activate','google']):
			speak(normalChat.wishMe() + " Sir. Please give a moment till I setup the environment.")
			# speak("Checking the requirements")
			# speak("Initializing Updates")
			speak("Everything is looking fine Sir. I'm ready to take commands. Just tell me and I will perform the task for you.")
			break
		else:
			continue
	main()


'''
1. jaise he mai aau, to apne aap wish karega(meri photo dekh ke)
2. agr dusra aadmi aaya to uska photo click krke uski details puchega and save krke agli baar usko ussi se wish krega
3. jarvis bolega tab bolne ka animation  
'''