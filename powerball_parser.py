import http.client
import json

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 5wP44Zxy7irccurw0YJsxy:5FyeP2cvsXmk9ZCCvp9dK6"
}

try:
    conn.request("GET", "/chancegame/usaPowerball", headers=headers)
    res = conn.getresponse()
    data = res.read()
    
    # Parse JSON response
    json_data = json.loads(data.decode("utf-8"))
    
    # First, let's see the full JSON structure
#   print("Full API Response:")
#   print(json.dumps(json_data, indent=2))
#   print("\n" + "="*50 + "\n")
    
    # Try to extract jackpot amount from common field names
    jackpot = None
    
    if json_data.get("success") and "result" in json_data:
        result = json_data["result"]
        
        # Check various possible field names for jackpot
        possible_fields = ["next_jackpot", "jackpot", "nextJackpot", "jackpot_amount", "amount", "prize"]
        
        for field in possible_fields:
            if field in result:
                jackpot = result[field]
#               print(f"Found jackpot in field '{field}': {jackpot}")
                break
        
        if not jackpot:
            print("Jackpot field not found. Available fields in result:")
            print(list(result.keys()))
    else:
        print("API call was not successful or no 'result' field found")
        if "message" in json_data:
            print(f"API Message: {json_data['message']}")
    
    if jackpot:
        print(f"\nNext Powerball Jackpot: {jackpot}")
    else:
        print("\nUnable to extract jackpot amount")
        
except json.JSONDecodeError:
    print("Error: Unable to parse JSON response")
    print("Raw response:", data.decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
