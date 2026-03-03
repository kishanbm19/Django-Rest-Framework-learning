from django.urls import path
from . import views
urlpatterns=[
    path('',views.ProductListCreateView.as_view()),
    path('update/<int:pk>/',views.updateapiview),
    path('list/',views.ProductListAPIView.as_view()),
    path('fbv/',views.alt_view),
]

