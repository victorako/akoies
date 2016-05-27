from django.conf.urls import url
from views import IndexView, ZOEhubView, ZOEaiView, UsesView, BuyView, ContactView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='home'),
    url(r'^zoehub$', ZOEhubView.as_view(), name='zoehub'),
    url(r'^zoeai$', ZOEaiView.as_view(), name='zoeai'),
    url(r'^uses$', UsesView.as_view(), name='uses'),
    url(r'^buy$', BuyView.as_view(), name='buy'),
    url(r'^contact$', ContactView.as_view(), name='contact')
]