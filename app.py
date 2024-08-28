# Imports
import requests
from functools import cache
from retry import retry

from flask import Flask
app = Flask(__name__)

# Function to fetch the results from isEven API
@cache # Cache the results to avoid overwhelming the server
@retry(ConnectionError, tries=3, delay=2) # Retry
def is_even(number):

    # Fetch the result
    r = requests.get(
        f"https://api.isevenapi.xyz/api/iseven/{number}/"
        )
    
    even_json = r.json()

    return even_json

@app.route('/api/isodd/<number>/')
def is_odd(number):

    even_json = is_even(number)

    if "error" in even_json:

        even_json["error"] = even_json["error"].replace("isEven", "isOdd")

        return even_json
    
    else:

        odd_json = {}

        odd_json["ad"] = even_json["ad"].replace("isEven", "isOdd")

        odd_json["isodd"] = not even_json["iseven"]

        return odd_json

app.run()