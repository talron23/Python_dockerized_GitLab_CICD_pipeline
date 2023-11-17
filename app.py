from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_joke', methods=['GET'])
def get_joke():
    joke_api_url = 'https://official-joke-api.appspot.com/jokes/random'
    response = requests.get(joke_api_url)

    if response.status_code == 200:
        joke_data = response.json()

        # Print the response for debugging
        print("API Response:", joke_data)

        # Check if 'setup' and 'punchline' keys exist in the response
        if 'setup' in joke_data and 'punchline' in joke_data:
            return jsonify({'joke': joke_data['setup'], 'punchline': joke_data['punchline']})
        else:
            return jsonify({'error': 'Invalid joke format from the external API'}), 500

    else:
        return jsonify({'error': f'Failed to fetch joke. Status code: {response.status_code}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)