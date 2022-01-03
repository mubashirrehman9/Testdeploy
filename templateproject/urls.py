"""templateproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from database import views
from database.views import *
from django.conf import settings
from django.conf.urls.static import static

from database.views import Loginform, MyContact, MyRegister, Logout, Changepassword, Newpassword

from database.views import Changeprofile

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('index', views.index, name='profile'),
                  path('index' , views.index.as_view(),name='profile'),
                  # path('getCategory/<int:id>/', views.index1, name='category'),
                  # path('getCategory1/<int:id>/', views.index2, name='category'),
                  path('getCategory/<int:id>/', views.index1.as_view(), name='category'),
                  path('getCategory1/<int:id>/', views.index2.as_view(), name='category'),
                  # path('getCategory2/', views.index3.as_view, name='filter'),
                  path('getCategory2/', views.index3.as_view(), name='filter'),
                  path('getCategory5/<int:id>/', views.index4.as_view()),
                  # path('index', views.index, name='profile'),
                  # path('product', views.product,name='product'),
                  path('product', views.product.as_view(),name='product'),
                  # path('about_us', views.about),
                  path('about_us', views.about.as_view()),
                  path('contact_us', MyContact.as_view()),
                  # path('product_detail', views.product_detail),
                  # path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
                  path('product_detail', views.product_detail.as_view()),
                  path('product_detail/<int:id>/', views.product_detail.as_view(), name='product_detail'),
                  path('search_result', views.search),
                  path('my_account', views.account),
                  path('checkout_payment', views.checkout),
                  path('checkout_info', views.checkout_info),
                  path('checkout_complete', views.checkout_complete),
                  path('checkout_cart', views.checkout_cart),
                  path('faq', views.faq),
                  path('registration', MyRegister.as_view() , name='registration1'),
                  path('login/', Loginform.as_view(), name='loginform'),
                  path('logout', Logout.as_view(), name='logout'),
                  path('changepassword', Changepassword.as_view(), name='Changepassword'),
                  path('Newpassword', Newpassword.as_view(), name='newpassword'),
                  path('changeprofile', Changeprofile.as_view(), name='Changeprofile'),
                  path('registration/<slug:token>/',views.verify, name='verify'),
                  # path('rate/',views.rate_image,name='rate_view')

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
