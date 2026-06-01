import os
import json
import asyncio
import logging
from datetime import datetime
from telegram import (
    Update, InlineKeyboardButton, InlineKeyboardMarkup,
    WebAppInfo, ChatMemberAdministrator, ChatMemberOwner
)
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    ChatMemberHandler, ContextTypes, filters
)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ── CONFIG ──
BOT_TOKEN   = os.environ.get("BOT_TOKEN", "8805295472:AAEX198MM0mh4lTe4xdJ2vGB9Ml5B0XLYL8")
GAME_URL    = os.environ.get("GAME_URL", "https://businessboard30-ship-it.github.io/aviacom/")
OWNER_ID    = int(os.environ.get("OWNER_ID", "8162426062"))
DATA_FILE   = "groups.json"

# ── AD MESSAGE ──
AD_TEXT = (
    "🚀 <b>AVIACOM — Rocket to Riches</b>\n\n"
    "Watch the multiplier soar and cash out before it crashes!\n\n"
    "💸 Real GHS payouts\n"
    "🎯 Minimum bet: GHS 2\n"
    "👥 Refer friends & earn 2% of their wins forever\n"
    "🔒 Powered by Paystack\n\n"
    "👇 Tap below to play now!"
)

# ── DATA HELPERS ──
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"groups": {}, "channels": {}}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def play_button():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🚀 PLAY AVIACOM NOW", web_app=WebAppInfo(url=GAME_URL))]
    ])

# ── BOT ADDED TO GROUP/CHANNEL ──
async def track_chat_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.my_chat_member
    if not result:
        return

    chat = result.chat
    new_status = result.new_chat_member.status
    old_status = result.old_chat_member.status

    data = load_data()
    chat_type = "channels" if chat.type == "channel" else "groups"
    chat_id = str(chat.id)

    # Bot was added
    if new_status in ["member", "administrator"] and old_status in ["left", "kicked"]:
        data[chat_type][chat_id] = {
            "title": chat.title,
            "id": chat.id,
            "type": chat.type,
            "joined": datetime.now().isoformat(),
            "is_admin": new_status == "administrator"
        }
        save_data(data)
        logger.info(f"Bot added to {chat.type}: {chat.title} ({chat.id})")

        # Notify owner
        await context.bot.send_message(
            chat_id=OWNER_ID,
            text=f"✅ <b>Bot added to {chat.type}!</b>\n\n"
                 f"Name: {chat.title}\n"
                 f"ID: {chat.id}\n"
                 f"Admin: {'Yes' if new_status == 'administrator' else 'No'}",
            parse_mode="HTML"
        )

        # Post ad if admin
        if new_status == "administrator":
            try:
                await context.bot.send_message(
                    chat_id=chat.id,
                    text=AD_TEXT,
                    parse_mode="HTML",
                    reply_markup=play_button()
                )
            except Exception as e:
                logger.error(f"Could not post ad: {e}")

    # Bot was removed
    elif new_status in ["left", "kicked"]:
        if chat_id in data[chat_type]:
            data[chat_type][chat_id]["left"] = datetime.now().isoformat()
            save_data(data)
        logger.info(f"Bot removed from {chat.type}: {chat.title}")

    # Bot was made admin
    elif new_status == "administrator" and old_status == "member":
        if chat_id in data[chat_type]:
            data[chat_type][chat_id]["is_admin"] = True
            save_data(data)

        # Post ad now that we're admin
        try:
            await context.bot.send_message(
                chat_id=chat.id,
                text=AD_TEXT,
                parse_mode="HTML",
                reply_markup=play_button()
            )
            await context.bot.send_message(
                chat_id=OWNER_ID,
                text=f"👑 <b>Bot made admin in {chat.title}!</b>\nAd posted automatically.",
                parse_mode="HTML"
            )
        except Exception as e:
            logger.error(f"Could not post ad after admin: {e}")

# ── /start COMMAND ──
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(
        f"🚀 <b>Welcome to AVIACOM, {user.first_name}!</b>\n\n"
        f"Tap the button below to play and win real GHS!",
        parse_mode="HTML",
        reply_markup=play_button()
    )

# ── /play COMMAND ──
async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 <b>Ready to play?</b>\n\nTap below to open the game!",
        parse_mode="HTML",
        reply_markup=play_button()
    )

