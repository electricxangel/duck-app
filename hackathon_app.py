import discord



class unnamed_duck_bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.All())
        self.synced = False