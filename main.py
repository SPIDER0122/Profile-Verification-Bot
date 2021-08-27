import discord
import asyncio

client = discord.Client()
token = "bot token"

@client.event
async def on_ready():
    print("Login")

@client.event
async def on_message(message):
    if message.content.startswith("!프로필"): #!프로필 @맨션 을 하시면 맨션당한사람에 프로필이 나옵니다
        target = message.mentions[0]
        embed = discord.Embed(title=f"다운로드", colour=0x00ff00, url=target.avatar_url)
        embed.set_image(url=target.avatar_url)
        embed.set_footer(text=f"{target.name}님의 프로필")
        await message.channel.send(embed=embed)

client.run(token)