## PyWaifu

PyWaifu is a simple package that shows cute waifus

~~~python
#  Simple example
import pywaifu

print(pywaifu.waifu())
~~~

**> Parameters**
- waifu()

~~~python
#  Returns a random image link 
import pywaifu

print(pywaifu.waifu())
~~~

- version
~~~python
#  Returns the package version
import pywaifu
print(pywaifu.__version__)
~~~

###Basic example in a discord bot
~~~python
import discord
import pywaifu

bot = discord.Bot()

@bot.slash_command()
async def waifu(ctx):
    result = pywaifu.waifu()
    await ctx.respond(result)

bot.run('your_secret_token')
~~~
