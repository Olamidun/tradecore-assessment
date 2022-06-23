import time
from datetime import datetime
from .utils import Utils
from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def geolocate_ip(geolocation_api_key, ip, email):
    user_data, status = Utils.ip_geolocation(geolocation_api_key, ip)

    if status == 200:
        user = User.objects.get(email=email)
        user.country = user_data['country']
        user.city = user_data['city']
        user.continent = user_data['continent']
        user.country_code = user_data['country_code']
        user.region = user_data['region']
        user.save(update_fields=['country', 'city', 'continent', 'country_code', 'region'])

    elif status == 400:
        pass
    elif status == 401:
        pass


@shared_task
def check_for_holiday(check_for_holiday_api_key, email):

    """
    Used time.sleep to ensure that geolocate_ip tasks finish executing and fills (if any) user's country code column. This is because we need the country code to check if holiday exists.
    in check_holiday method, a requests could be made to the ip geolocator endpoint to get the country code, but to avoid extra api calls, this approach was taken.
    """
    time.sleep(15)
    user = User.objects.get(email=email)
    if user.country_code:
        date_joined = user.date_joined
        year = date_joined.date().year
        month = date_joined.date().month
        day = date_joined.date().day

        response, holiday_status = Utils.check_for_holiday(check_for_holiday_api_key, user.country_code, year, month, day)

        if holiday_status == 200:
            if len(response) > 0:
                user.name_of_holiday = response[0]['name']
                user.holiday_type = response[0]['type']
                # user.holiday_date = datetime.strptime(response[0]['date'], '%d/%m/%Y')
                user.weekday = response[0]['week_day']
                user.save(update_fields=['name_of_holiday', 'holiday_type', 'weekday'])
            else:
                pass
        elif holiday_status == 401:
            pass