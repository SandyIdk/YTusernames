import itertools
import requests
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
words = []
available = []

for length in range(1,6):
  for combinations in itertools.permutations(letters,length):
    words.append("".join(combination))
 

def check_name(name)
  url = "https://www.googleapis.com/youtube/v3/channels"
  params = {
    "part": "id",
    "forUsername": name
  }
  response = requests.get(url,params=params)
  
  if response.status_code == 200:
    return True
  else:
    return False

for i in range(words):
  available(i) = check_name(words(i))

