import requests, json

# Define the URL of your Flask application
url = 'http://localhost:5000/predict'

# Define the data to be sent in the POST request
data = {'tokenized': 'this is the data'}

# Set the headers to specify that the data is in JSON format
headers = {'Content-Type': 'application/json'}

# Send the POST request
response = requests.post(url, json=data, headers=headers)

# Print the response from the server
print(response.json())
