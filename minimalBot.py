import discord
from discord.ext import commands,tasks
import asyncpg
client = commands.Bot(command_prefix='.')
import psycopg2
import nlp1
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command(aliases=['out'])    
async def run(ctx):
    conn = psycopg2.connect("dbname=train user=postgres password=passmein@16")
    cur = conn.cursor()
    await ctx.send("Enter sql")
    sql = await client.wait_for("message")
    text_con = nlp1.NLP_SQL(sql.content)
    print(text_con)
    cur.execute(text_con)
    out = cur.fetchall()
    for i in out:
        embed = discord.Embed(title="NLP", description="Welcome to NLP test", color=discord.Color.random())
        embed.add_field(name="train Number", value=i[0])
        embed.add_field(name="train Name", value=i[1])
        embed.add_field(name="Starts at ", value=i[2])
        embed.add_field(name="Ends at ", value=i[3])
        await ctx.send(embed=embed)
    cur.close()
    conn.close()



client.run('OTI0MTcwNDAxMDcwODQxODU3.YcaqwQ.RBq2na_G9CuGnA97uSlrNyA1MZ4')

