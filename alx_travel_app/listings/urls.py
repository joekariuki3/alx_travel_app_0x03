from .views import ListingViewSet, BookingViewSet, verify_payment, UserViewSet, LocationViewSet, \
    PaymentListView
from rest_framework_nested import routers
from django.urls import path


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('locations', LocationViewSet)
router.register('listings', ListingViewSet)
router.register('bookings', BookingViewSet)

urlpatterns = [
    *router.urls,
    path("payments/", PaymentListView.as_view(), name="payment_list"),
    path("payments/verify/<str:tx_ref>/", verify_payment, name="verify_payment"),
]

