roles.py (Python):

import discord

class RolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='assign_role')
    async def assign_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.add_roles(role)
            await ctx.send(f'{member.mention} has been assigned the role {role.name}')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')

    @commands.command(name='remove_role')
    async def remove_role(self, ctx, member: discord.Member, role: discord.Role):
        try:
            await member.remove_roles(role)
            await ctx.send(f'{member.mention} has been removed from the role {role.name}')
        except Exception as e:
            await ctx.send(f'An error occurred: {e}')

def setup(bot):
    bot.add_cog(RolesCog(bot))