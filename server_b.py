from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

@app.route("/ping")
def ping():
    print("✅ Server B received ping")
    return {"status": "Server B alive"}, 200

def ping_server_a():
    while True:
        try:
            res = requests.get("https://binance-webhook-55an.onrender.com/ping", timeout=5)
            if res.status_code == 200:
                print("✅ Pinged Server A")
        except Exception as e:
            print("⚠️ Ping failed:", e)
        time.sleep(300)

threading.Thread(target=ping_server_a, daemon=True).start()

if __name__ == "__main__":
    app.run()
