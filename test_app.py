import unittest
from flask import Flask, jsonify
from flask_testing import TestCase
from unittest.mock import patch
from app import app

class TestApp(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    @patch('app.requests.get')
    def test_get_joke_success(self, mock_get):
        # Mock the external API response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'setup': 'Test setup', 'punchline': 'Test punchline'}

        # Make a request to the testing route
        response = self.client.get('/get_joke')

        # Assert the response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'joke': 'Test setup', 'punchline': 'Test punchline'})

    @patch('app.requests.get')
    def test_get_joke_failure(self, mock_get):
        # Mock the external API response
        mock_get.return_value.status_code = 500

        # Make a request to the testing route
        response = self.client.get('/get_joke')

        # Assert the response
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {'error': 'Failed to fetch joke. Status code: 500'})

if __name__ == '__main__':
    unittest.main()
