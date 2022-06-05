# -*- coding: utf-8 -*-

# ライブラリのインポート
import discord
import asyncio

TOKEN = 'OTgyMjExNjI5ODI1NTMxOTU0.GCnnrg.UfQTF_0Ph0dvXPVWBF_xq3PHZvPLSXNVKJpJDY'
client = discord.Client()

# ボットの起動時に実行されるイベントハンドラを定義
@client.event
async def on_ready():
    print('Bot Launched')

# メッセージの送信時に実行されるイベントハンドラを定義
@client.event
async def on_message(message):
    if message.author.bot:
        pass
    elif message.content.startswith('$heybot'):
        send_message = f'{message.author.mention}さん、こんにちは！ https://github.com/kinieko/ss.git'
        await message.channel.send(send_message)

#ボットを実行
client.run(TOKEN)
#ここより下に書かれた処理はボットが停止するまで実行されない
    

