import requests
from bs4 import BeautifulSoup

def get_powerball_jackpot():
    # URL of the website containing Powerball jackpot information
    url = "https://www.powerball.com/"

    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the website
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the element containing the jackpot information
        jackpot_element = soup.find('div', class_='game-detail-group')
        
        # Extract the jackpot amount
        jackpot_amount = jackpot_element.find('span', class_='game-jackpot-number').text.strip()

        # Print the jackpot amount
        print("Latest Powerball Jackpot:", jackpot_amount)
    else:
        print("Failed to retrieve Powerball jackpot information.")

# Call the function to get the latest Powerball jackpot
get_powerball_jackpot()

