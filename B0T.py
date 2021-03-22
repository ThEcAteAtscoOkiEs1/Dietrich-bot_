import discord
import asyncio
import random

client = discord.Client()

token ="ODIzMTc5ODA4NjM1NjE3MzMw.YFdD8A.D_CsUX-4LpZoWUa8WSCI_HuL1n0"

@client.event
async def on_ready():

    print(client.user.name)
    print("그래그래 봇 실행 됐다 일마야")
    game = discord.Game("ChilL And diScO")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "시발":
        await message.channel.send("욕 쓰지마 ㅠㅠㅠ")

    if message.content =="오늘의 솔랭 운세":
        ran = random.randint(0,1)
        if ran == 0:
            d = "연승"
        if ran == 1:
            d = "연패 병신 ㅋ"
        await message.channel.send(d)


client.run(token)