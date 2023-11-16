from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/get_joke', methods=['GET'])
def get_joke():
    joke_api_url = 'https://official-joke-api.appspot.com/jokes/random'
    response = requests.get(joke_api_url)

    if response.status_code == 200:
        joke_data = response.json()
        return jsonify({'joke': joke_data['setup'], 'punchline': joke_data['delivery']})
    else:
        return jsonify({'error': 'Failed to fetch joke'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
