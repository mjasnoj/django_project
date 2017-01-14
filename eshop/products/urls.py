from django.conf.urls import url
from products.views import detail, order


urlpatterns = [
    url(r'^detail/(?P<product_id>\d+)', detail),
    url(r'^order/(?P<product_id>\d+)', order),
]