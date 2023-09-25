import requests
import json

apikey = "https://official-joke-api.appspot.com/random_ten"
def main():
    choice = input("Movie or Joke")
    if choice == "Movie":
        Movie()
    if choice == "Joke":
        Joke(apikey)


def Movie():
    moviename = input("enter name 4 serch")
    response = requests.get('http://www.omdbapi.com/?apikey=f3950e24&t='+ moviename)
    print(response.text)


def Joke(apikey):

    a = Joke(apikey)
    data = requests.get(apikey)
    tt = json.loads(data.text)
    for i in (a):
        print(i["setup"])
        print(i["punchline"], "\n")
    return tt

if __name__ == "__main__":
    main()