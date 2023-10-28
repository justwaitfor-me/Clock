def update_clock_msg(url, clock_id, new_content):
  clock = f"{url}/messages/{clock_id}"
  data = {
      "content": new_content
  }
  headers = {
      "Content-Type": "application/json"
  }
  response = requests.patch(clock, data=json.dumps(data), headers=headers)
  if response.status_code != 200:
      print("Failed to update webhook message.")

def update_fortnite_msg(url, fortnite_id, new_content):
  fact = new_content['fact']
  fortnite = f"{url}/messages/{fortnite_id}"
  date = new_content['date']
  news = ast.literal_eval(new_content['news'])[0]
  maps = ast.literal_eval(new_content['maps'])
  map = new_content['map']
  mention = new_content['mention']
  cosmetics = ast.literal_eval(new_content['cosmetics'])
  shop = ast.literal_eval(new_content['shop'])

  data = {
      "content": f"{mention}",
      'embeds': [
          {
              'title': 'Fortnite News',
              'description': date,
              'color': 65535,  # Blue color
              'author': {
                  'name': 'daily dose of fortnite',
                  'url': 'https://store.epicgames.com/de/p/fortnite',
                  'icon_url': 'https://static.wikia.nocookie.net/logopedia/images/d/db/Fortnite_S1.svg/revision/latest/scale-to-width-down/150?cb=20210330161743'
              },
              'fields': [
                  {
                      'name': f'Todays Map:',
                      'value': f"Name: {maps[0]}\nMap Code: _{maps[1]}\nCreator: {maps[2]}_",
                      'inline': False
                  },
                  {
                      'name': 'Random Fact:',
                      'value': f"_{fact}_",
                      'inline': False
                  },
                  {
                      'name': 'Random Cosmetic:',
                      'value': f"*{cosmetics['name']} ({cosmetics['type']})*\n{cosmetics['description']}\nRarity:{cosmetics['rarity']}",
                      'inline': False
                  },
                  {
                    'name': 'News:',
                    'value': f"*{news['title']}*\n_{news['body']}_",
                    'inline': False
                  }
              ],
              'footer': {
                  'text': 'made by justwait'
              },
              'thumbnail': {'url':'https://static.wikia.nocookie.net/logopedia/images/d/db/Fortnite_S1.svg/revision/latest/scale-to-width-down/150?cb=20210330161743'
              },
              'image': {
                  'url': news["tileImage"]
              }
          }
      ]
  }
  headers = {
      "Content-Type": "application/json"
  }
  response = requests.patch(fortnite, data=json.dumps(data), headers=headers)
  if response.status_code != 200:
      print("Failed to update webhook message. Fortnite")

def update_valo_msg(url, valo_id, new_content):
  pick = new_content['pick']
  result = new_content['result']
  fact = new_content['fact']
  agent = new_content['agent']
  map = new_content['map']
  valo = f"{url}/messages/{valo_id}"
  img = clock_data["valorant"]["agenten"][agent]
  skin = new_content['skin']
  date = new_content['date']
  mention = new_content['mention']
  data = {
      "content": f"{mention}",
      'embeds': [
          {
              'title': 'Valorant News',
              'description': date,
              'color': 16711680,  # Red color
              'author': {
                  'name': 'daily dose of valorant',
                  'url': 'https://playvalorant.com/',
                  'icon_url': 'https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png'
              },
              'fields': [
                  {
                      'name': 'Todays Agent:',
                      'value': f"_{agent}_",
                      'inline': True
                  },
                  {
                      'name': 'Todays Map:',
                      'value': f"_{map}_",
                      'inline': False
                  },
                  {
                      'name': 'Random Fact:',
                      'value': f"_{fact}_",
                      'inline': False
                  },
                  {
                      'name': 'Random Skin:',
                      'value': f"_{skin}_",
                      'inline': False
                  },
                  {
                      'name': 'Todays ability:',
                      'value': f">>> _{pick}_\n\n_Answer: ||{result}||_",
                      'inline': False
                  }
              ],
              'footer': {
                  'text': 'made by justwait'
              },
              'thumbnail': {
                  'url': 'https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png'
              },
              'image': {
                  'url': img
              }
          }
      ]
  }
  headers = {
      "Content-Type": "application/json"
  }
  response = requests.patch(valo, data=json.dumps(data), headers=headers)
  if response.status_code != 200:
      print("Failed to update webhook message. Valo")