# filters.py (Python)

import discord
from discord.ext import commands

class Filters(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        # Implement filter logic here to detect and delete inappropriate content
        if "bad_word" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

def setup(client):
    client.add_cog(Filters(client))