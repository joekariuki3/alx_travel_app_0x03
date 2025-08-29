from rest_framework import serializers
from .models import User, Listing, Booking, Payment, Location

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name' , 'username', 'email', 'phone_number']
        read_only_fields = ['id']

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'price_per_night', 'description', 'image_url', 'location', 'host', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'start_date', 'end_date', 'status', 'total_price', 'payment_url',  'guest', 'listing', 'created_at', 'updated_at']
        read_only_fields = ['id', 'payment_url', 'total_price', 'status', 'created_at', 'updated_at']

    def validate_booking_days(self, days):
        if days < 1:
            raise serializers.ValidationError("Booking days must be at least 1 day long.")
        return days


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'country', 'state', 'city']
        read_only_fields = ['id']