# ── /stats COMMAND (owner only) ──
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ You are not authorized.")
        return

    data = load_data()
    groups   = data.get("groups", {})
    channels = data.get("channels", {})

    admin_groups   = [g for g in groups.values()   if g.get("is_admin")]
    admin_channels = [c for c in channels.values() if c.get("is_admin")]

    msg = (
        f"📊 <b>AVIACOM BOT STATS</b>\n\n"
        f"👥 Groups: {len(groups)} total, {len(admin_groups)} as admin\n"
        f"📢 Channels: {len(channels)} total, {len(admin_channels)} as admin\n\n"
    )

    if groups:
        msg += "<b>Groups:</b>\n"
        for g in list(groups.values())[:10]:
            admin = "👑" if g.get("is_admin") else "👤"
            msg += f"{admin} {g['title']}\n"

    if channels:
        msg += "\n<b>Channels:</b>\n"
        for c in list(channels.values())[:10]:
            admin = "👑" if c.get("is_admin") else "👤"
            msg += f"{admin} {c['title']}\n"

    await update.message.reply_text(msg, parse_mode="HTML")

# ── /sendad COMMAND (owner only) — blast ad to all admin groups/channels ──
async def sendad(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        await update.message.reply_text("❌ You are not authorized.")
        return

    data = load_data()
    sent = 0
    failed = 0

    all_chats = {**data.get("groups", {}), **data.get("channels", {})}

    for chat_id, info in all_chats.items():
        if info.get("left"):
            continue
        try:
            # Check if bot is actually admin before sending
            member = await context.bot.get_chat_member(int(chat_id), context.bot.id)
            if member.status not in ["administrator", "creator"]:
                failed += 1
                continue
            await context.bot.send_message(
                chat_id=int(chat_id),
                text=AD_TEXT,
                parse_mode="HTML",
                reply_markup=play_button()
            )
            # Mark as admin in data
            info["is_admin"] = True
            sent += 1
            await asyncio.sleep(0.5)
        except Exception as e:
            failed += 1
            logger.error(f"Failed to send ad to {chat_id}: {e}")
    save_data(data)

    await update.message.reply_text(
        f"📢 <b>Ad blast complete!</b>\n\n"
        f"✅ Sent: {sent}\n❌ Failed: {failed}",
        parse_mode="HTML"
    )

# ── /listgroups COMMAND (owner only) ──
async def listgroups(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return

    data = load_data()
    all_chats = {**data.get("groups", {}), **data.get("channels", {})}

    if not all_chats:
        await update.message.reply_text("No groups or channels yet.")
        return

    msg = f"📋 <b>ALL CHATS ({len(all_chats)})</b>\n\n"
    for info in all_chats.values():
        status = "👑 Admin" if info.get("is_admin") else "👤 Member"
        left = " (left)" if info.get("left") else ""
        msg += f"{status} — {info['title']}{left}\n"

    await update.message.reply_text(msg, parse_mode="HTML")

# ── /addgroup COMMAND (owner only) — manually add a group ID ──
async def addgroup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != OWNER_ID:
        return
    if not context.args:
        await update.message.reply_text(
            "Usage: /addgroup <group_id>

To get a group ID, forward a message from the group to @userinfobot"
        )
        return
    group_id = context.args[0]
    data = load_data()
    try:
        chat = await context.bot.get_chat(int(group_id))
        member = await context.bot.get_chat_member(int(group_id), context.bot.id)
        is_admin = member.status in ["administrator", "creator"]
        data["groups"][group_id] = {
            "title": chat.title,
            "id": int(group_id),
            "type": chat.type,
            "joined": datetime.now().isoformat(),
            "is_admin": is_admin
        }
        save_data(data)
        await update.message.reply_text(
            f"✅ Added: {chat.title}\nAdmin: {'Yes' if is_admin else 'No'}"
        )
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")

# ── MAIN ──
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("sendad", sendad))
    app.add_handler(CommandHandler("listgroups", listgroups))
    app.add_handler(CommandHandler("addgroup", addgroup))
    app.add_handler(ChatMemberHandler(track_chat_member, ChatMemberHandler.MY_CHAT_MEMBER))

    logger.info("AVIACOM Bot starting...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
