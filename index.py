import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


def scrapeTextFromWebPage(url):
    response = requests.get(url)

    parseHtmlContent = BeautifulSoup(response.content, "html.parser")

    return parseHtmlContent.get_text()


def getTextFromFile(file_path):
    with open(file_path, "r") as file:
        text = file.read()

    return text


def generateWordCloud(text):
    stopwords = set(STOPWORDS)

    wordcloud = WordCloud(stopwords=stopwords,
                          background_color="white").generate(text)

    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()


webPage = int(input('Enter web page URL:'))

text = scrapeTextFromWebPage(webPage)

generateWordCloud(text)
