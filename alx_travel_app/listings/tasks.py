from celery import shared_task
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