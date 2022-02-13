
from random import randint
import random
import discord
from MccDB import  dataBase,dbTool
import datetime
import requests

from imger.image import level_imger

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
        coinCount = await dataBase.get(user.id,"coin")
        embed = discord.Embed(title="功能說明",
            description=f"發訊息可以增加經驗值\n當經驗值達標時將會升級\n\n-info```查看自己的持有物與資料```\n-pay <目標> <金額>```匯款給別人```\n-signin```每日簽到```\n-rank```查看土豪排行榜```\n-mining```挖礦```\n-sell <數量>```賣出寶石```\n-gamble <下注金額>```賭博(?)```"
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
        coinCount = await dataBase.get(user.id,"coin")
        if coinCount < price:
            embed = discord.Embed(title="匯款系統",description=f"金幣不足！")
            await channel.send(embed=embed)
            return
        embed = discord.Embed(title="匯款系統",description=f"<@!{user.id}> 匯款了 **{price}** :dollar: 給 <@!{target.id}>")
        await dataBase.add( user.id,"coin", -price )
        await dataBase.add( target.id,"coin", price )
        await channel.send(embed=embed)
        return

    if checkCommand(message,"info"):
        coinCount = await dataBase.get(user.id,"coin")
        diamondCount = await dataBase.get(user.id,"diamond")
        level = await dataBase.get(user.id,"level")
        if (not level):
            level = 1
            await dataBase.set(user.id,"level",level)
        exp = await dataBase.get(user.id,"exp")
        embed = discord.Embed(title="資料查詢",description=f"你的資產：**{coinCount}** :dollar:\n你的鑽石：**{diamondCount}** :gem:\n你的等級： **{level}({exp}/{level*5})**")
        await channel.send(embed=embed)

    if checkCommand(message,"mining"):
        print("開始挖礦")
        gems = random.randint(0,5)
        embed = discord.Embed(title="挖礦系統",description=f"你挖到了 **{gems}** :gem:")
        print("輸出中")
        await channel.send(embed=embed)
        print("輸出完畢")
        await dataBase.add(user.id,"diamond",gems)

    if checkCommand(message,"sell"):
        args = message.split(" ")
        count = args[len(args)-1]
        if not count.isdigit():
            embed = discord.Embed(title="出售寶石",description=f"請輸入正確的出售數量")
            await channel.send(embed=embed)
            return
        else:
            count = int(count)
            if (count > await dataBase.get(user.id,"diamond")):
                count = await dataBase.get(user.id,"diamond")
        price = random.randint(1,5)
        embed = discord.Embed(title="出售寶石",description=f"```寶石價格：{price}\n賣出數量：{count}```\n獲得 **{count*price}** :dollar:")
        await dataBase.add(user.id,"coin",count*price)
        await dataBase.add(user.id,"diamond",-count)
        await channel.send(embed=embed)


    if checkCommand(message,"signin"):
        today = datetime.datetime.now().day
        if (await dataBase.get(user.id,"signin") != today):
            embed = discord.Embed(title="簽到系統",description=f"簽到成功！\n獲得 **100** :dollar:")
            await dataBase.add(user.id,"coin",100)
            await dataBase.set(user.id,"signin",today)
        else:
            embed = discord.Embed(title="簽到系統",description=f"你已經簽到過了")
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
        coinCount = await dataBase.get(user.id,"coin")
        if coinCount < price:
            embed = discord.Embed(title="匯款系統",description=f"金幣不足！")
            await channel.send(embed=embed)
            return

        await dataBase.add(user.id,"coin",-price)
        await dataBase.add(user.id,"coin",result)

        embed = discord.Embed(title="賭博系統",description=f"```本局賭注：{price}\n返回金額：{coinPrice}\n本局倍率：{pow}```\n【賭局結果】\n你獲得 **{result}** :dollar:")
        await channel.send(embed=embed)

    if checkCommand(message,"rank"):
        # coinCount = await dataBase.get(user.id,"coin")

        rank = dbTool.get()

        for i in rank:
            await dataBase.get(i,"coin")

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
            "keycap_ten"
            ]

        for i in rank:
            index = list(rank.keys()).index(i)
            if index <= 9:
                members = await bot.fetch_user(int(i))
                result += f":{emoji[index]}: {members.name}：擁有 **{rank[i]['coin']}** :dollar:\n\n"
            else:
                id = int(i)
                if user.id == id:
                    result += f"```>> 你排在第 {index+1} 名```"
                    break

        embed = discord.Embed(title="土豪排行榜",description=result)
        await channel.send(embed=embed)
    