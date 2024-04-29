from django.urls import path
#from cars.views import CarTestView, CarDetailView
from cars.views import CarListCreateView

urlpatterns = [
    # path('carTest', CarTestView.as_view()),
    # path('carDetail/<int:pk>', CarDetailView.as_view()),
    # path('carDetail/<str:pk>', CarDetailView.as_view()),
    # path('carDetail/<slug:pk>', CarDetailView.as_view()),
    path('cars', CarListCreateView.as_view()),
]