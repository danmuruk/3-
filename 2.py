import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswith("!도움말"):
        await message.channel.send("현재 삼뚝이는 명령어를 지원하지 않습니다. 이후 버전에 업데이트 될 예정입니다.")
    if message.content.startswith("!명령어"):
        await message.channel.send("현재 삼뚝이는 명령어를 지원하지 않습니다. 이후 버전에 업데이트 될 예정입니다.")


client.run("NzE1MzM1NjM0NzA4ODU2ODgz.Xs7uaA.thbh15XwsN0Ko2zZZ0XQ4GVk-tg")