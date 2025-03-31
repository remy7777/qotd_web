from flask import Flask, render_template
import json
import random
from pathlib import Path
from datetime import datetime

app = Flask(__name__)

# Global variables to store the daily quote
daily_quote = None
last_updated = None

def get_random_quote():
    """Loads quotes from file and selects a random one."""
    quotes_path = Path(__file__).parent / "quotes.json"
    with open(quotes_path, 'r') as file:
        quotes = json.load(file)
    return random.choice(quotes)

def get_daily_quote():
    """Returns the same quote for a whole day, changing at midnight."""
    global daily_quote, last_updated
    
    today = datetime.now().date()
    
    # If it's a new day or first-time load, pick a new quote
    if last_updated != today:
        daily_quote = get_random_quote()
        last_updated = today  # Update last stored date
    
    return daily_quote

@app.route('/')
def home():
    quote = get_daily_quote()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=80)
