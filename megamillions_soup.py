import requests
from bs4 import BeautifulSoup

def get_megamillions_jackpot():
    # URL of the website containing Mega Millions jackpot information
    url = "https://www.megamillions.com/"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the element containing the jackpot information
        jackpot_element = soup.find('div', class_='nextEstGroup')

        # Extract the jackpot amount
        jackpot_amount = jackpot_element.text.strip()

        # Print the jackpot amount
        print("Latest Mega Millions Jackpot:", jackpot_amount)
    else:
        print("Failed to retrieve Mega Millions jackpot information.")

# Call the function to get the latest Mega Millions jackpot
get_megamillions_jackpot()

