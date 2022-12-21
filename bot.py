import discord
import requests
import json
import random
client = discord.Client()


def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + "-" + json_data[0]['a']
  return(quote)
  

def get_joke():
  response = requests.get("https://v2.jokeapi.dev/joke/Programming,Miscellaneous,Dark,Pun,Spooky,Christmas?blacklistFlags=religious&type=twopart")
  json_data = json.loads(response.text)
  setup = json_data["setup"]
  punchline = json_data["delivery"]
  return (setup,punchline)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_ready1():
  await client.change_presence(activity = discord.Activity(type=discord.ActivityType.Listening, name='w.[location]'))
   


@client.event
async def on_message(message):
  username = str(message.author).split('#')[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f'{username}:{user_message} ({channel})')

  if message.author == client.user:
    return
  
  if message.content.startswith('&hello'):
    await message.channel.send('Hey!')
    
  if message.content.startswith('&inspire'):
    quote=get_quote()
    await message.channel.send(quote)

  if message.content.startswith('&joke'):
    joke = get_joke()
    await message.channel.send(joke)
  
  if message.content== '&alone':
    await message.author.send('HELLO, HEARD YOU ARE ALONE SO LETS HAVE FUN TOGETHER!')
  
  
  if message.content.startswith('hi'):
     await message.channel.send(f'Hello,{username}!')
     return
  if user_message.lower()=='bye':
    await  message.channel.send(f'See you later, {username}!')
    return
  if user_message.lower()=='!random':
    response = f'This is your random number:{random.randrange(1000000)}'
    await message.channel.send(response)
    return
  
client.run('MTA1NTIwNTU0MDc5NzYyODQ4Ng.GiqJ3H.gbvob-N-ZlanKmRy3wzpO1i4OzLUDeJjpFRpLM')
 