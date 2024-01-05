import requests
import csv
from bs4 import BeautifulSoup

# URL for the website that will be scraped
url = "https://www.swiggy.com/city/mumbai/best-restaurants"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

try:
    # test get request 
    response = requests.get(url, headers=headers)   
    response.raise_for_status() 
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # List of elements that hold restaurants
        restaurants = soup.find_all('div', class_="styled__StyledRestaurantGridCard-sc-fcg6mi-0 lgOeYp")
        
        # Open a csv file to store restaurant data
        csv_file = open('restaurants.csv', 'w')
        writer = csv.writer(csv_file) 
        writer.writerow(["Name", "Rating", "Cuisine", "Location"]) 

        for restaurant in restaurants:
            # find the name of the restaurant 
            name = restaurant.find('div', class_='sc-beySbM cwvucc').text

            # find the rating and clean it
            rating = restaurant.find('span', class_='sc-beySbM evFhcR').text
            rating = float(rating[0:-2])

            # find the cuisine and location of the restaurant
            locationAndCuisine = restaurant.find_all('div', class_='sc-beySbM iTWFZi')
            cuisine = locationAndCuisine[0].text
            location = locationAndCuisine[1].text

            # write data to file 
            writer.writerow([name, rating, cuisine, location])

        # close the file
        csv_file.close()
    else:
        print('Webpage retrieval failed with Status Code: ' + response.status_code)

except requests.exceptions.HTTPError as errh:
    print("Error! " + errh + " occured!")





