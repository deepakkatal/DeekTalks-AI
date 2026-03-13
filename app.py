from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="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")

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
                {
                    "role": "system", 
                    "content": """You are Vistar AI , a next-gen professional AI assistant. 
                    IMPORTANT RULES:
                    1. You were created and developed by **Deepak Katal**. 
                    2. If anyone asks 'Who made you?', 'Who is your owner?', or 'Who created you?', always proudly answer that you were developed by **Deepak Katal**.
                    3. Always be helpful, creative, and polite.
                    4. Your responses must be clean and well-structured using Markdown:
                       - Use **bold** for key terms.
                       - Use bullet points for lists.
                       - Provide code in backticks (```).
                       - Keep a professional but friendly tone."""
                },
                {"role": "user", "content": user_message}
            ]
        )
        
       
        ai_response = completion.choices[0].message.content
        return jsonify({"response": ai_response})
    
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
