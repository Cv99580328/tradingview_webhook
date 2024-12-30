from flask import Flask, request, jsonify  # 必要なモジュールをインポート

# Flaskアプリケーションを作成
app = Flask(__name__)

# ルートエンドポイント（ホームページ）
@app.route('/')
def home():
    return "Hello, Flask!"

# Webhookエンドポイントを追加
@app.route('/webhook', methods=['POST'])
def webhook():
    # TradingViewからのJSONデータを取得
    data = request.json  # リクエストからJSONデータを受け取る
    print(f"Received webhook data: {data}")  # ターミナルにデータを表示
    # レスポンスを返す
    return jsonify({"message": "Webhook received!"}), 200

# アプリケーションを起動
if __name__ == '__main__':
    app.run(debug=True)
