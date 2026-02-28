from django.urls import path
from . import views
urlpatterns=[
    path('',views.ProductListCreateView.as_view()),
    path('<int:pk>/',views.ProductDetailAPIView.as_view()),
    path('list/',views.ProductListAPIView.as_view())
]
