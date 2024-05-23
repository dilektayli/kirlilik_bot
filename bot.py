import discord
from discord.ext import commands
import requests

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} olarak giriş yapıldı.')

@bot.command()
async def geri_donusum(ctx, *, mesaj):
    # Geri dönüşümle ilgili bilgi almak için bir API'ye istek gönder
    api_url = 'API_URL_BURAYA_GELECEK'
    params = {'sorgu': mesaj}
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        # API'den gelen veriyi kullanarak bir mesaj oluştur
        await ctx.send(f"Geri dönüşüm bilgisi: {data['bilgi']}")
    else:
        await ctx.send('Bir hata oluştu, lütfen daha sonra tekrar deneyin.')

# Botunuzu çalıştırmak için tokeninizi buraya girin
bot.run('YOUR_DISCORD_BOT_TOKEN')
