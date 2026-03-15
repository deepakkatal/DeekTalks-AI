# from flask import Flask, render_template, request, jsonify
# from groq import Groq

# app = Flask(__name__)

# client = Groq(api_key="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")

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         user_message = request.json.get("message")
        
     
#         completion = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {
#                     "role": "system", 
#                     "content": """You are Vistar AI , a next-gen professional AI assistant. 
#                     IMPORTANT RULES:
#                     1. You were created and developed by **Deepak Katal**. 
#                     2. If anyone asks 'Who made you?', 'Who is your owner?', or 'Who created you?', always proudly answer that you were developed by **Deepak Katal**.
#                     3. Always be helpful, creative, and polite.
#                     4. Your responses must be clean and well-structured using Markdown:
#                        - Use **bold** for key terms.
#                        - Use bullet points for lists.
#                        - Provide code in backticks (```).
#                        - Keep a professional but friendly tone."""
#                 },
#                 {"role": "user", "content": user_message}
#             ]
#         )
        
       
#         ai_response = completion.choices[0].message.content
#         return jsonify({"response": ai_response})
    
#     except Exception as e:
#         print(f"Error: {e}")
#         return jsonify({"error": str(e)}), 500

# if __name__ == '__main__':



from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

# अपनी Groq API Key यहाँ डालें
client = Groq(api_key="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")

# 1. लैंडिंग पेज का रास्ता (Route)
@app.route('/')
def landing_page():
    # यह 'templates/index.html' को लोड करेगा (नया वाला लैंडिंग पेज)
    return render_template('index.html')

# 2. चैट पेज का रास्ता (Route)
@app.route('/chat_page')
def chat_page():
    # यह 'templates/Personal_ai/chat.html' को लोड करेगा
    return render_template('Personal_ai/chat.html')

# 3. AI चैट का Logic (Backend API)
@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message")
        
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": """You are Vistar AI, a next-gen professional AI assistant. 
                    IMPORTANT RULES:
                    1. You were created and developed by **Deepak Katal**. 
                    2. If anyone asks 'Who made you?', always answer you were developed by **Deepak Katal**.
                    3. Always be helpful, creative, and polite.
                    4. Use Markdown: **bold**, bullet points, and code blocks (```)."""
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

