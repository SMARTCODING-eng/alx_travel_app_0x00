from rest_framework import serializers
from .models import Listing, Booking, Review


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id',
            'price',
            'description',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        field =[
            'id',
            'listing',
            'user',
            'book_date',
            'created_at',
        ]
        read_only_fields = ['created_at']


# class ReviewSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Review
#         fields = [
#             'id',
#             'listing',
#             'user',
#             'rating',
#             'comment',
#             'created_at',
#         ]
#         read_only_fields = ['created_at']
