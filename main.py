import random
from coinDB import dataBase
import discord
import botFunctions
from commands import CommandSystem,runCommand

client = discord.Client()
CommandSys = CommandSystem("-")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith(CommandSys.prefix):
        await runCommand(
            message.content[1:len(message.content)],
            message.author,
            message.channel,
            message.mentions,
            client
        )
    else:
        dataBase.add(message.author.id,"coin",1)
    
client.run("OTQxNzE0OTU3NTY3OTQyNzM2.YgZ-Zg.e-Dt1Vi63QrJHKvE9fQBRypmUf4")