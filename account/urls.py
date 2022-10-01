from django.urls import path
from .import views
app_name = "account"
urlpatterns = [
    #path('login/', views.authlogin, name = "login" ),
    path('', views.login_set, name = 'login' ),
    path('', views.logout, name = 'logout' ),
    path('dashboard', views.dashboard, name = 'home' ),
    path('products/', views.product_set, name='products' ),
    path('returns-products/', views.return_set, name = 'return' ),
    path('sales-products/', views.sales_set, name = 'sale' ),
    path('user-managements/', views.user_set, name = 'my_user' ),
    path('Add-products/', views.addProduct_set, name = 'addproducts' ),
    path('Add-returns-Product/', views.addReturn_set, name = 'addreturn' ),
    path('Add-sales-Product/', views.addSale_set, name = 'addsale' ),
    path('Adduser-managements/', views.addUser_set, name = 'addmy_user' ),
    #path('settings-Profile/', views.pageUser_set, name = 'profile' ),
    #path('System-login/', views.login_set, name = 'login' ),
]