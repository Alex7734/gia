from django.urls import path
from .views import home, about, produse, anexe, sendEmail

urlpatterns = [
	path('', home, name="home"),
	path('about', about, name="about"),
	path('produse', produse, name="produse"),
	path('anexe', anexe, name="anexe"),
	path('send-email', sendEmail, name="send-email")
]
