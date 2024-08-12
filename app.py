from flask import Flask, jsonify
import requests

app = Flask(__name__)

# In-memory storage for processed data
processed_data_storage = {}

# Function to fetch data from the mock API
def fetch_mock_data():
    url = "https://mock.shop/api"
    query = '''
    {
      products(first: 20) {
        edges {
          node {
            id
            title
            description
            featuredImage {
              id
              url
            }
            variants(first: 3) {
              edges {
                node {
                  price {
                    amount
                    currencyCode
                  }
                }
              }
            }
          }
        }
      }
    }
    '''
    response = requests.get(url, params={'query': query})
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

# Function to process the fetched data
def process_data(data):
    # Example transformation: converting product titles to uppercase
    for product in data['data']['products']['edges']:
        product['node']['title'] = product['node']['title'].upper()

    # Example transformation: summing up all prices for each product's variants
    for product in data['data']['products']['edges']:
        total_price = sum(
            float(variant['node']['price']['amount']) for variant in product['node']['variants']['edges']
        )
        product['node']['total_price'] = {
            "amount": total_price,
            "currencyCode": product['node']['variants']['edges'][0]['node']['price']['currencyCode']
        }

    return data

# API endpoint to fetch and process data
@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    raw_data = fetch_mock_data()
    if "error" in raw_data:
        return jsonify(raw_data), 500
    
    processed_data = process_data(raw_data)

    # Store the processed data in memory
    processed_data_storage["processed_data"] = processed_data

    return jsonify({"message": "Data fetched and processed successfully"})

# API endpoint to retrieve processed data
@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    if "processed_data" in processed_data_storage:
        return jsonify(processed_data_storage["processed_data"])
    else:
        return jsonify({"message": "No processed data found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

