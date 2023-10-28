from discord_webhook import DiscordWebhook, DiscordEmbed
import os, ast

def send_valo(valorant_data, data, webhook_id="1145764081320611991"):
  pick = data['pick']
  result = data['result']
  fact = data['fact']
  agent = data['agent']
  map = data['map']
  image = valorant_data["agenten"][agent] #ändern zu data
  skin = data['skin']
  date = data['date']
  mention = data['mention']
  
  webhook_valo = DiscordWebhook(url=os.environ['valorant'], id=webhook_id, content=mention)
  
  embed = DiscordEmbed(title="Valorant News", description=date, color="16711680")
  embed.set_author(
    name="daily dose of valorant", 
    url="https://playvalorant.com/", 
    icon_url="https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png"
  )

  # set image
  embed.set_image(url=image)
  embed.set_thumbnail(url="https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png")

  # set footer
  embed.set_footer(text="made by justwait")
  embed.set_timestamp()

  # add fields to embed
  embed.add_embed_field(name="Todays Agent:", value=f"_{agent}_", inline=False)
  embed.add_embed_field(name="Todays Map:", value=f"_{map}_", inline=False)
  embed.add_embed_field(name="Random Fact:", value=f"_{fact}_", inline=False)
  embed.add_embed_field(name="Random Skin:", value=f"_{skin}_", inline=False)
  embed.add_embed_field(name="Todays ability:", value=f">>> _{pick}_\n\n_Answer: ||{result}||_", inline=False)

  # add embed object to webhook
  webhook.add_embed(embed)
  response_valo = webhook_valo.execute()
  
  
def send_fortnite(data, webhook_id="1145764413933105252"):
  fact = data['fact']
  date = data['date']
  news = ast.literal_eval(data['news'])[0]
  maps = ast.literal_eval(data['maps'])
  map = data['map']
  mention = data['mention']
  cosmetics = ast.literal_eval(data['cosmetics'])
  shop = ast.literal_eval(data['shop'])
  
  webhook_fortnite = DiscordWebhook(url=os.environ['fortnite'], id=webhook_id, content=mention)
  
  embed = DiscordEmbed(title="Fortnite News", description=date, color="65535")
  embed.set_author(
    name="daily dose of fortnite", 
    url="https://store.epicgames.com/de/p/fortnite", 
    icon_url="https://static.wikia.nocookie.net/logopedia/images/d/db/Fortnite_S1.svg/revision/latest/scale-to-width-down/150?cb=20210330161743"
  )

  # set image
  embed.set_image(url=news["tileImage"])
  embed.set_thumbnail(url="https://static.wikia.nocookie.net/logopedia/images/d/db/Fortnite_S1.svg/revision/latest/scale-to-width-down/150?cb=20210330161743")

  # set footer
  embed.set_footer(text="made by justwait")
  embed.set_timestamp()

  # add fields to embed
  embed.add_embed_field(
    name="Todays Map:", 
    value=f"Name: {maps[0]}\nMap Code: _{maps[1]}\nCreator: {maps[2]}_", 
    inline=False
  )
  embed.add_embed_field(
    name="Random Fact:", 
    value=f"_{fact}_", 
    inline=False
  )
  embed.add_embed_field(
    name="Random Cosmetic:", 
    value=f"*{cosmetics['name']} ({cosmetics['type']})*\n{cosmetics['description']}\nRarity:{cosmetics['rarity']}", 
    inline=False
  )
  embed.add_embed_field(
    name="News:", 
    value=f"*{news['title']}*\n_{news['body']}_", 
    inline=False
  )

  # add embed object to webhook
  webhook.add_embed(embed)
  response_fortnite = webhook_fortnite.execute()
  

def send_clock(data, webhook_id="1145763238848508088"):
  webhook_clock = DiscordWebhook(url=os.environ['clock'], id=webhook_id, content=data)
  response_clock = webhook_clock.execute()

