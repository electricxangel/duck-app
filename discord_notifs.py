import discord
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

embed = discord.Embed()


class unnamed_duck_bot(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.All())

    async def on_ready(self):
        print("ready")


bot = unnamed_duck_bot()

while True:
    will_dm = input("shall i dm?")
    if will_dm == "yes":
        async def message(member: discord.Member):
            member.name = "heeheebiki"
            await member.send("hello world")



unnamed_duck_bot.run(bot, token=DISCORD_TOKEN)

