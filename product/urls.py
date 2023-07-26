from django.urls import path
from . import views
from django.conf import settings

app_name='product'

urlpatterns = [
    # path('',views.index,name="index"),
    path('',views.allproductcat,name="allproductcat"),
    path('<slug:slug>/',views.allproductcat,name="product_by_cat"),
    path('<slug:slug>/<slug:pro_slug>/',views.prodetails,name="product_details"),
]

from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
