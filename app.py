from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
openai.api_key = 'YOUR-OPENAI-API-KEY'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['POST'])
def api():
     message = request.form.get("message")

       
     completion = openai.ChatCompletion.create(
     model="gpt-3.5-turbo",
     messages=[
        {"role": "user", "content": message}
     ]
     )
     print("Chat response:", completion.choices[0].message.content)
     return jsonify({"message": completion.choices[0].message['content']})
     

if __name__ == '__main__':
    app.run()


 