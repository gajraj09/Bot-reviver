# server_b.py
from flask import Flask
import threading
import requests
import time

app = Flask(__name__)

@app.route("/ping")
def ping():
    print("✅ Server B received ping")
    return {"status": "B alive"}, 200

def ping_server_a():
    target_url = "https://server-a.onrender.com/ping"  # Replace with actual Server A URL

    while True:
        success = False
        for attempt in range(10):  # Retry up to 3 times
            try:
                response = requests.get(target_url, timeout=5)
                if response.status_code == 200:
                    print("✅ Server B pinged Server A")
                    success = True
                    break
            except Exception as e:
                print(f"⚠️ Server B ping attempt {attempt+1} failed: {e}")
                time.sleep(2)

        if not success:
            print("❌ Server B failed to ping Server A after 3 attempts")

        time.sleep(300)  # 5 minutes

# Start background pinger
threading.Thread(target=ping_server_a, daemon=True).start()

if __name__ == "__main__":
    app.run()
