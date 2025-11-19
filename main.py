import discord
import requests
from discord.ext import commands
import json
from colorama import Fore as color
import os  # <-- IMPORTANT for Railway variables

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
bot.remove_command("help")

print(color.LIGHTGREEN_EX + "Coded by muha - guns.lol/muha")
print(color.YELLOW + r"""
███████╗████████╗ █████╗ ██████╗ 
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
███████╗   ██║   ███████║██████╔╝
╚════██║   ██║   ██╔══██║██╔══██╗
███████║   ██║   ██║  ██║██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
""")

# -------------------------------
# READ VARIABLES FROM RAILWAY
# -------------------------------
TOKEN = os.getenv("token")        # <-- Railway variable
ID = int(os.getenv("your_id"))    # <-- Railway variable

print(color.RESET + "[~] Do !help to get all commands")

@bot.event
async def on_ready():
    print(color.GREEN + f"[~] Logged in as {bot.user}")

@bot.event
async def on_command_error(ctx, error):
    print(color.RED + f"[!] Command error: {error}")

@bot.command()
async def help(ctx):
    if ctx.author.id == ID:
        embed = discord.Embed(
            title="⭐ STAR MENU",
            description=(
                "**__COMMANDS__**\n"
                "```\n"
                "nicknames <text>\n"
                "dm <text>\n"
                "```"
            ),
            color=0xa072d9
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1440791147432640655/1440794009709576252/liv4b.jpg?ex=691f737c&is=691e21fc&hm=6b6458e79d7b1d29320f2d304ce1517e5df2eb56a2f0cf2cae08e8fe035a062f")
        embed.set_footer(text="Prefix: ! ! made by muha")
        await ctx.send(embed=embed)
    else:
        print(color.RED + f"[!] {ctx.author.name} tried running help command")

@bot.command()
@commands.guild_only()
async def nicknames(ctx, *, arg):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for member in ctx.guild.members:
            try:
                await member.edit(nick=arg)
            except:
                print(color.RED + f"[!] Failed to change nickname of {member}")
        await msg.add_reaction("✅")

@bot.command()
@commands.guild_only()
async def dm(ctx, *, arg):
    if ctx.author.id == ID:
        msg = ctx.message
        await msg.add_reaction("🔄")
        for member in ctx.guild.members:
            try:
                await member.send(arg)
            except:
                print(color.RED + f"[!] Failed to DM {member}")
        await msg.add_reaction("✅")


bot.run(TOKEN)
