import discord # importing discord
from discord.ext import commands
import core
import re

# you can change TemplateRename to whatever you want <3
class TemplateRename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @core.checks.thread_only() # as you requested, it's thread only :) :P :)
    @core.checks.has_permissions(core.models.PermissionLevel.SUPPORTER)
    async def rename(self, ctx, *, template: str):
        recipient = ctx.thread.recipient

        main_guild = self.bot.get_guild(int(self.bot.config.get("guild_id"))) # DONT PUT YOUR GUILD IT HERE! THE MAGIC DOES IT.
        member = main_guild.get_member(recipient.id) if main_guild else None

        new_name = template # i actually dont know where template is? # oh im a idiot it is DEFINED HERE! silly me! uwu https://tenor.com/en-GB/view/paul-allen-willem-dafoe-patrick-bateman-american-psycho-chad-uv-uk-ondi-gif-27368842
        new_name = new_name.replace("{{author.id}}", str(recipient.id))
        new_name = new_name.replace("{{author.username}}", recipient.name)
        new_name = new_name.replace(
            "{{author.nickname}}", member.display_name if member else recipient.name
        )

        new_name = new_name.lower().replace(" ", "-")
        new_name = re.sub(r"[^a-z0-9\-_]", "", new_name) # thbe "[]"" may look like gibberish but its complex sub
        new_name = new_name[:100]

        try:
            await ctx.channel.edit(name=new_name)
            await ctx.send(f"Renamed to: `{new_name}`")
        except Exception:
            await ctx.send("Failed to rename channel") # this errors when it does not work, if this happens PANICK

async def setup(bot):
    await bot.add_cog(TemplateRename(bot)) 


# Pride Awareness 2025 VS Code Plugin
# Please educate yourself:
# https://www.communityintegratedcare.co.uk/pride-month-2025/

# <3 hope u enjoy it my friend! lovce and peace, <3 xo xo 🏳️‍🌈 🏳️‍🌈 🏳️‍🌈 🏳️‍🌈