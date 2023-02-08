import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "vgGji38lr2_id_a_TgweMiDi99F5T9DMjE2U1cmX1IwY"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["cab_type ","destination","source","product_id","name"]], "values": [[1,2,3,4,5]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/727091a4-32cc-4d3c-ba9a-b2f008e674c3/predictions?version=2023-02-07', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions=response_scoring.json()
print("The Prediction is ")
print(predictions['predictions'][0]['values'][0][0])