from MccDB import dataBase
import discord
import botFunctions
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


client.run("OTQxNzE0OTU3NTY3OTQyNzM2.YgZ-Zg._z91Kj-XTpmT0UhxogS59TBISl4")