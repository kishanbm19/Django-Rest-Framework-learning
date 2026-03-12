from django.urls import path
from . import views
urlpatterns=[
    path('',views.ProductListCreateView.as_view(),name='product-detail'),
    # path('update/<int:pk>/',views.updateapiview),
    path('update/<int:pk>/',views.Product_update_generics.as_view()),
    path('list/',views.ProductListCreateView.as_view()),
    path('fbv/',views.alt_view),
    # path('delete/<int:pk>/',views.deleteapiview),
     path('delete/<int:pk>/',views.product_destroy_api_generics.as_view()),


    #  mixins urls
    path('mixinproduct/',views.Productlistcreate_mixin.as_view()),
    path('mixindet/<int:pk>/',views.ProductDetailMixin.as_view(),name='product-detail'),

    
]

