import requests
API_KEY = "a1450b56fa14a82f77d708b098d40d9a9a7894a49b42bfb7eb8b94d5346e3f31"

bitcoin = float(input("How many bitcoins do you want to buy?"))
 
response = requests.get("http://rest.coincap.io/v3/assets/bitcoin?apiKey="+API_KEY)
bitcoin_price = float(response.json()["data"]["priceUsd"])
total = round(bitcoin * bitcoin_price, 2)
print(f"Your total will be: ${total:,.2f}")