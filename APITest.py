import requests
import json

url = "https://official-joke-api.appspot.com/random_joke"
def main():
    choice = input("Enter Movie or Joke \n")
    if choice == "Movie":
        Movie()
    if choice == "Joke":
        Joke(url)


def Movie():
    moviename = input("Enter movie name for search \n")
    response = requests.get('http://www.omdbapi.com/?apikey=f3950e24&t='+ moviename)
    resDict = json.loads(response.text)    
    for i in (resDict):
        print(i, ": ", resDict[i])


def Joke(url):
    jokeAmount = input("How many jokes you want?")
    for i in range(0, int(jokeAmount)):
        data = requests.get(url)
        tt = json.loads(data.text)
        print(tt["setup"])
        print(tt["punchline"], "\n")

if __name__ == "__main__":
    main()