import asyncio
import time
import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from pyrogram import Client, filters

# ================= CONFIG =================

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Apna Telegram ID yaha daalo
SUDO_USERS = [8021000961]

app = Client(
    "custombot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =============== RENDER PORT ===============

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot Running")

def run_web():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), Handler)
    server.serve_forever()

threading.Thread(target=run_web, daemon=True).start()

# =============== CUSTOM LINES ===============

CUSTOM_LINES = [
    
    "🔥 teri mummy ki chut!",
    "⚡ bahen k lode teri dadi ki black hairy pussy",
    "🚀 teri mummy ko ulta ltkakr taangduga aur uski chut maruga!",
    "✨ bsdk teri mummy teri dadi sb randi ki bachi h",
    "bahenklodo tumhari maa meri setting",
    "bahenklodo tumhari maa meri setting",
    "teri mummy randi h randi bsdk",
    "teri mummy ki pussy m scooter dalduga",
    "teri mummy ki pussy me cum krduga randi maa k bache",
    "tera khandan hi randiyo ka h",
    "teri dadi ki pussy me mera lund",
    "teri mummy ko chodkr ulta ltkakr uske muh me loda deduga",
    "teri mummy ko deepthroat deduga madarchod k bache",
    "✌️✌️tera papa bhi randi ki aulad h bsdk",
    "teri mummy ko yoga sikhaduga aur usko different styles me choduga",
    "tera papa hu mai teri mummy ka bf jis s vo chudkr gyi thi",
    "teri maa ki pussy me scooter dalduga bahen k lode🤣🤣",
    "teri maa ki chut me bihari gutka khakr thuk kr chale gye the🔥🔥",
    "💀💀teri maa ka bosda randi k beej",
    "✌️✌️teri maa ki chut me 2finger dekr uska paani nikalduga0",
    "🔥🔥teri maa k muh me gass pipe dekr uski gaand me fire lgakr tere baap ki gaand jalauga",
    "😂😍😍teri randi maa ko chodkr maine gb road pr beach diya tha",
    "🙌🙌teri mummy k haath divar pr lgvadiye the 10bihariyo ne",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑵𝑭𝑻 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑨𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑳𝑨𝑮𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",

"𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑩𝑬𝑯𝑬𝑵 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑩𝑨𝑨𝑷 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑭𝑨𝑴𝑰𝑳𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑲𝑼𝑻𝑻𝑬 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",

"𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑨𝑼𝑲𝑨𝑨𝑻 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰𝑷𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑬 𝑳𝑶𝑫𝑬 𝑲𝑶 𝑨𝑰𝑹𝑫𝑹𝑶𝑷 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑩𝑨𝑹𝑪𝑶𝑫𝑬 𝑳𝑨𝑮𝑨 𝑲𝑬 𝑺𝑪𝑨𝑵 𝑲𝑨𝑹𝑾𝑨𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑰 𝑴𝑼𝑴𝑴𝒀 𝑲𝑶 𝑨𝑰 𝑻𝑶𝑶𝑳 𝑺𝑬 𝑼𝑷𝑺𝑪𝑨𝑳𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝑻𝑶𝑹𝑹𝑬𝑵𝑻 𝑩𝑨𝑵𝑨𝑲𝑬 𝑺𝑬𝑬𝑫 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑭𝑰𝑹𝑬𝑾𝑨𝑳𝑳 𝑳𝑨𝑮𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑪𝑯𝑼𝑻 𝑴𝑬 𝑺𝑺𝑫 𝑩𝑶𝑶𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑳𝑼𝑵𝑫 𝑶𝑳𝑿 𝑷𝑬 𝑩𝑬𝑪𝑯 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑰 𝑮𝑨𝑨𝑵𝑫 𝑴𝑬 𝑸𝑹 𝑪𝑶𝑫𝑬 𝑪𝑯𝑰ℙ𝑲𝑨 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑩𝑯𝑺𝑶𝑫𝑨 𝑵𝑭𝑻 𝑴𝑬 𝑴𝑰𝑵𝑻 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑨 𝑶𝑵𝑳𝒀𝑭𝑨𝑵𝑺 𝑳𝑰𝑽𝑬 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑶 𝒁𝑰𝑷 𝑭𝑰𝑳𝑬 𝑴𝑬 𝑪𝑶𝑴𝑷𝑹𝑬𝑺𝑺 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",
    "𝑻𝑬𝑹𝑬 𝑫𝑨𝑫𝑨 𝑲𝑬 𝑩𝑯𝑶𝑺𝑫𝑬 𝑴𝑬 𝑷𝒀𝑻𝑯𝑶𝑵 𝑹𝑼𝑵 𝑲𝑨𝑹 𝑫𝑼𝑵𝑮𝑨",


    # Yaha apni lines add karo
]

spam_running = {}

# =============== ALIVE ===============

@app.on_message(filters.command("alive", prefixes=".") & filters.user(SUDO_USERS))
async def alive(_, message):
    await message.reply_text("MAA CHODNE KE LIYE READY")

# =============== PING ===============

@app.on_message(filters.command("ping", prefixes=".") & filters.user(SUDO_USERS))
async def ping(_, message):
    start = time.time()
    msg = await message.reply_text("Pinging...")
    end = time.time()

    ms = round((end - start) * 1000, 2)
    await msg.edit_text(f"PONG ⚡\n{ms} ms")

# =============== SPEED ===============

@app.on_message(filters.command("speed", prefixes=".") & filters.user(SUDO_USERS))
async def speed(_, message):
    await message.reply_text("SUPER FAST")

# =============== C COMMAND ===============

@app.on_message(filters.regex(r"^\.c(?:\s+\d+)?$") & filters.user(SUDO_USERS))
async def custom_mention(_, message):

    if not message.reply_to_message:
        return await message.reply_text("SIR KIS KI GAND KA KIDA NIKALWANA HAI TAG KARO")

    target = message.reply_to_message.from_user

    count = 1
    parts = message.text.split()

    if len(parts) > 1:
        try:
            count = int(parts[1])
        except:
            count = 1

    chat_id = message.chat.id
    spam_running[chat_id] = True

    for _ in range(count):

        if not spam_running.get(chat_id):
            break

        mention = target.mention

        line = CUSTOM_LINES[_ % len(CUSTOM_LINES)]

        await app.send_message(
            chat_id,
            f"{mention}\n{line}"
        )

        await asyncio.sleep(1)

# =============== STOPC ===============

@app.on_message(filters.command("stopc", prefixes=".") & filters.user(SUDO_USERS))
async def stop_custom(_, message):

    spam_running[message.chat.id] = False

    await message.reply_text(
        "GAND MAR LIYA MADARCHOD KA"
    )

# =============== START ===============

print("Bot Started...")
app.run()
