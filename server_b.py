
from flask import Flask
import threading
import requests
import time
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    print("✅ Server B received ping")
    return {"status": "B alive"}, 200

def ping_server_a():
    target_url = os.environ.get("PING_URL", "https://binance-65gz.onrender.com/ping")  # Replace with your actual Server A URL

    while True:
        success = False
        for attempt in range(3):  # Retry up to 3 times
            try:
                response = requests.get(target_url, timeout=5)
                if response.status_code == 200:
                    print("✅ Server B pinged Server A")
                    success = True
                    break
            except Exception as e:
                print(f"⚠️ Server B ping attempt {attempt+1} failed: {e}")
                time.sleep(2)  # Wait 2 seconds before retrying

        if not success:
            print("❌ Server B failed to ping Server A after 3 attempts")

        time.sleep(300)  # Wait 5 minutes before next cycle

# Start ping thread
threading.Thread(target=ping_server_a, daemon=True).start()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Use Render's injected PORT env variable
    app.run(host="0.0.0.0", port=port)
