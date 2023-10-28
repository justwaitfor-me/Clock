import fortnite_api, pytz, json, os, time, datetime, random, sys
from keepalive import keep_alive
from webhook import send_clock, send_valo, send_fortnite
from modules import *
from replit import db

db["days"] = 0
db["result"] = ""

with open("json/clock.json", "r") as file:
    # Load the JSON data into a Python object
    clock_data = json.load(file)
with open("json/fortnite.json", "r") as file:
    # Load the JSON data into a Python object
    fortnite_data = json.load(file)
with open("json/valorant.json", "r") as file:
    # Load the JSON data into a Python object
    valorant_data = json.load(file)


agenten = [
    "Gekko (InT)",
    "Harbor (Con)",
    "Fade (InT)",
    "Neon (DuL)",
    "PHOENIX (DuL)",
    "JETT (DuL)",
    "VIPER (Con)",
    "SOVA (InT)",
    "CYPHER (SenT)",
    "BRIMSTONE (Con)",
    "Sage (SenT)",
    "OMEN (Con)",
    "BREACH (InT)",
    "Raze (DuL)",
    "REYNA (DuL)",
    "KILLJOY (SenT)",
    "SKYE (InT)",
    "YORU (DuL)",
    "ASTRA (Con)",
    "KAY/O (InT)",
    "CHAMBER (SenT)",
    "Deadlock (SenT)"
]


api = fortnite_api.FortniteAPI(api_key=os.environ["fortnite_api"])
clock =  os.environ['clock']
valorant = os.environ['valorant']
fortnite = os.environ['fortnite']
home = os.environ['home']
clock_id = "1145763238848508088"
valo_id = "1145764081320611991"
fortnite_id = "1145764413933105252"
task = False
task_no = 0

def restart_script():
    python = sys.executable
    os.execv(python, [python] + sys.argv)

def get_clock():
    clock = ""
    bitcoin = ""
    tz = pytz.timezone('Europe/Berlin') # Zeitzone Berlin
    berlin_now = datetime.datetime.now(tz) # aktuelle Zeit in Berlin
    m = berlin_now.strftime("%M") # Minute
    h = berlin_now.strftime("%H") # Stunden

    h = clock_data["Clocks"][str(h)]
    h = h.replace(" ", "\n")
    h = h.replace("1", "⬜")
    h = h.replace("0", "⬛")
    h = split_variable(h)

    m = clock_data["Clocks"][str(m)]
    m = m.replace(" ", "\n")
    m = m.replace("1", "⬜")
    m = m.replace("0", "⬛")
    m = split_variable(m)

    for i in range(0, 5):
        hour = h[i]
        minute = m[i]
        if i == 0 or i == 4:
          clock += f"{hour} ⬛⬜⬛ {minute}\n"
        else:
          clock += f"{hour} ⬛⬛⬛ {minute}\n"
    
    day = berlin_now.strftime('%d')
    number = db["number"]
  
    fact = db["fun_facts"].replace("['", "").replace("']", "").replace('["', "").replace('"]', "")
    month = berlin_now.strftime('%m')
    year = berlin_now.strftime('%y')
    sec = berlin_now.strftime('%S')
    fullday = berlin_now.strftime("%A")
    bitcoin = str(btc())[:-5].replace(",", ".")
    return(f"**{fullday} {day}.{month}.20{year}**\n{clock}**Seconds: {sec}\n\n>>> BTC: {bitcoin}€\nTodays Number: {number}\n\nTodays Fact:\n{fact}**")

def get_db():
    tz = pytz.timezone('Europe/Berlin') # Zeitzone Berlin
    berlin_now = datetime.datetime.now(tz) # aktuelle Zeit in Berlin
    day = berlin_now.strftime('%d')
    days = db["days"]
    if int(day) != days:
      db["days"] =  int(day)
      db["mention"] = "<@&1145756815913660547>"
      db["number"] = random.randint(1000, 9999)
      db["agent"]  = str(random.choices(agenten))
      db["fact"] = str(random.choices(valorant_data["facts"]))
      db["maps"] = str(random.choices(valorant_data["maps"]))
      db["skins"] = str(random.choices(valorant_data["skins"]))
      db["fun_facts"] = str(random.choices(clock_data["fun_facts"]))
      db["pick"], db["data_result"] = guessing(valorant_data)
      db["fortnite_fact"] = str(random.choices(fortnite_data["facts"]))
      db["fortnite_maps"] = str(random.choices(fortnite_data["maps"]))
      db["fortnite_news"] = str(random.choices(api.news.fetch().raw_data["br"]["motds"]))
      db["fortnite_map"] = str(api.map.fetch().blank_image)
      db["fortnite_cosmetics"] = str(get_fortnite_cosmetics())
      db["fortnite_shop"] = str(get_fortnite_shop())
      
    else:
      db["mention"] = ""
      
def get_valo():
  tz = pytz.timezone('Europe/Berlin') # Zeitzone Berlin
  berlin_now = datetime.datetime.now(tz) # aktuelle Zeit in Berlin
  date = f"{berlin_now.strftime('%d')}.{berlin_now.strftime('%m')}.20{berlin_now.strftime('%y')}"
  pick = db["pick"]
  result = db["data_result"]
  skin = db["skins"].replace("['", "").replace("']", "").replace('["', "").replace('"]', "").replace('\n', " ").replace('\r', " ")
  fact = db["fact"].replace("['", "").replace("']", "").replace('["', "").replace('"]', "")
  agent = db["agent"].replace("['", "").replace("']", "").replace('["', "").replace('"]', "")
  map = db["maps"].replace("['", "").replace("']", "").replace('["', "").replace('"]', "")
  mention = db["mention"]
  return({"pick":pick, "result":result, "fact":fact, "agent":agent, "map":map, "skin":skin, "date":date, "mention":mention})

def get_fortnite():
  tz = pytz.timezone('Europe/Berlin') # Zeitzone Berlin
  berlin_now = datetime.datetime.now(tz) # aktuelle Zeit in Berlin
  date = f"{berlin_now.strftime('%d')}.{berlin_now.strftime('%m')}.20{berlin_now.strftime('%y')}"
  fact = db["fortnite_fact"].replace("['", "").replace("']", "").replace('["', "").replace('"]', "")
  maps = db["fortnite_maps"].replace("[[", "[").replace("]]", "]")
  news = db["fortnite_news"].replace("[[", "[").replace("]]", "]")
  map = db["fortnite_map"]
  mention = db["mention"]
  cosmetics = db["fortnite_cosmetics"].replace("['", "").replace("']", "").replace('["', "").replace('"]', "")
  shop = db["fortnite_shop"].replace("['", "").replace("']", "").replace('["', "").replace('"]', "")
  return({"fact":fact, "maps":maps, "date":date, "news":news, "map":map, "mention":mention, "cosmetics":cosmetics, "shop":shop})
  

for none in range(0, 2):
  print(f"task: for ({none})")
  while task_no < 500 and task == True:
    task_no += 1
    get_db()
    send_clock(get_clock())
    send_valo(get_valo())
    send_fortnite(get_fortnite())
    time.sleep(1)
  else:
    print(f"task: while false ({task_no}) ({task})")
    keep_alive()
    task = True

print(f"task: restart ({task_no}) ({task})")
restart_script()