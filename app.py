# Importing required libraries
from functools import cache
import requests
from retry import retry
from flask import Flask


app = Flask(__name__)

# Function to fetch the results from isEven API
@cache # Cache the results to avoid overwhelming the server
@retry(ConnectionError, tries=3, delay=2) # Retry in case of failure
def is_even(number):

    # Fetch the result
    r = requests.get(
        f"https://api.isevenapi.xyz/api/iseven/{number}/"
        )
    
    even_json = r.json()

    return even_json

# Function for the isOdd API
@app.route('/api/isodd/<number>/')
def is_odd(number):

    # Get the is_even results
    even_json = is_even(number)

    # Pass on the error message
    if "error" in even_json:

        # Replace isEven with isOdd when free usage limits are exceeded
        # to nudge users to upgrade to Premium or Enterprise
        even_json["error"] = even_json["error"].replace("isEven", "isOdd")

        return even_json
    
    else:

        # Instantiate an empty dictionary
        odd_json = {}

        # Replace isEven with isOdd when ad tries to upsell isEven
        odd_json["ad"] = even_json["ad"].replace("isEven", "isOdd")

        # Revert the result
        odd_json["isodd"] = not even_json["iseven"]

        return odd_json

# Run the api
app.run(host='127.0.0.1', port=5000)