#https://www.youtube.com/watch?v=SPTfmiYiuok
#https://replit.com/join/mbhhonnfko-nathaliecuartas

#1 - create bot (https://discord.com/developers/applications)
  #Name: Test1 Bot
 
#2
import discord

client = discord.Client()

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startwith('$hello'):
		await message.channel.send('Hello!')
		
#insert token (use environment variable)
#use sidebar for environmental variable
client.run()
