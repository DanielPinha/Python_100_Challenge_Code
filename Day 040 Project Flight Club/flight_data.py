class FlightData:

    def __init__(self):
        self.from_city = ''
        self.to_city = ''
        self.travel_price = None
        self.travel_link = None
        self.format_travel = {
            'from_city': '',
            'to_city': '',
            'option': [],
            "lowest_option": {},
        }

    def format_travel_info(self, flight_json, city_data):
        """Receives flight raw data and city data and format with useful information"""
        self.clear_format_travel_dict()

        self.from_city = flight_json['data'][0]['cityFrom']
        self.to_city = flight_json['data'][0]['cityTo']
        self.format_travel['from_city'] = self.from_city
        self.format_travel['to_city'] = self.to_city

        lowest_price = city_data['lowestPrice']
        lowest_travel_link = None
        for flight in flight_json['data']:
            self.travel_price = flight['price']
            self.travel_link = flight['deep_link']
            if lowest_price > self.travel_price:
                lowest_price = self.travel_price
                lowest_travel_link = self.travel_link
            self.format_travel["option"] += [
                {
                    'travel price': self.travel_price,
                    'link': self.travel_link,
                }
            ]
        self.format_travel["lowest_option"] = {
            'travel price': lowest_price,
            'link': lowest_travel_link,
        }

    def clear_format_travel_dict(self):
        """Clear Dictionary and reset keys to default values"""
        self.format_travel.clear()
        self.format_travel = {
            'from_city': '',
            'to_city': '',
            'option': [],
            "lowest_option": {},
        }
