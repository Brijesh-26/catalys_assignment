from flask import Flask, jsonify
import json

app = Flask(__name__)

# In-memory storage for processed data
data_storage = {}

# Mock data simulating external service response
mock_data = [
    {"id": 1, "name": "item one", "value": 100},
    {"id": 2, "name": "item two", "value": 200},
    {"id": 3, "name": "item three", "value": 300},
]

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    """
    Simulate fetching data from an external service.
    For this example, it returns mock data.
    """
    return jsonify(mock_data)

@app.route('/process-data', methods=['GET'])
def process_data():
    """
    Process the fetched data. For this example, it converts all 'name' values to uppercase
    and sums up the 'value' fields.
    """
    processed_data = []
    total_value = 0

    for item in mock_data:
        processed_item = {
            "id": item["id"],
            "name": item["name"].upper(),
            "value": item["value"]
        }
        processed_data.append(processed_item)
        total_value += item["value"]
    
    # Store processed data in memory
    data_storage['processed_data'] = {
        "items": processed_data,
        "total_value": total_value
    }
    
    return jsonify({"message": "Data processed successfully"})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    """
    Return the processed data stored in memory.
    """
    return jsonify(data_storage.get('processed_data', {}))

if __name__ == '__main__':
    app.run(debug=True)
