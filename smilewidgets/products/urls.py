from django.urls import path

from .views import PriceCalculatorView

urlpatterns = [
    path('get-price/', PriceCalculatorView.as_view(), name='price_calculator'),
]