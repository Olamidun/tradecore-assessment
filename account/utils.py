import requests

"""Utility class that contains methods to validate email, geolocate ip address and get holidays"""
class Utils:
    @classmethod
    def email_validator(self, email_validator_api_key, email):
        endpoint = f"https://emailvalidation.abstractapi.com/v1/?api_key={email_validator_api_key}&email={email}"

        response = requests.get(endpoint)

        if response.status_code == 200:
            return response.json()['deliverability'], 200
    @classmethod
    def ip_geolocation(cls, geolocation_api_key, ip):
        endpoint = f"https://ipgeolocation.abstractapi.com/v1/?api_key={geolocation_api_key}&ip_address={ip}&fields=country,city,continent,region,country_code"

        response = requests.get(endpoint)

        # response_dict = {
        #     200: ,
        #     400: response.json()['error']['details']['ip_address'][0],
        #     401: response.json()['error']['message']
        # }
        if response.status_code == 200:
           return response.json(), 200
        elif response.status_code == 400:
            return response.json()['error']['details']['ip_address'][0], 400
        elif response.status == 401:
            return response.json()['error']['message'], 401
        
    @classmethod
    def check_for_holiday(cls, check_holiday_api_key, country_code, year, month, day ):
        # country_code = cls.ip_geolocation(geolocation_api_key, ip)['country_code']
        endpoint = f"https://holidays.abstractapi.com/v1/?api_key={check_holiday_api_key}&country={country_code}&year={year}&month={month}&day={day}"
        response = requests.get(endpoint)

        print(response.json())

        if response.status_code == 200:
            return response.json(), 200
        elif response.status_code == 401:
            return response.json()['error']['message'], 401
