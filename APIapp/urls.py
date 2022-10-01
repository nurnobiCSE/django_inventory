from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from APIapp import views

urlpatterns = [
    path('productadd/',views.addProductList.as_view()),
    path('productadd/<int:pk>/',views.addProductDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)