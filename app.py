from flask import Flask, render_template, request, jsonify
import openai
import stripe
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'supersecretkey')

openai.api_key = os.environ.get('OPENAI_API_KEY')
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': user_msg}]
        )
        reply = response['choices'][0]['message']['content']
    except Exception as e:
        reply = f"Error: {str(e)}"
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run()
