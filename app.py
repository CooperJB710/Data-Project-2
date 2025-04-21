from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# TOKEN REQUIRED to access the API
AUTHORIZED_TOKEN = "mysecuretoken123"

# Your TimeZoneDB API Key (register for free at timezonedb.com)
TIMEZONEDB_API_KEY = "H2EDV9AGVMH5"

# Dictionary mapping capital cities to their time zones
CAPITAL_TIMEZONES = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Paris": "Europe/Paris",
    "Canberra": "Australia/Sydney",
    "Ottawa": "America/Toronto",
    "Beijing": "Asia/Shanghai",
    "New Delhi": "Asia/Kolkata",
    "Brasília": "America/Sao_Paulo"
}

# API endpoint: /time
# Test it like this: http://127.0.0.1:5000/time?city=London&token=mysecuretoken123
@app.route("/time", methods=["GET"])
def get_time():
    # Get token and city from query parameters
    token = request.args.get("token")
    city = request.args.get("city")

    # Validate token
    if token != AUTHORIZED_TOKEN:
        return jsonify({"error": "Unauthorized access. Valid token required."}), 403

    # Validate city parameter
    if not city:
        return jsonify({"error": "Missing city parameter."}), 400

    timezone = CAPITAL_TIMEZONES.get(city)
    if not timezone:
        return jsonify({"error": f"City '{city}' not found in our database."}), 404

    # Query TimeZoneDB for the current time
    api_url = f"http://api.timezonedb.com/v2.1/get-time-zone?key={TIMEZONEDB_API_KEY}&format=json&by=zone&zone={timezone}"

    try:
        response = requests.get(api_url)
        data = response.json()

        if data['status'] != 'OK':
            return jsonify({"error": "Failed to retrieve time from API", "details": data.get('message', 'Unknown error')}), 500

        return jsonify({
            "city": city,
            "local_time": data["formatted"],
            "utc_offset": data["gmtOffset"]
        })
    except Exception as e:
        return jsonify({"error": "Failed to retrieve time from API", "details": str(e)}), 500

# Start Flask server on all IPs at port 5000
# To test locally, go to: http://127.0.0.1:5000/time?city=London&token=mysecuretoken123
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
