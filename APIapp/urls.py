from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from APIapp import views

urlpatterns = [
    path('productadd/',views.addProductList.as_view()),
    path('productadd/<int:pk>/',views.addProductDetail.as_view()),
    path('registered_user/',views.registered_UserList.as_view()),
    path('returnproduct/',views.returnProductList.as_view()),
    path('saleproduct/',views.saleProductList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)