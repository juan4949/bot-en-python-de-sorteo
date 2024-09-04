import discord 
from discord.ext import commands

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    CHANNEL_ID = 1279636388848996447

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.CHANNEL_ID)
        if channel:
            try:
                await channel.send(f"{member.mention}")
                
                embed = discord.Embed(
                    title="¡Bienvenido al servidor! 🎉",
                    description="Espero te vaya genial por este gran servidor.",
                    color=discord.Color.blue()
                )

                embed.set_thumbnail(url="https://discord.com/assets/5d69e29f0d71aaa04ed9725100199b4e.png")

                await channel.send(embed=embed)
            except Exception as e:
                print(f"Error al enviar mensaje de bienvenida: {e}")
        else:
            print("No se encontró el canal")

async def setup(bot):
    await bot.add_cog(Welcome(bot))