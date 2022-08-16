# the bot was made in diskord.py 1.7.3
import CONFIG
import discord
from discord.ext import tasks
from datetime import datetime

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@tasks.loop(seconds=CONFIG.UPDATE_TIME)
async def mainLoop():
    try:
        for guild in client.guilds:
            for member in guild.members:
                if member and member.activity and member.activity.name:
                    for i in range(len(CONFIG.BANNED_GAMES)):
                        if (member.activity.name.lower() == CONFIG.BANNED_GAMES[i].lower()) and ((datetime.utcnow() - member.activity.start).total_seconds() > CONFIG.BAN_TIME):
                            await member.send(CONFIG.BAN_MESSAGES[i])
                            await member.ban(delete_message_days=0, reason=CONFIG.BAN_REASONS[i])
    except exception as e:
        print("Error", e)

mainLoop.start()
client.run(CONFIG.TOKEN)
