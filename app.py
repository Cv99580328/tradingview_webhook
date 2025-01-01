from flask import Flask, request, jsonify

app = Flask(__name__)

# テスト用のルート
@app.route("/", methods=["GET"])
def home():
    return "Webhook is running!", 200

# Webhookエンドポイントの例
@app.route("/alert-hook", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return jsonify({"error": "No data received"}), 400

    # ここで受信したデータを処理する（例: ログ出力）
    print(f"Received data: {data}")
    return jsonify({"status": "success", "message": "Data received"}), 200

# Flaskアプリケーションの起動設定
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
