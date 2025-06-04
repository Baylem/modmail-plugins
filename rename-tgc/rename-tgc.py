import discord
from discord.ext import commands
import core
import re


class TemplateRename(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @core.checks.thread_only()
    @core.checks.has_permissions(core.models.PermissionLevel.SUPPORTER)
    async def rename(self, ctx, *, template: str):
        recipient = ctx.thread.recipient

        main_guild = self.bot.get_guild(int(self.bot.config.get("guild_id")))
        member = main_guild.get_member(recipient.id) if main_guild else None

        new_name = template
        new_name = new_name.replace("{{author.id}}", str(recipient.id))
        new_name = new_name.replace("{{author.username}}", recipient.name)
        new_name = new_name.replace(
            "{{author.nickname}}", member.display_name if member else recipient.name
        )

        new_name = new_name.lower().replace(" ", "-")
        new_name = re.sub(r"[^a-z0-9\-_]", "", new_name)
        new_name = new_name[:100]

        try:
            await ctx.channel.edit(name=new_name)
            await ctx.send(f"Renamed to: `{new_name}`")
        except Exception:
            await ctx.send("Failed to rename channel")


async def setup(bot):
    await bot.add_cog(TemplateRename(bot))
