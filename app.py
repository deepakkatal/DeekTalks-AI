from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

# अपनी API Key यहाँ लिखें
client = Groq(api_key="PASTE_YOUR_KEY_HERE")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message")
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are Vistar AI, developed by Deepak Katal. Be professional."},
                {"role": "user", "content": user_message}
            ]
        )
        return jsonify({"response": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
