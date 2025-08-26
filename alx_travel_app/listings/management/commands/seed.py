import csv
import os
from uuid import UUID
from datetime import datetime

from django.core.management.base import BaseCommand
from listings.models import User, Location, Listing, Booking, Review

def read_csv_generator(csv_file):
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            yield row

def parse_bool(value):
    return str(value).strip().lower() in ['1', 'true', 'yes']

def parse_uuid(value):
    try:
        return UUID(value)
    except Exception as e:
        print(f"[UUID]({value}) Error: {e}")
        return None

def parse_datetime(value):
    try:
        return datetime.fromisoformat(value)
    except Exception:
        return None

def populate_user_table(csv_file, stdout):
    for row in read_csv_generator(csv_file):
        try:
            user, created = User.objects.get_or_create(
                id=parse_uuid(row['id']),
                defaults={
                    'username': row['username'],
                    'first_name': row['first_name'],
                    'last_name': row['last_name'],
                    'email': row['email'],
                    'is_staff': parse_bool(row['is_staff']),
                    'is_active': parse_bool(row['is_active']),
                    'date_joined': row['date_joined'],
                }
            )
            action = "Created" if created else "Exists"
            stdout.write(f"[User] {action}: {user.username}")
        except Exception as e:
            stdout.write(f"[User] Error: {e}")

def populate_location_table(csv_file, stdout):
    for row in read_csv_generator(csv_file):
        try:
            location, created = Location.objects.get_or_create(
                id=parse_uuid(row['id']),
                defaults={
                    'country': row['country'],
                    'state': row['state'],
                    'city': row['city'],
                }
            )
            action = "Created" if created else "Exists"
            stdout.write(f"[Location] {action}: {location.city}")
        except Exception as e:
            stdout.write(f"[Location] Error: {e}")

def populate_listing_table(csv_file, stdout):
    for row in read_csv_generator(csv_file):
        try:
            listing, created = Listing.objects.get_or_create(
                id=parse_uuid(row['id']),
                defaults={
                    'title': row['title'],
                    'price_per_night': float(row['price_per_night']),
                    'description': row['description'],
                    'image_url': row['image_url'],
                    'created_at': parse_datetime(row['created_at']),
                    'updated_at': parse_datetime(row['updated_at']),
                    'host_id': parse_uuid(row['host']),
                    'location_id': parse_uuid(row['location']),
                }
            )
            action = "Created" if created else "Exists"
            stdout.write(f"[Listing] {action}: {listing.title}")
        except Exception as e:
            stdout.write(f"[Listing] Error: {e}")

def populate_booking_table(csv_file, stdout):
    for row in read_csv_generator(csv_file):
        try:
            booking, created = Booking.objects.get_or_create(
                id=parse_uuid(row['id']),
                defaults={
                    'start_date': parse_datetime(row['start_date']),
                    'end_date': parse_datetime(row['end_date']),
                    'total_price': float(row['total_price']),
                    'status': row['status'],
                    'created_at': parse_datetime(row['created_at']),
                    'updated_at': parse_datetime(row['updated_at']),
                    'guest_id': parse_uuid(row['guest']),
                    'listing_id': parse_uuid(row['listing']),
                }
            )
            action = "Created" if created else "Exists"
            stdout.write(f"[Booking] {action}: {booking.id}")
        except Exception as e:
            stdout.write(f"[Booking] Error: {e}")

def populate_review_table(csv_file, stdout):
    for row in read_csv_generator(csv_file):
        try:
            review, created = Review.objects.get_or_create(
                id=parse_uuid(row['id']),
                defaults={
                    'rating': int(row['rating']),
                    'comment': row['comment'],
                    'created_at': parse_datetime(row['created_at']),
                    'updated_at': parse_datetime(row['updated_at']),
                    'listing_id': parse_uuid(row['listing']),
                    'guest_id': parse_uuid(row['guest']),
                }
            )
            action = "Created" if created else "Exists"
            stdout.write(f"[Review] {action}: {review.id}")
        except Exception as e:
            stdout.write(f"[Review] Error: {e}")

class Command(BaseCommand):
    help = "Populates the database with sample data from CSV files."

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(BASE_DIR, '..', 'data')

    def handle(self, *args, **options):
        users_csv = os.path.join(self.data_dir, 'users.csv')
        populate_user_table(users_csv, self.stdout)

        locations_csv = os.path.join(self.data_dir, 'locations.csv')
        populate_location_table(locations_csv, self.stdout)

        listings_csv = os.path.join(self.data_dir, 'listings.csv')
        populate_listing_table(listings_csv, self.stdout)

        bookings_csv = os.path.join(self.data_dir, 'bookings.csv')
        populate_booking_table(bookings_csv, self.stdout)

        reviews_csv = os.path.join(self.data_dir, 'reviews.csv')
        populate_review_table(reviews_csv, self.stdout)

        self.stdout.write(self.style.SUCCESS("✅ Database populated successfully!"))
