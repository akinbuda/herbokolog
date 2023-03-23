#Libraries
import discord
import openai
import os
import time

botsCommand="!chatbot" #you can change this.
spesificChannel= #your channel id. if you want to use bot in a spesific channel paste your channel id int type and go to line 25

botName="" #Your bot's name.
openai.api_key = "" #Your openai api key.
TOKEN = "" #Your Discord bot token.
model_engine = "text-davinci-002"
client = discord.Client(intents=discord.Intents.all())
prompt = f"Hi, i am {botName}. How can i help you?" 


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    splitted= message.content.split(" ")
    if splitted[0] == botsCommand: # for spesific channel change this line to = if splitted[0] == botsCommand and message.shannel.id == spesificChannel:
      if message.author == client.user:
          return
      else:
          user_input = message.content
          response = openai.Completion.create(
              engine=model_engine,
              prompt=prompt + "\nKullanıcı: " + user_input + "\nChatGPT:",
              temperature=0.7,
              max_tokens=1024,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
          )
          reply = response.choices[0].text.strip()           
          await message.channel.send(reply)
          new_prompt = prompt + "\nKullanıcı: " + user_input + "\nChatGPT: " + reply
          time.sleep(1)

client.run(TOKEN)
