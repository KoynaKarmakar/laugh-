from flask import Flask, jsonify
from flask_cors import CORS
import json
import random
import os

# Initialize Flask app
app = Flask(__name__)

# Enable CORS - allows frontend (Vercel) to make requests to this backend
CORS(app)

# Global variable to store jokes
jokes_list = []

def load_jokes():
    """
    Load jokes from jokes.json file
    Returns True if successful, False otherwise
    """
    global jokes_list
    try:
        # Get the directory where app.py is located
        base_dir = os.path.dirname(os.path.abspath(__file__))
        jokes_file = os.path.join(base_dir, 'jokes.json')
        
        # Open and read the jokes file
        with open(jokes_file, 'r', encoding='utf-8') as file:
            data = json.load(file)
            jokes_list = data.get('jokes', [])
            
        print(f"✓ Loaded {len(jokes_list)} jokes successfully")
        return True
        
    except FileNotFoundError:
        print("✗ Error: jokes.json file not found")
        return False
    except json.JSONDecodeError:
        print("✗ Error: jokes.json is not valid JSON")
        return False
    except Exception as e:
        print(f"✗ Error loading jokes: {str(e)}")
        return False

# Load jokes when app starts
load_jokes()

# Route 1: Root endpoint - status check
@app.route('/', methods=['GET'])
def home():
    """
    Root endpoint to verify backend is running
    """
    return jsonify({
        "message": "Laugh() backend is running",
        "total_jokes": len(jokes_list)
    }), 200

# Route 2: Get random joke
@app.route('/joke', methods=['GET'])
def get_joke():
    """
    Returns a random joke from the jokes list
    """
    # Check if jokes are loaded
    if not jokes_list:
        return jsonify({
            "error": "No jokes available"
        }), 500
    
    # Select and return a random joke
    random_joke = random.choice(jokes_list)
    
    return jsonify({
        "joke": random_joke
    }), 200

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "error": "Endpoint not found"
    }), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "error": "Internal server error"
    }), 500

# Run the app
if __name__ == '__main__':
    # Production: Set debug=False
    # Development: Can set debug=True for auto-reload
    app.run(host='0.0.0.0', port=5001, debug=False)