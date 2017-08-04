import discord
import dicerolls
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('!roll '):
        print(message, message.content)
        msg = dicerolls.roll(message.content[6:])

        await client.send_message(message.channel, "<@!" + message.author.id + ">:\n" + msg)

client.run(os.environ('DISCORD_BOT_TOKEN'))