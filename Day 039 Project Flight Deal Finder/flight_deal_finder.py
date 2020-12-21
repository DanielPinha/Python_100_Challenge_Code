import data_manager
import flight_search
import flight_data
import notification_manager

data_manager = data_manager.DataManager()
flight_search = flight_search.FlightSearch()
flight_data = flight_data.FlightData()
notification = notification_manager.NotificationManager()

# For each city in the data file get IATA code and price to search for flight
for city in data_manager.deals['deals']:
    flight_search.fly_to = city['iataCode']
    flight_search.max_price = city['lowestPrice']
    flight_search.search_flight()
    # If flight is found format the information and send email
    if flight_search.search_result is not None:
        flight_data.format_travel_info(flight_search.search_result, city)
        notification.send_email(flight_data.format_travel)
