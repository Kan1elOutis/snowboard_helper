"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from orders.views import stripe_webhook_view
from products.views import IndexView, SnowboardsView, BootsView, GlasesView, GlovesView, KrasnoyarskView, SheregeshView, \
    DivnogorskView, FreestyleView, FreerideView, CarvingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('snowboards/', SnowboardsView.as_view(), name='snowboards'),
    path('boots/', BootsView.as_view(), name='boots'),
    path('bracing/', GlasesView.as_view(), name='glases'),
    path('gloves/', GlovesView.as_view(), name='gloves'),
    path('krasnoyarsk/', KrasnoyarskView.as_view(), name='krsk'),
    path('divnogorsk/', DivnogorskView.as_view(), name='divnogorsk'),
    path('sheregesh/', SheregeshView.as_view(), name='sheregesh'),
    path('freestyle/', FreestyleView.as_view(), name='freestyle'),
    path('freeride/', FreerideView.as_view(), name='freeride'),
    path('carving/', CarvingView.as_view(), name='carving'),
    path('products/', include('products.urls', namespace='products')),
    path('resumes/', include('resumes.urls', namespace='resumes')),
    path('users/', include('users.urls', namespace='users')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('accounts/', include('allauth.urls')),
    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
