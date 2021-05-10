import os
import discord

my_secret = os.environ['TOKEN']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('hello')

client = MyClient()
client.run(my_secret)
