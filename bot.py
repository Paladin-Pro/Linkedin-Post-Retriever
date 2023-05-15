import discord
from linkedin import linkedin
import requests
import json
import os
from dotenv import load_dotenv
from discord.ext import tasks, commands

client = commands.Bot(command_prefix='!')

linkedin_api_url = 'https://api.linkedin.com/v2/shares?q=owners&owners=urn:li:organization:<company-id>&count=1'

discord_channel_id = '<channel-id>'

access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')

@tasks.loop(seconds=60)
async def post_linkedin_to_discord():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(linkedin_api_url, headers=headers)
    response_json = response.json()

    latest_share = response_json.get('elements')[0]

    if post_linkedin_to_discord.latest_share != latest_share:
        post_linkedin_to_discord.latest_share = latest_share
        discord_channel = client.get_channel(discord_channel_id)
        await discord_channel.send(f'New post on LinkedIn: {latest_share.get("text").get("text")}\n{latest_share.get("originalUrl")}')

@post_linkedin_to_discord.before_loop
async def before_post_linkedin_to_discord():
    await client.wait_until_ready()
    post_linkedin_to_discord.latest_share = None

post_linkedin_to_discord.start()
client.run('<discord-bot-token>')