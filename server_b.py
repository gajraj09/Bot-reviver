from flask import Flask, jsonify
import threading
import requests
import time
import os

app = Flask(__name__)

# Single server to keep alive
TARGET_URL = "https://ethusdc-longonly.onrender.com/ping"

PING_INTERVAL = int(os.environ.get("PING_INTERVAL", 300))  # default 5 minutes


@app.route("/ping")
def ping():
    """Health check for the reviver itself."""
    return jsonify({"status": "reviver alive"}), 200


def keep_alive():
    """Background task to keep the target server alive by pinging it."""
    while True:
        success = False
        for attempt in range(3):  # retry up to 3 times
            try:
                response = requests.get(TARGET_URL, timeout=5)
                if response.status_code == 200:
                    print(f"✅ Successfully pinged {TARGET_URL}")
                    success = True
                    break
            except Exception as e:
                print(f"⚠️ Ping attempt {attempt+1} to {TARGET_URL} failed: {e}")
                time.sleep(2)  # wait before retry

        if not success:
            print(f"❌ Failed to ping {TARGET_URL} after 3 attempts")

        time.sleep(PING_INTERVAL)


if __name__ == "__main__":
    # Start background thread only once
    threading.Thread(target=keep_alive, daemon=True).start()

    # Render provides PORT env variable
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)


# from flask import Flask, jsonify
# import threading
# import requests
# import time
# import os

# app = Flask(__name__)

# # List of servers that need to be kept alive
# TARGETS = [
#     "https://ethusdc-longonly.onrender.com",
#     # "https://binance-65gz.onrender.com/ping",
#     # "https://chartify-ethusdc.onrender.com/ping",
#     # "https://ethusdc-15min-unrepeat.onrender.com/ping",
#     # "https://chartify-webhook.onrender.com/ping",
#     # "https://chartify-ovem.onrender.com/ping",
#     # "https://chartinger.onrender.com/ping"
# ]

# PING_INTERVAL = int(os.environ.get("PING_INTERVAL", 300))  # default 5 minutes


# @app.route("/ping")
# def ping():
#     """Health check for the reviver itself."""
#     return jsonify({"status": "reviver alive"}), 200


# def keep_alive():
#     while True:
#         for url in TARGETS:
#             success = False
#             for attempt in range(3):  # retry up to 3 times
#                 try:
#                     response = requests.get(url, timeout=5)
#                     if response.status_code == 200:
#                         print(f"✅ Successfully pinged {url}")
#                         success = True
#                         break
#                 except Exception as e:
#                     print(f"⚠️ Ping attempt {attempt+1} to {url} failed: {e}")
#                     time.sleep(2)  # wait before retry

#             if not success:
#                 print(f"❌ Failed to ping {url} after 3 attempts")

#         time.sleep(PING_INTERVAL)


# # Start background thread
# threading.Thread(target=keep_alive, daemon=True).start()

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 10000))  # Render injects PORT env variable
#     app.run(host="0.0.0.0", port=port)



# from flask import Flask
# import threading
# import requests
# import time
# import os

# app = Flask(__name__)

# @app.route("/ping")
# def ping():
#     print("✅ Server B received ping")
#     return {"status": "B alive"}, 200

# def ping_server_a():
#     target_url = os.environ.get("PING_URL", "https://binance-65gz.onrender.com/ping")  # Replace with your actual Server A URL

#     while True:
#         success = False
#         for attempt in range(3):  # Retry up to 3 times
#             try:
#                 response = requests.get(target_url, timeout=5)
#                 if response.status_code == 200:
#                     def ping_webhook_modifier()
#                     print("✅ Server B pinged Server A")
#                     success = True
#                     break
#             except Exception as e:
#                 print(f"⚠️ Server B ping attempt {attempt+1} failed: {e}")
#                 time.sleep(2)  # Wait 2 seconds before retrying

#         if not success:
#             print("❌ Server B failed to ping Server A after 3 attempts")

#         time.sleep(300)  # Wait 5 minutes before next cycle

# def ping_webhook_modifier():
#     target_url = os.environ.get("PING_URL", "https://binance-65gz.onrender.com/ping")  # Replace with your actual Server A URL

#     while True:
#         success = False
#         for attempt in range(3):  # Retry up to 3 times
#             try:
#                 response = requests.get(target_url, timeout=5)
#                 if response.status_code == 200:
#                     print("✅ Server B pinged Server A")
#                     success = True
#                     break
#             except Exception as e:
#                 print(f"⚠️ Server B ping attempt {attempt+1} failed: {e}")
#                 time.sleep(2)  # Wait 2 seconds before retrying

#         if not success:
#             print("❌ Server B failed to ping Server A after 3 attempts"

# # Start ping thread
# threading.Thread(target=ping_server_a, daemon=True).start()

# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 10000))  # Use Render's injected PORT env variable
#     app.run(host="0.0.0.0", port=port)
