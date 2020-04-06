from django.conf.urls import url
from portfolio import views
from portfolio import portfolio

urlpatterns = [
    django.urls.path('', portfolio.urls, name='URLs')
]