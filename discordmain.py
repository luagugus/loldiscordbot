import discord
from riotwatcher import LolWatcher, ApiError
api_key = 'your api key'
watcher = LolWatcher(api_key)
my_region = 'kr'

class MyClient(discord.Client):
    async def on_ready(self):
        print('실행중')

    async def on_message(self, message):
        if message.content.startswith("!검색"):
            value = message.content.replace('!검색', '')
            me = watcher.summoner.by_name(my_region, value)
            t = me['name']
            c = me['summonerLevel']
            embed=discord.Embed(title="전적", description="전적입니다.", color=0x00aaaa)
            embed.set_author(name="LOL BOT",icon_url=message.author.avatar_url)
            embed.add_field(name="level", value=t, inline=False)
            embed.add_field(name="name", value=c, inline=False)
            embed.set_footer(text="togugu")
            await message.channel.send(embed=embed)
                
client = MyClient()
client.run('your token')