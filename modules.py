import random, requests, json, os

def guessing(data):
  agentenx = [
    "Gekko (InT)",
    "Harbor (Con)",
    "Fade (InT)",
    "Neon (DuL)",
    "PHOENIX (DuL)",
    "CHAMBER (SenT)",
    "KAY/O (InT)",
    "ASTRA (Con)",
    "YORU (DuL)",
    "SKYE (InT)"
  ]
  guessing = data["guessing"]
  agent = str(random.choice(agentenx))
  agent_data = guessing[agent]
  data = random.choice(agent_data["Data"])
  pick = agent_data[data]
  result = f"{agent}, {data}"
  return pick, result

def btc():
  response = requests.get(os.environ['coin_api'])
  data = response.json()
  return data["bpi"]["EUR"]["rate"]

def split_variable(string):
    lines = string.split("\n")
    return lines

def get_fortnite_shop():
  url = 'https://fortnite-api.com/v2/shop/br'
  return_list = []
  response = requests.get(url)
  if response.status_code == 200:
    data = (json.loads(response.text)["data"]["featured"]["entries"])
    for i in data:
      data = i["items"][0]
      type = data["type"]["displayValue"]
      name = data["name"]
      rarity = data["rarity"]["displayValue"]
      description = data["description"]
      images = data["images"]
      return_list.append({"name":name,"description":description,"type":type,"rarity":rarity,"images":images})
    return return_list
  else:
      return('Error:', response.status_code)

def get_fortnite_cosmetics():
  url = 'https://fortnite-api.com/v2/cosmetics/br/new'
  response = requests.get(url)
  if response.status_code == 200:
    data = (random.choices(json.loads(response.text)["data"]["items"])[0])
    type = data["type"]["displayValue"]
    name = data["name"]
    rarity = data["rarity"]["displayValue"]
    description = data["description"]
    images = data["images"]
    return({"name":name,"description":description,"type":type,"rarity":rarity,"images":images})
  else:
    return('Error:', response.status_code)