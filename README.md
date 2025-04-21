# Capital Time API

## Description
This Flask-based API returns the current local time and UTC offset for selected capital cities. It uses the TimeZoneDB (https://timezonedb.com) API and requires a token for access.

## Authorization Token
You must include a token to call the API.

Your token: mysecuretoken123

## Endpoint
GET /time

### Query Parameters:
- city: Name of a capital city (e.g., London, Tokyo)
- token: Your API token (e.g., mysecuretoken123)

## Example Call

URL:
http://127.0.0.1:5000/time?city=London&token=mysecuretoken123

### Sample Response:
{
  "city": "London",
  "local_time": "2025-04-21 18:24:59",
  "utc_offset": 3600
}

## Error Examples

Invalid Token:
{
  "error": "Unauthorized access. Valid token required."
}

City Not Found:
{
  "error": "City 'Madrid' not found in our database."
}

## Setup

1. Clone this repo:
   git clone https://github.com/YOUR_USERNAME/capital-time-api.git
   cd capital-time-api

2. Install requirements:
   pip install -r requirements.txt

3. Run the app:
   python app.py

4. Access the API via browser or curl using:
   http://127.0.0.1:5000/time?city=London&token=mysecuretoken123
