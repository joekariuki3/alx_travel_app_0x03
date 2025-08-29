from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from .models import Booking


@shared_task
def send_booking_confirmation_email(booking_id):
    """
    Sends a booking confirmation email to the guest of a specified booking.

    This function retrieves the booking by its ID, constructs a confirmation
    email message, and sends the email to the booking guest.

    Parameters:
        booking_id (int): The ID of the booking for which the confirmation email
        needs to be sent.
    """
    booking = Booking.objects.get(id=booking_id)
    subject = "Booking Confirmation"
    message = f"Your booking for {booking.listing.title} has been confirmed. Thank you for booking with us!"
    booking.guest.email_user(
        subject,
        message,
    )


@shared_task
def send_payment_confirmation_email(user_email, booking_id):
    subject = "Booking Payment Confirmation"
    message = f"Your payment for booking {booking_id} was successful. Thank you for booking with us!"
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user_email])