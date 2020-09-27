import wikipedia
import webbrowser
import requests
from bs4 import BeautifulSoup

def google(search):
	result = requests.get('https://www.google.com/search?q='+''.join(search))
	# print(result.status_code)
	# print(result.headers)
	src = result.text
	# print(src)
	soup = BeautifulSoup(src, 'html.parser')
	links = soup.select('a')
	linkToOpen = min(5, len(links))
	for i in range(linkToOpen):
		webbrowser.open('https://google.com'+links[i].get('href'))


def whiteHouse():
	result = requests.get('https://www.whitehouse.gov/briefings-statements/')
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')
	urls = []
	for h2_tag in soup.find_all('h2'):
		a_tag = h2_tag.find('a')
		urls.append(a_tag.attrs['href'])

	for link in urls:
		print(link)


def wikiResult(query):
	query = query.replace('wikipedia','')
	query = query.replace('search','')
	if len(query.split())==0: query = "wikipedia"
	try:
		return wikipedia.summary(query, sentences=2)
	except Exception as e:
		return "Desired Result Not Found"

def weather():
	URL = 'https://weather.com/en-IN/weather/today/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	city = ""
	for h in soup.find_all('h1'):
		city = h.text
		city = city.replace('Weather','')
		city = "Weather of " + city + " is "
		break

	spans = soup.find_all('span')
	
	for span in spans:
		try:
			if span['data-testid']=="TemperatureValue":
				return city + span.text+' Celcius.'
		except Exception as e:
			pass

	return "Not Available Sir"


def latestNews(news=5):
	URL = 'https://indianexpress.com/latest-news/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	headlineLinks = []
	headlines = []

	divs = soup.find_all('div', {'class':'title'})

	count=0
	for div in divs:
		count += 1
		if count>news:
			break
		a_tag = div.find('a')
		headlineLinks.append(a_tag.attrs['href'])
		headlines.append(a_tag.text)

	# for i in range(len(headlines)):
		# print(headlines[i])
		# print(headlineLinks[i])
		# print()

	return headlines,headlineLinks

def openWebsite(url='https://www.google.com/'):
	webbrowser.open(url)
	return "You can now read the full news from this website."

def jokes():
	URL = 'https://icanhazdadjoke.com/'
	result = requests.get(URL)
	src = result.content

	soup = BeautifulSoup(src, 'html.parser')

	try:
		p = soup.find('p')
		return p.text
	except Exception as e:
		raise e


def youtube(query):
	from youtube_search import YoutubeSearch
	query = query.replace('play',' ')
	query = query.replace('on youtube',' ')
	query = query.replace('youtube',' ')
	results = YoutubeSearch(query,max_results=1).to_dict()
	webbrowser.open('https://www.youtube.com/watch?v=' + results[0]['id'])
	return "Enjoy Sir..."