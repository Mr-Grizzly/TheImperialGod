import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.filtered_words = ['idiot', 'Idiots', "DIE", "ass", "butt", "Fool", "shit", "bitch"]
        self.INVITE_LINK = "https://discordapp.com/oauth2/authorize?&client_id=768695035092271124&scope=bot&permissions=21474836398"


    @commands.Cog.listener()
    async def on_ready(self):
        print("Misc commands are ready!")

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title = "Invite Link:", color = ctx.author.color)
        embed.add_field(name = "Here:", value = f"[Click me]({self.INVITE_LINK})")
        await ctx.send(embed = embed)

    @commands.command(aliases = ["sc"])
    async def servercount(self, ctx):
        sc = 0
        for i in self.client.guilds:
            sc += 1
        embed = discord.Embed(title = "Server Count", color = ctx.author.color)
        embed.add_field(name = "Server Count:", value = f"`{sc}`")
        embed.add_field(name = "User Count:", value = f'`{len(self.client.users)}`')
        await ctx.send(embed = embed)

    @commands.command()
    async def candy(self, ctx):
        await ctx.send("You want candy, take it!")
        await ctx.send(file = discord.File("./assets/candy.jpg"))
    
    @commands.command()
    async def say(self, ctx, *, msg = None):
        if msg == None:
            await ctx.send("No message provided!")
            return

        for word in self.filtered_words:
            if word in msg.content:
                return
        
        await ctx.send(msg)

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def suggest(self, ctx, *, suggestion):
        await ctx.send("Your suggestion has been sent to the devs!")
        embed = discord.Embed(title = "New Suggestions", color = discord.Color.red())
        embed.add_field(name = "Author:", value = f"`{ctx.author.name}`")
        embed.add_field(name = "Server:", value = f"`{ctx.guild.name}`")
        embed.add_field(name = "Suggestion: ", value = f"`{suggestion}`")
        # sending it to the support server
        guild = self.client.get_guild(781057246092197898)
        # sending it in the channel
        for channel in guild.channels:
            if channel.id == 781363343780741140:
                await channel.send(embed = embed)
    
    @suggest.error
    async def suggest_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            embed = discord.Embed(title = "Slow it down C'mon", color = ctx.author.color)
            embed.add_field(name = 'Reason:', value = "If you have these many suggestions contact NightZan999!")
            await ctx.send(embed = embed)

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(title = "Support Me! 🎉", color = ctx.author.color,
        description = """
        :link: Vote for me on top.gg, [here](https://top.gg/bot/768695035092271124/vote)\n
        :link: Please leave a review on top.gg [here](https://top.gg/bot/768695035092271124#reviews)
        """
        )
        embed.add_field(name = "Invite Link!", value = f":link: [Invite Link]({self.INVITE_LINK})")
        embed.add_field(name = "Support Server!", value = f":link: [Support Server](https://discord.gg/WQhBqAuUqG)")
        embed.add_field(name = "Website:", value = f":link: [Website](https://theimperialgodwebsite.nightzan.repl.co/)")
        embed.add_field(name = "Why Support me?", inline = False, value = f"""Look, its your choice whether or not you would like to help me out.\n
        But if you like how I roll and think that I help your servers, just by doing these small tasks you can take me to other people who
        are in need like you.\n\nPlus I have 70 commands and am in just {len(self.client.guilds)} servers.
        """)
        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Misc(client))