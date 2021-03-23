from django.urls import path
from .views import home, about, produse, anexe

urlpatterns = [
	path('', home, name="home"),
	path('about', about, name="about"),
	path('produse', produse, name="produse"),
	path('anexe', anexe, name="anexe")
]
