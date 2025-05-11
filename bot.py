import discord
import openai
import os
from github import Github
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = "M0nkeyFl0wer/discord-to-bluesky"  # Adjust if repo name changes
TARGET_CHANNEL_ID = 123456789012345678  # Replace with your actual Discord thread or channel ID

# Initialize APIs
openai.api_key = OPENAI_API_KEY
g = Github(GITHUB_TOKEN)

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def summarize_for_bluesky(message_content):
    prompt = f"Rewrite this Discord update as a polished Bluesky post under 300 characters:\n\n{message_content}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response.choices[0].message["content"].strip()

def create_issue(original_text, gpt_post, media_urls=[]):
    repo = g.get_repo(GITHUB_REPO)
    body = f"""**Source (Discord):**
> {original_text}

**Proposed Bluesky Post (by GPT):**
{gpt_post}

**Media:**\n"""
    for url in media_urls:
        body += f"- {url}\n"

    repo.create# Discord listener placeholder
