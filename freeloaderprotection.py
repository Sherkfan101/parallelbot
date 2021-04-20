import discord
import os
from discord.ext import commands
import discord, time, asyncio, os, random, json, re
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, cooldown, MissingPermissions, check, has_role
from discord.utils import get
from discord_webhook import DiscordWebhook, DiscordEmbed
from termcolor import colored



class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.switch = False

        print("System - Heist Leave Ban          "+colored('Running', 'green'))

    def is_authed(ctx):
        authed = []
        return ctx.authod.id in authed

    @commands.command()
    @has_permissions(administrator=True)
    async def heistban(self, ctx):
        self.switch = True
        await ctx.send("Now banning leaves for 2hrs!")

        t_end = time.time() + 7200
        while time.time() < t_end:
            pass
            await asyncio.sleep(1)

        self.switch = False

    @commands.command()
    @has_permissions(administrator=True)
    async def stopheistban(self, ctx):
        self.switch = False
        await ctx.send("Ok, Stopped banning leaves!")


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        if self.switch:
            await member.ban(reason="Heist Ban - Banned because they left after a heist!")
     



def setup(client):
    client.add_cog(Example(client))
