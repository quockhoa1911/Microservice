"""core URL Configuration

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
from rest_framework.routers import SimpleRouter
from api_user.views import Accountsviewset,Rolesviewset,Paymentsviewset

router = SimpleRouter(trailing_slash=True)

router.register(r'users',Accountsviewset,basename='users')
router.register(r'roles',Rolesviewset,basename='roles')
router.register(r'payments',Paymentsviewset,basename='payments')

urlpatterns = router.urls
