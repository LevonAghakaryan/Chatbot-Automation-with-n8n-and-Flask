import requests
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

chat_messages = []

# Քո n8n webhook URL-ը
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/product/chat")
def chat_page():
    return render_template("chat.html")


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    user_message = data.get("user_message") # Փոխված է այստեղ

    if not user_message:
        return jsonify({"status": "error", "message": "Հաղորդագրություն չկա"}), 400

    # Ավելացնում ենք օգտատիրոջ հաղորդագրությունը
    chat_messages.append({"sender": "user", "text": user_message})

    bot_response_text = "🤖 Սխալ..."

    try:
        print(f"Ուղարկում եմ n8n: {user_message}")

        # POST request n8n-ին
        response = requests.post(
            N8N_WEBHOOK_URL,
            json={"user_message": user_message},
            headers={'Content-Type': 'application/json'},
            timeout=10
        )

        print(f"n8n կոդ: {response.status_code}")
        print(f"n8n պատասխան: {response.text}")

        if response.status_code == 200:
            # Ստուգում ենք՝ JSON է թե ոչ
            content_type = response.headers.get('content-type', '')

            if 'application/json' in content_type:
                try:
                    bot_data = response.json()
                    bot_response_text = bot_data.get("reply", "🤖 Պատասխան չկա")
                except json.JSONDecodeError:
                    bot_response_text = f"🤖 JSON սխալ: {response.text[:100]}"
            else:
                # Եթե JSON չէ, ցույց տալ պատասխանի տեքստը
                bot_response_text = f"🤖 n8n պատասխան (ոչ JSON): {response.text[:200]}"
        else:
            bot_response_text = f"🤖 HTTP սխալ {response.status_code}: {response.text[:100]}"

    except requests.exceptions.ConnectionError:
        bot_response_text = "🤖 n8n-ին կապ չկա։ Ստուգիր՝ n8n գործում է?"
    except requests.exceptions.Timeout:
        bot_response_text = "🤖 n8n ժամանակը սպառվեց"
    except Exception as e:
        bot_response_text = f"🤖 Անհայտ սխալ: {str(e)}"

    # Ավելացնում ենք բոտի պատասխանը
    chat_messages.append({"sender": "bot", "text": bot_response_text})

    return jsonify({"status": "ok"})


@app.route("/get_messages")
def get_messages():
    return jsonify(chat_messages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
