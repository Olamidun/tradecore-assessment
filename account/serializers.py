from .utils import Utils
from decouple import config
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .tasks import geolocate_ip, check_for_holiday
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JwtTokenObtainPairSerializer


User = get_user_model()
utils = Utils()
class RegisterSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=15, write_only=True, min_length=6, required=True)
    email = serializers.EmailField(required=True)

    def create(self, validated_data):
        print(self.context.get('request').META.get('HTTP_X_FORWARDED_FOR'))
        password = validated_data.pop('password')
        email = validated_data.get('email')
        print(email)
        validate_email, status = utils.email_validator(config('EMAIL_VALIDATE_API_KEY'), email)
        # Checking the status alone is not enough because invalid email also returns 200
        if status == 200 and validate_email == 'DELIVERABLE':
            user = User.objects.create_user(email=email)
            user.set_password(password)
            user.save()
            geolocate_ip.delay(config('GEOLOCATE_IP_API_KEY'), '102.89.41.43', email)
            check_for_holiday.delay(config('CHECK_HOLIDAY_API_KEY'), email)
            return user
        else:
            raise serializers.ValidationError({"error": "This email could not be validated"})

    
"""Override the TokenObtainPairSerializer to use email for authentication instead of username"""
class CustomTokenObtainPairSerializer(JwtTokenObtainPairSerializer):
    # username_field = get_user_model().USERNAME_FIELD

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user_id'] = user.id

        return token


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['timezone', 'country_code', 'weekday', 'password', 'last_login', 'user_permissions', 'groups']