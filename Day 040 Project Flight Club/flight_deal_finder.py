import data_manager
import flight_search
import flight_data
import notification_manager

data_manager = data_manager.DataManager()
flight_search = flight_search.FlightSearch()
flight_data = flight_data.FlightData()
notification = notification_manager.NotificationManager()

print("Welcome to Flight's Club.")
print("We will track the best flight deals for you and send it in an email")
name = input("What is your first name?\n")
last_name = input("What is your last name?\n")
email = input("What is your email?\n")
email_confirm = input("type your email again\n")

if email == email_confirm:
    data_manager.add_in_user_database(name, last_name, email)
else:
    print("Different emails, could not add to user database")

# For each city in the data file get IATA code and price to search for flight
for city in data_manager.deals['deals']:
    flight_search.fly_to = city['iataCode']
    flight_search.max_price = city['lowestPrice']
    flight_search.search_flight()
    # If flight is found format the information and send email
    if flight_search.search_result is not None:
        flight_data.format_travel_info(flight_search.search_result, city)
        notification.send_email(flight_data.format_travel, data_manager.emails)
