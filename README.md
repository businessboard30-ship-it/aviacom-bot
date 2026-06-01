# AVIACOM Telegram Bot

## What this bot does
- Opens your game as a Telegram Mini App
- Tracks every group and channel it's added to
- Auto-posts an ad with PLAY button when made admin
- Sends ad blasts to all admin groups with /sendad
- Notifies you (owner) of every new group added

## Bot Commands
- /start — Welcome message with Play button
- /play — Open the game
- /stats — (Owner only) See all groups/channels stats
- /sendad — (Owner only) Blast ad to all admin groups
- /listgroups — (Owner only) List all groups/channels

## Setup on Railway

### Step 1 — Upload to GitHub
1. Create a new GitHub repo called `aviacom-bot`
2. Upload these 3 files: bot.py, requirements.txt, Procfile

### Step 2 — Deploy on Railway
1. Go to railway.app and sign up
2. Click New Project → Deploy from GitHub
3. Select your aviacom-bot repo
4. Go to Variables and add:
   - BOT_TOKEN = 8805295472:AAEX198MM0mh4lTe4xdJ2vGB9Ml5B0XLYL8
   - GAME_URL = https://businessboard30-ship-it.github.io/aviacom/
   - OWNER_ID = 8162426062
5. Deploy — bot will be live in 2 minutes!

### Step 3 — Set up Mini App on Telegram
1. Open @BotFather on Telegram
2. Send /mybots
3. Select @AVIACOM_BOT
4. Click Bot Settings → Menu Button
5. Set URL to: https://businessboard30-ship-it.github.io/aviacom/
6. Set button text to: 🚀 Play Aviacom

## Environment Variables
| Variable  | Value |
|-----------|-------|
| BOT_TOKEN | Your bot token |
| GAME_URL  | Your game URL |
| OWNER_ID  | Your Telegram user ID |
