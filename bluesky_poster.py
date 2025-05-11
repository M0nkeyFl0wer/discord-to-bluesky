import os
import requests
from atproto import Client
from github import Github
from dotenv import load_dotenv

load_dotenv()

BLUESKY_HANDLE = os.getenv("BLUESKY_HANDLE")
BLUESKY_APP_PASSWORD = os.getenv("BLUESKY_APP_PASSWORD")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = "M0nkeyFl0wer/discord-to-bluesky"

g = Github(GITHUB_TOKEN)
repo = g.get_repo(GITHUB_REPO)
bsky = Client()

def extract_post_and_media(issue_body):
    lines = issue_body.splitlines()
    post_lines = []
    media_urls = []
    in_post = False
    for line in lines:
        if line.startswith("**Proposed Bluesky Post"):
            in_post = True
        elif in_post and line.startswith("**Media:**"):
            in_post = False
        elif in_post:
            post_lines.append(line)
        elif line.strip().startswith("- http"):
            media_urls.append(line.strip().lstrip("- "))
    return "\n".join(post_lines).strip(), media_urls

def download_media(url):
    resp = requests.get(url)
    content_type = resp.headers.get("Content-Type", "application/octet-stream")
    return resp.content, content_type

def post_to_bluesky(text, media_urls):
    bsky.login(BLUESKY_HANDLE, BLUESKY_APP_PASSWORD)
    blobs = []
    for url in media_urls:
        data, mime = download_media(url)
        blob = bsky.com.atproto.repo.upload_blob(data, content_type=mime)
        blobs.append(blob)

    if blobs:
        embed = Client.models.AppBskyEmbedImages.Main(images=[
            Client.models.AppBskyEmbedImages.Image(
                alt="Media from Discord",
                image=blob.blob
            ) for blob in blobs
        ])
        bsky.send_post(text=text, embed=embed)
    else:
        bsky.send_post(text=text)

def main():
    issues = repo.get_issues(state="open", labels=["approved"])
    for issue in issues:
        post_text, media_urls = extract_post_and_media(issue.body)
        print(f"Posting: {post_text}\nMedia: {media_urls}")
        post_to_bluesky(post_text, media_urls)
        issue.add_to_labels("posted")
        issue.edit(state="closed")

if __name__ == "__main__":
    main()# Bluesky posting logic placeholder
