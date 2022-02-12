
from random import randint
import random
import discord
from coinDB import dataBase, dbTool
import re

class CommandSystem:
    def __init__(self,prefix):
        self.prefix = prefix

def checkCommand(message,command):
    if message.startswith(command):
        return True
    else:
        return False

async def runCommand(message,user,channel,mentions,bot):
    if checkCommand(message,"help"):
        coinCount = dataBase.get(user.id,"coin")
        embed = discord.Embed(title="功能說明",
            description=f"發訊息有機率獲得錢錢\n\n-coin```查看自己有多少錢```-pay <目標> <金額>```匯款給別人```-rank```查看土豪排行榜```"
        )
        await channel.send(embed=embed)

    if checkCommand(message,"pay"):
        if len(mentions) != 1:
            embed = discord.Embed(title="匯款系統",description=f"請輸入一個匯款目標")
            await channel.send(embed=embed)
            return
        target = mentions[0]
        args = message.split(" ")
        price = args[len(args)-1]
        if not price.isdigit():
            embed = discord.Embed(title="匯款系統",description=f"請輸入正確的匯款金額")
            await channel.send(embed=embed)
            return
        else:
            price = int(price)
        coinCount = dataBase.get(user.id,"coin")
        if coinCount < price:
            embed = discord.Embed(title="匯款系統",description=f"金幣不足！")
            await channel.send(embed=embed)
            return
        embed = discord.Embed(title="匯款系統",description=f"<@!{user.id}> 匯款了 **{price}** :dollar: 給 <@!{target.id}>")
        dataBase.add( user.id,"coin", -price )
        dataBase.add( target.id,"coin", price )
        await channel.send(embed=embed)
        return

    if checkCommand(message,"coin"):
        coinCount = dataBase.get(user.id,"coin")
        embed = discord.Embed(title="金幣查詢",description=f"你的資產：**{coinCount}** :dollar:")
        await channel.send(embed=embed)

    if checkCommand(message,"mining"):
        coinCount = dataBase.get(user.id,"coin")
        gems = random.randint(0,3)
        embed = discord.Embed(title="挖礦系統",description=f"你挖到了 **{gems}** :gem:")
        await channel.send(embed=embed)

    if checkCommand(message,"gamble"):
        args = message.split(" ")
        price = args[len(args)-1]
        if not price.isdigit():
            embed = discord.Embed(title="賭博",description=f"請輸入正確的下注金額")
            await channel.send(embed=embed)
            return
        else:
            price = int(price)
        coinPrice = randint(0,20)/10
        pow = randint(0,20)/10
        result = round(price*pow*coinPrice)
        coinCount = dataBase.get(user.id,"coin")
        if coinCount < price:
            embed = discord.Embed(title="匯款系統",description=f"金幣不足！")
            await channel.send(embed=embed)
            return

        dataBase.add(user.id,"coin",-price)
        dataBase.add(user.id,"coin",result)

        embed = discord.Embed(title="賭博系統",description=f"```本局賭注：{price}\n返回金額：{coinPrice}\n本局倍率：{pow}```\n【賭局結果】\n你獲得 **{result}** :dollar:")
        await channel.send(embed=embed)

    if checkCommand(message,"rank"):
        # coinCount = dataBase.get(user.id,"coin")

        rank = dbTool.get()
        rank = dict(sorted(rank.items(), key=lambda item: item[1]["coin"], reverse=True))
        
        result = ""
        emoji = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten"
            ]

        for i in rank:
            members = await bot.fetch_user(int(i))
            index = list(rank.keys()).index(i)
            result += f":{emoji[index]}: {members.name}：擁有 **{rank[i]['coin']}** :dollar:\n\n"
            if index == 10:
                break

        embed = discord.Embed(title="土豪排行榜",description=result)
        await channel.send(embed=embed)
    