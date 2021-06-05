import discord
from riotwatcher import LolWatcher, ApiError
api_key = 'your api key'
watcher = LolWatcher(api_key)
my_region = 'kr'

class MyClient(discord.Client):
    async def on_ready(self):
        print('실행중')

    async def on_message(self, message):
        if message.content.startswith("!검색"): # 만약, 채팅이 "!도움말"로 >>시작<< 한다면,
            value = message.content.replace('!검색', '')
            me = watcher.summoner.by_name(my_region, value)
            t = me['name']
            c = me['summonerLevel']
            await message.channel.send("이름 : " + t + ", Lv." + c)
                
client = MyClient()
client.run('your token')