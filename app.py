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


# from flask import Flask, render_template, request, jsonify
# from groq import Groq
# import os

# app = Flask(__name__)

# # अपनी API Key यहाँ डालें
# client = Groq(api_key="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")

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat_page')
# def chat_page():
#     return render_template('Personal_ai/chat.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         user_message = request.json.get("message")
        
#         # यहाँ हमने AI को उसकी पहचान (Identity) दी है
#         completion = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {
#                     "role": "system", 
#                     "content": """You are Vistar AI, a next-gen professional AI assistant. 
#                     STRICT RULES:
#                     1. You were created and developed by **Deepak Katal**. 
#                     2. If anyone asks 'Who made you?', 'Who is your creator?', or 'Who developed you?', always answer that you were developed by **Deepak Katal**.
#                     3. Always be helpful, creative, and polite.
#                     4. Use Markdown: **bold** for keys, bullet points, and code blocks."""
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
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)

# from flask import Flask, render_template, request, jsonify
# from groq import Groq
# import os

# app = Flask(__name__)

# # Apni API Key yahan dalein ya environment variable use karein
# # client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
# client = Groq(api_key="api_key")

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/chat_page')
# def chat_page():
#     return render_template('Personal_ai/chat.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     try:
#         user_message = request.json.get("message")
        
#         # AI Identity configuration with Social Links
#         completion = client.chat.completions.create(
#             model="llama-3.3-70b-versatile",
#             messages=[
#                 {
#                     "role": "system", 
#                     "content": """You are Vistar AI, a next-gen professional AI assistant. 
#                     STRICT RULES:
#                     1. If anyone asks 'Who made you?', 'Who is your creator?', or 'Who developed you?', you must answer exactly like this:
#                        "I was developed by **Deepak Katal**. You can connect with him here:
#                        - **LinkedIn**: [Deepak Katal](www.linkedin.com/in/deepak-katal-796029305)
#                        - **Instagram**: [dkarts_007](https://www.instagram.com/dkarts_007/)"
#                     2. Always be helpful, creative, and polite.
#                     3. Use Markdown: **bold** for keys, bullet points, and code blocks.
#                     4. You can communicate in both Hindi and English based on the user's language."""
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
#     # Port 5500 set kiya hai jaisa aapne pehle pucha tha
#     port = int(os.environ.get("PORT", 5500))
#     app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask, render_template, request, jsonify
from groq import Groq
import os

app = Flask(__name__)

client = Groq(api_key="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")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat_page')
def chat_page():
    return render_template('Personal_ai/chat.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_message = request.json.get("message")

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
You are Vistar AI, a professional AI assistant.

Rules:
1. Always respond in clean markdown format.
2. Use headings and bullet points when needed.
3. Keep answers structured and readable.
4. Avoid messy formatting.

If someone asks who created you respond exactly:

I was developed by **Deepak Katal**.

### Connect with him

- **LinkedIn**  
www.linkedin.com/in/deepak-katal-796029305

- **Instagram**  
https://www.instagram.com/dkarts_007/
"""
                },
                {"role": "user", "content": user_message}
            ]
        )

        ai_response = completion.choices[0].message.content

        return jsonify({"response": ai_response})

    except Exception as e:
        print(e)
        return jsonify({"response": "⚠️ AI error occurred"})


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5500))
    app.run(host='0.0.0.0', port=port, debug=True)
