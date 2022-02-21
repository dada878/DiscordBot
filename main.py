from MccDB import dataBase
import discord
import levels
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
        await levels.addExp(message.author.id,message.channel,message.author)


client.run("token") #請填入自己的token