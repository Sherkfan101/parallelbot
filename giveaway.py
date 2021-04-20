'''
Yea this code is a mess
'''
import discord
from discord.ext import commands
import asyncio
from termcolor import colored
import random
import datetime

class giveaway(commands.Cog):

    def __init__(self, client):
        self.client = client

        self.switch = False

        print("System - Giveaway Cog         "+colored('Running', 'green'))

    @commands.command()
    async def gstart(self,ctx, timeInput=None, winners=None, * , prize=None):
        await ctx.message.delete()
        if timeInput is None:
        	embed = discord.Embed(title="Error: Missing Arguements", description="You need to include all of the Arguements of the Giveaway.\n```xml\n< p!gstart <time> <winners> <prize>```\n‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎^\n ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏ ‎‏‏‎ ‎‏‏‎Missing Arguement\n\nError: Missing TimeInput\n\nExplination: Please tell the bot how long the giveaway should be.\nTime - The time until the giveaways ends you can attach [s, m, h, d] to the end to specify seconds, minutes, hours, or days",color=0xff0000)
        	await ctx.send(embed=embed)
        	return
        if winners is None:
        	embed = discord.Embed(title="Error: Missing Arguements", description="You need to include all of the Arguements of the Giveaway.\n```xml\n< p!gstart <time> <winners> <prize>```\n‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎^\n ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎Missing Arguement\n\nError: Missing WinnerCount\n\nExplination: How many winners are in the Giveaway?\nWinners - The amount of winners the giveaway will have. Maximum of 9.",color=0xff0000)
        	await ctx.send(embed=embed)
        	return
        if prize is None:
        	embed = discord.Embed(title="Error: Missing Arguements", description="You need to include all of the Arguements of the Giveaway.\n```xml\n< p!gstart <time> <winners> <prize>```\n‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎^\n ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎‏‏‎ ‎Missing Arguement\n\nError: Missing Prize\n\nExplination: What is the Prize of the Giveaway?\nPrize - The title of the Giveaway Embed",color=0xff0000)
        	await ctx.send(embed=embed)
        	return
        if len(winners) > 2:
            return await ctx.send("Winners can only be 9 or less")
        try:
            time = int(timeInput)
        except:
            convertTimeList = {'s':1, 'm':60, 'h':3600, 'd':86400, 'S':1, 'M':60, 'H':3600, 'D':86400}
            time = int(timeInput[:-1]) * convertTimeList[timeInput[-1]]

        en = datetime.datetime.now() + datetime.timedelta(seconds = time) 
        end = en.strftime("%I:%M %p")
        if winners == "1w":
            winnercount = 1
        if winners == "2w":
            winnercount = 2
        if winners == "3w":
            winnercount = 3
        if winners == "4w":
            winnercount = 4
        if winners == "5w":
            winnercount = 5
        if winners == "6w":
            winnercount = 6
        if winners == "7w":
            winnercount = 7
        if winners == "8w":
            winnercount = 8
        if winners == "9w":
            winnercount = 9
        if winners == "10w":
            winnercount = 10
        if time > 86400:
            await ctx.send("I can\'t do giveaways over a day long")
            return
        if time <= 0:
            await ctx.send("Giveaways don\'t go into negatives :/")
            return
        if time >= 3600:
            embed = discord.Embed(title = f"{prize}", description = f"React with <a:giveaway_yellow:819392280490278942> to enter\n**{time//3600}** hours, **{time%3600//60}** minutes, **{time%60}** seconds\nHosted by {ctx.author}", color = 0xFFF857)
            embed.set_footer(text=f'Winners: {winnercount} | Ends at • {end}')
            message = await ctx.send(embed=embed)
            await message.add_reaction('<a:giveaway_yellow:819392280490278942>')
        elif time >= 60:
            embed = discord.Embed(title = f"{prize}", description = f"React with <a:giveaway_yellow:819392280490278942> to enter\n**{time//60}** minutes, **{time%60}** seconds\nHosted by {ctx.author}", color = 0xFFF857)
            embed.set_footer(text=f'Winners: {winnercount} | Ends at • {end}')
            message = await ctx.send(embed=embed)
            await message.add_reaction('<a:giveaway_yellow:819392280490278942>')
        elif time < 60:
            embed = discord.Embed(title = f"{prize}", description = f"React with <a:giveaway_yellow:819392280490278942> to enter\n**{time}** seconds\nHosted by {ctx.author}", color = 0xFFF857)
            embed.set_footer(text=f'Winners: {winnercount} | Ends at • {end}')
            message = await ctx.send(embed=embed)
            await message.add_reaction('<a:giveaway_yellow:819392280490278942>')
        while True:
            try:
                await asyncio.sleep(6)
                time -= 6
                if time >= 3600:
                    embed = discord.Embed(title = f"{prize}", description = f"React with <a:giveaway_yellow:819392280490278942> to enter\n**{time//3600}** hours, **{time%3600//60}** minutes, **{time%60}** seconds\nHosted by {ctx.author}", color = 0xFFF857)
                    embed.set_footer(text=f'Winners: {winnercount} | Ends at • {end}')
                    await message.edit(embed=embed)
                elif time >= 60:
                    embed = discord.Embed(title = f"{prize}", description = f"React with <a:giveaway_yellow:819392280490278942> to enter\n**{time//60}** minutes, **{time%60}** seconds\nHosted by {ctx.author}", color = 0xFFF857)
                    embed.set_footer(text=f'Winners: {winnercount} | Ends at • {end}')
                    await message.edit(embed=embed)
                elif time < 60:
                    embed = discord.Embed(title = f"{prize}", description = f"React with <a:giveaway_yellow:819392280490278942> to enter\n**{time}** seconds\nHosted by {ctx.author}", color = 0xFFF857)
                    embed.set_footer(text=f'Winners: {winnercount} | Ends at • {end}')
                    await message.edit(embed=embed)
                if time <= 0:
                    m = await ctx.channel.fetch_message(message.id)
                    reactants = await m.reactions[0].users().flatten()
                    reactants.pop(reactants.index(self.client.user))
                    if len(reactants) < winnercount:
                    	await ctx.send("Couldn\'t end the Giveaway. There were not enough members.")
                    	embed = discord.Embed(title="Giveaway Error",description=f"There weren\'t enough members\nLower the winner count\nHosted By: {ctx.author}",color=0xff0000)
                    	embed.set_footer(text=f'Winners: {winnercount} | Ends at • {end}')
                    	await message.edit(embed=embed)
                    	return
                    if winners == "1w":
                        winner = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winner: {winner.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        await winner.send(embed=emb)
                        return 
                    if winners == "2w":
                        winner = random.choice(reactants)
                        winnere = random.choice(reactants)
                        winner = random.choice(reactants)
                        winnere = random.choice(reactants)
                        if winner == winnere:
                            winnere = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention} and {winnere.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winnere.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winnere]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return 
                    if winners == "3w":
                        winner = random.choice(reactants)
                        winner1 = random.choice(reactants)
                        winner2 = random.choice(reactants)
                        while winner1 == winner2:
                            winner1 = random.choice(reactants)
                        while winner2 == winner:
                            winner2 = random.choice(reactants)
                        while winner == winner1:
                            winner1 = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention}, {winner1.mention} and {winner2.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winner1.mention}, {winner2.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winner1,winner2]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return
                    if winners == "4w":
                        winner = random.choice(reactants)
                        winner1 = random.choice(reactants)
                        winner2 = random.choice(reactants)
                        winner3 = random.choice(reactants)
                        while winner1 == winner2:
                            winner1 = random.choice(reactants)
                        while winner2 == winner:
                            winner2 = random.choice(reactants)
                        while winner == winner1:
                            winner1 = random.choice(reactants)
                        while winner == winner3:
                            winner3 = random.choice(reactants)
                        while winner1 == winner3:
                            winner3 = random.choice(reactants)
                        while winner2 == winner3:
                            winner3 = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention}, {winner1.mention}, {winner2.mention} and {winner3.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winner1,winner2,winner3]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return 
                    if winners == "5w":
                        winner = random.choice(reactants)
                        winner1 = random.choice(reactants)
                        winner2 = random.choice(reactants)
                        winner3 = random.choice(reactants)
                        winner4 = random.choice(reactants)
                        while winner1 == winner2:
                            winner1 = random.choice(reactants)
                        while winner2 == winner:
                            winner2 = random.choice(reactants)
                        while winner == winner1:
                            winner1 = random.choice(reactants)
                        while winner == winner3:
                            winner3 = random.choice(reactants)
                        while winner1 == winner3:
                            winner3 = random.choice(reactants)
                        while winner2 == winner3:
                            winner3 = random.choice(reactants)
                        while winner == winner4:
                            winner4 = random.choice(reactants)
                        while winner1 == winner4:
                            winner4 = random.choice(reactants)
                        while winner2 == winner4:
                            winner4 = random.choice(reactants)
                        while winner3 == winner4:
                            winner4 = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winner1,winner2,winner3,winner4]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return 
                    if winners == "6w":
                        winner = random.choice(reactants)
                        winner1 = random.choice(reactants)
                        winner2 = random.choice(reactants)
                        winner3 = random.choice(reactants)
                        winner4 = random.choice(reactants)
                        winner5 = random.choice(reactants)
                        while winner1 == winner2:
                            winner1 = random.choice(reactants)
                        while winner2 == winner:
                            winner2 = random.choice(reactants)
                        while winner == winner1:
                            winner1 = random.choice(reactants)
                        while winner == winner3:
                            winner3 = random.choice(reactants)
                        while winner1 == winner3:
                            winner3 = random.choice(reactants)
                        while winner2 == winner3:
                            winner3 = random.choice(reactants)
                        while winner == winner4:
                            winner4 = random.choice(reactants)
                        while winner1 == winner4:
                            winner4 = random.choice(reactants)
                        while winner2 == winner4:
                            winner4 = random.choice(reactants)
                        while winner3 == winner4:
                            winner4 = random.choice(reactants)
                        while winner == winner5:
                            winner5 = random.choice(reactants)
                        while winner1 == winner5:
                            winner5 = random.choice(reactants)
                        while winner2 == winner5:
                            winner5 = random.choice(reactants)
                        while winner3 == winner5:
                            winner5 = random.choice(reactants)
                        while winner4 == winner5:
                            winner5 = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winner1,winner2,winner3,winner4,winner5]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return         
                    if winners == "7w":
                        winner = random.choice(reactants)
                        winner1 = random.choice(reactants)
                        winner2 = random.choice(reactants)
                        winner3 = random.choice(reactants)
                        winner4 = random.choice(reactants)
                        winner5 = random.choice(reactants)
                        winner6 = random.choice(reactants)
                        while winner1 == winner2:
                            winner1 = random.choice(reactants)
                        while winner2 == winner:
                            winner2 = random.choice(reactants)
                        while winner == winner1:
                            winner1 = random.choice(reactants)
                        while winner == winner3:
                            winner3 = random.choice(reactants)
                        while winner1 == winner3:
                            winner3 = random.choice(reactants)
                        while winner2 == winner3:
                            winner3 = random.choice(reactants)
                        while winner == winner4:
                            winner4 = random.choice(reactants)
                        while winner1 == winner4:
                            winner4 = random.choice(reactants)
                        while winner2 == winner4:
                            winner4 = random.choice(reactants)
                        while winner3 == winner4:
                            winner4 = random.choice(reactants)
                        while winner == winner5:
                            winner5 = random.choice(reactants)
                        while winner1 == winner5:
                            winner5 = random.choice(reactants)
                        while winner2 == winner5:
                            winner5 = random.choice(reactants)
                        while winner3 == winner5:
                            winner5 = random.choice(reactants)
                        while winner4 == winner5:
                            winner5 = random.choice(reactants)
                        while winner == winner6:
                            winner6 = random.choice(reactants)
                        while winner1 == winner6:
                            winner6 = random.choice(reactants)
                        while winner2 == winner6:
                            winner6 = random.choice(reactants)
                        while winner3 == winner6:
                            winner6 = random.choice(reactants)
                        while winner4 == winner6:
                            winner6 = random.choice(reactants)
                        while winner5 == winner6:
                            winner6 = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}, {winner6.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}, {winner6.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winner1,winner2,winner3,winner4,winner5,winner6]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return 
                    if winners == "8w":
                        winner = random.choice(reactants)
                        winner1 = random.choice(reactants)
                        winner2 = random.choice(reactants)
                        winner3 = random.choice(reactants)
                        winner4 = random.choice(reactants)
                        winner5 = random.choice(reactants)
                        winner6 = random.choice(reactants)
                        winner7 = random.choice(reactants)
                        while winner1 == winner2:
                            winner1 = random.choice(reactants)
                        while winner2 == winner:
                            winner2 = random.choice(reactants)
                        while winner == winner1:
                            winner1 = random.choice(reactants)
                        while winner == winner3:
                            winner3 = random.choice(reactants)
                        while winner1 == winner3:
                            winner3 = random.choice(reactants)
                        while winner2 == winner3:
                            winner3 = random.choice(reactants)
                        while winner == winner4:
                            winner4 = random.choice(reactants)
                        while winner1 == winner4:
                            winner4 = random.choice(reactants)
                        while winner2 == winner4:
                            winner4 = random.choice(reactants)
                        while winner3 == winner4:
                            winner4 = random.choice(reactants)
                        while winner == winner5:
                            winner5 = random.choice(reactants)
                        while winner1 == winner5:
                            winner5 = random.choice(reactants)
                        while winner2 == winner5:
                            winner5 = random.choice(reactants)
                        while winner3 == winner5:
                            winner5 = random.choice(reactants)
                        while winner4 == winner5:
                            winner5 = random.choice(reactants)
                        while winner == winner6:
                            winner6 = random.choice(reactants)
                        while winner1 == winner6:
                            winner6 = random.choice(reactants)
                        while winner2 == winner6:
                            winner6 = random.choice(reactants)
                        while winner3 == winner6:
                            winner6 = random.choice(reactants)
                        while winner4 == winner6:
                            winner6 = random.choice(reactants)
                        while winner5 == winner6:
                            winner6 = random.choice(reactants)
                        while winner == winner7:
                            winner7 = random.choice(reactants)
                        while winner1 == winner7:
                            winner7 = random.choice(reactants)
                        while winner2 == winner7:
                            winner7 = random.choice(reactants)
                        while winner3 == winner7:
                            winner7 = random.choice(reactants)
                        while winner4 == winner7:
                            winner7 = random.choice(reactants)
                        while winner5 == winner7:
                            winner7 = random.choice(reactants)
                        while winner6 == winner7:
                            winner7 = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}, {winner6.mention}, {winner7.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}, {winner6.mention}, {winner7.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winner1,winner2,winner3,winner4,winner5,winner6,winner7]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return 
                    if winners == "9w":
                        winner = random.choice(reactants)
                        winner1 = random.choice(reactants)
                        winner2 = random.choice(reactants)
                        winner3 = random.choice(reactants)
                        winner4 = random.choice(reactants)
                        winner5 = random.choice(reactants)
                        winner6 = random.choice(reactants)
                        winner7 = random.choice(reactants)
                        winner8 = random.choice(reactants)
                        while winner1 == winner2:
                            winner1 = random.choice(reactants)
                        while winner2 == winner:
                            winner2 = random.choice(reactants)
                        while winner == winner1:
                            winner1 = random.choice(reactants)
                        while winner == winner3:
                            winner3 = random.choice(reactants)
                        while winner1 == winner3:
                            winner3 = random.choice(reactants)
                        while winner2 == winner3:
                            winner3 = random.choice(reactants)
                        while winner == winner4:
                            winner4 = random.choice(reactants)
                        while winner1 == winner4:
                            winner4 = random.choice(reactants)
                        while winner2 == winner4:
                            winner4 = random.choice(reactants)
                        while winner3 == winner4:
                            winner4 = random.choice(reactants)
                        while winner == winner5:
                            winner5 = random.choice(reactants)
                        while winner1 == winner5:
                            winner5 = random.choice(reactants)
                        while winner2 == winner5:
                            winner5 = random.choice(reactants)
                        while winner3 == winner5:
                            winner5 = random.choice(reactants)
                        while winner4 == winner5:
                            winner5 = random.choice(reactants)
                        while winner == winner6:
                            winner6 = random.choice(reactants)
                        while winner1 == winner6:
                            winner6 = random.choice(reactants)
                        while winner2 == winner6:
                            winner6 = random.choice(reactants)
                        while winner3 == winner6:
                            winner6 = random.choice(reactants)
                        while winner4 == winner6:
                            winner6 = random.choice(reactants)
                        while winner5 == winner6:
                            winner6 = random.choice(reactants)
                        while winner == winner7:
                            winner7 = random.choice(reactants)
                        while winner1 == winner7:
                            winner7 = random.choice(reactants)
                        while winner2 == winner7:
                            winner7 = random.choice(reactants)
                        while winner3 == winner7:
                            winner7 = random.choice(reactants)
                        while winner4 == winner7:
                            winner7 = random.choice(reactants)
                        while winner5 == winner7:
                            winner7 = random.choice(reactants)
                        while winner6 == winner7:
                            winner7 = random.choice(reactants)
                        while winner == winner8:
                            winner8 = random.choice(reactants)
                        while winner1 == winner8:
                            winner8 = random.choice(reactants)
                        while winner2 == winner8:
                            winner8 = random.choice(reactants)
                        while winner3 == winner8:
                            winner8 = random.choice(reactants)
                        while winner4 == winner8:
                            winner8 = random.choice(reactants)
                        while winner5 == winner8:
                            winner8 = random.choice(reactants)
                        while winner6 == winner8:
                            winner8 = random.choice(reactants)
                        while winner7 == winner8:
                            winner8 = random.choice(reactants)

                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}, {winner6.mention}, {winner7.mention}, {winner8.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}, {winner6.mention}, {winner7.mention}, {winner8.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winner1,winner2,winner3,winner4,winner5,winner6,winner7,winner8]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return 
                    if winners == "10w":
                        winner = random.choice(reactants)
                        winner1 = random.choice(reactants)
                        winner2 = random.choice(reactants)
                        winner3 = random.choice(reactants)
                        winner4 = random.choice(reactants)
                        winner5 = random.choice(reactants)
                        winner6 = random.choice(reactants)
                        winner7 = random.choice(reactants)
                        winner8 = random.choice(reactants)
                        winner9 = random.choice(reactants)
                        while winner1 == winner2:
                            winner1 = random.choice(reactants)
                        while winner2 == winner:
                            winner2 = random.choice(reactants)
                        while winner == winner1:
                            winner1 = random.choice(reactants)
                        while winner == winner3:
                            winner3 = random.choice(reactants)
                        while winner1 == winner3:
                            winner3 = random.choice(reactants)
                        while winner2 == winner3:
                            winner3 = random.choice(reactants)
                        while winner == winner4:
                            winner4 = random.choice(reactants)
                        while winner1 == winner4:
                            winner4 = random.choice(reactants)
                        while winner2 == winner4:
                            winner4 = random.choice(reactants)
                        while winner3 == winner4:
                            winner4 = random.choice(reactants)
                        while winner == winner5:
                            winner5 = random.choice(reactants)
                        while winner1 == winner5:
                            winner5 = random.choice(reactants)
                        while winner2 == winner5:
                            winner5 = random.choice(reactants)
                        while winner3 == winner5:
                            winner5 = random.choice(reactants)
                        while winner4 == winner5:
                            winner5 = random.choice(reactants)
                        while winner == winner6:
                            winner6 = random.choice(reactants)
                        while winner1 == winner6:
                            winner6 = random.choice(reactants)
                        while winner2 == winner6:
                            winner6 = random.choice(reactants)
                        while winner3 == winner6:
                            winner6 = random.choice(reactants)
                        while winner4 == winner6:
                            winner6 = random.choice(reactants)
                        while winner5 == winner6:
                            winner6 = random.choice(reactants)
                        while winner == winner7:
                            winner7 = random.choice(reactants)
                        while winner1 == winner7:
                            winner7 = random.choice(reactants)
                        while winner2 == winner7:
                            winner7 = random.choice(reactants)
                        while winner3 == winner7:
                            winner7 = random.choice(reactants)
                        while winner4 == winner7:
                            winner7 = random.choice(reactants)
                        while winner5 == winner7:
                            winner7 = random.choice(reactants)
                        while winner6 == winner7:
                            winner7 = random.choice(reactants)
                        while winner == winner8:
                            winner8 = random.choice(reactants)
                        while winner1 == winner8:
                            winner8 = random.choice(reactants)
                        while winner2 == winner8:
                            winner8 = random.choice(reactants)
                        while winner3 == winner8:
                            winner8 = random.choice(reactants)
                        while winner4 == winner8:
                            winner8 = random.choice(reactants)
                        while winner5 == winner8:
                            winner8 = random.choice(reactants)
                        while winner6 == winner8:
                            winner8 = random.choice(reactants)
                        while winner7 == winner8:
                            winner8 = random.choice(reactants) 
                        while winner == winner9:
                            winner9 = random.choice(reactants)
                        while winner1 == winner9:
                            winner9 = random.choice(reactants)
                        while winner2 == winner9:
                            winner9 = random.choice(reactants)
                        while winner3 == winner9:
                            winner9 = random.choice(reactants)
                        while winner4 == winner9:
                            winner9 = random.choice(reactants)
                        while winner5 == winner9:
                            winner9 = random.choice(reactants)
                        while winner6 == winner9:
                            winner9 = random.choice(reactants)
                        while winner7 == winner9:
                            winner9 = random.choice(reactants)
                        while winner8 == winner9:
                            winner9 = random.choice(reactants)
                        embed = discord.Embed(
                            title=f'{prize}',
                            description=f'Winners: {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}, {winner6.mention}, {winner7.mention}, {winner8.mention}, {winner9.mention}\n\nHosted By: {ctx.author.mention}',
                            color=0x2e3135
                        )
                        embed.set_footer(text=f"Winners: {winnercount} | Ended at • {end}")
                        await message.edit(embed=embed)
                        await ctx.send(f"**CONGRATS**\n<a:pepemoneyrain:819391189009956875> **Prize:** {prize}\n<a:yay:819391235441557535> **Winners:** {winner.mention}, {winner1.mention}, {winner2.mention}, {winner3.mention}, {winner4.mention}, {winner5.mention}, {winner6.mention}, {winner7.mention}, {winner8.mention}, {winner9.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{message.id}")
                        emb = discord.Embed(title='You won a giveaway 🎉', description=f'You won a giveaway in {ctx.guild.name} for [**{prize}**]({message.jump_url}).\nPlease wait for your prize, {ctx.author.mention} is the host.', color=0xFFF857)
                        h = [winner,winner1,winner2,winner3,winner4,winner5,winner6,winner7,winner8,winner9]
                        for dude in h: 
                            try:
                                await dude.send(embed=emb)
                            except Forbidden:
                                print(f'Couldn\'t dm {dude.name}')
                        return
            except:
                break
                
    @commands.command(aliases=['reroll'])
    async def greroll(self,ctx, id_ : int):
        channel = ctx.channel
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            await ctx.send("The id was entered incorrectly.")
            return
        
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)

        await channel.send(f"**CONGRATS**\n<a:yay:819391235441557535> **Winners:** {winner.mention}\n<a:cool:819391289418055760> **Giveaway:** https://discord.com/channels/{ctx.guild.id}/{ctx.channel.id}/{id_}")

def setup(client):
    client.add_cog(giveaway(client))
