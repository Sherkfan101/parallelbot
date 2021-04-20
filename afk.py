import discord
from discord.ext import commands
import json

class Afk(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("Afk Cog Is Lock And Loaded")

  @commands.Cog.listener()
  async def on_message(self, msg):
    if msg.author.bot:
      return
    
    file = open("afk.json", "r")
    afk = json.load(file)
    if not str(msg.guild.id) in afk:
      return
    if len(msg.mentions) > 0:
      user = msg.mentions[0]
      if user.id in afk[str(msg.guild.id)]["to-mention-ids"]:
        msgs = f"{user.name} is AFK with reason : {afk[str(msg.guild.id)][str(user.id)]}"
        await msg.channel.send(msgs)
    if msg.author.id in afk[str(msg.guild.id)]["to-mention-ids"]:
      index = afk[str(msg.guild.id)]["to-mention-ids"].index(msg.author.id)
      del afk[str(msg.guild.id)]["to-mention-ids"][index]
      afk[str(msg.guild.id)].pop(str(msg.author.id))
      dumps = open("afk.json", "w")
      json.dump(afk, dumps, indent = 4)
      await msg.channel.send("Welcome back {}, I removed your AFK.".format(msg.author.mention), delete_after = 10)
      await msg.author.edit(nick=f"{msg.author.name}")

  @commands.command(aliases=["away_from_keyboard", "Afk"])
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def afk(self, ctx, *, message = "AFK"):
    file = open("afk.json", "r")
    afk = json.load(file)
    if not str(ctx.guild.id) in afk:
      afk[str(ctx.guild.id)] = {}
    if not str(ctx.author.id) in afk[str(ctx.guild.id)]:
      afk[str(ctx.guild.id)][str(ctx.author.id)] = {}
    if not "to-mention-ids" in afk[str(ctx.guild.id)]:
      afk[str(ctx.guild.id)]["to-mention-ids"] = []
    if not ctx.author.id in afk[str(ctx.guild.id)]["to-mention-ids"]:
      afk[str(ctx.guild.id)][str(ctx.author.id)] = message
      afk[str(ctx.guild.id)]["to-mention-ids"].append(ctx.author.id)
      dumps = open("afk.json", "w")
      json.dump(afk, dumps, indent = 4)
      await ctx.send("{}, I have set your AFK with reason : {}".format(ctx.author.mention, message))  
      await ctx.author.edit(nick = f"[AFK] {ctx.author.name}")
    else:
      return

  @afk.error
  async def afk_error(self, ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = discord.Embed(title = "Take a Chill Pill", description = "Woahhh there buddy, we dont want you spamming our afk command.\nWait **{:.2f} seconds**".format(error.retry_after), color = discord.Color(0x3F51B5))
      await ctx.send(embed=embed)

def setup(bot):
  bot.add_cog(Afk(bot))
