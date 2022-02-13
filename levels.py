from MccDB import dataBase
import discord
from imger.image import download_image, level_imger

async def addExp(member,channel,user):
    await dataBase.add(member,"exp",1)
    exp = await dataBase.get(member,"exp")
    level = await dataBase.get(member,"level")

    if not level:
        level = 1

    if exp >= level*5:
        level += 1
        exp = 0
        gift = level*75
        await dataBase.add(member,"coin",gift)
        img = user.avatar_url
        download_image(img)
        level_imger(user.name,level)
        await channel.send(f"<@!{member}> 獲得升級獎勵 {gift} :dollar:",file=discord.File("./imger/image.png"))

    await dataBase.set(member,"level",level)
    await dataBase.set(member,"exp",exp)
