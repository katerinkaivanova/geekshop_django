from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

import mainapp.views as mainapp
import authapp.views as authapp
import basketapp.views as basketapp

if settings.DEBUG:
    import debug_toolbar

urlpatterns = [
    path('', mainapp.main_view, name='main'),
    path('auth/', include('authapp.urls', namespace='auth')),
    path('basket/', include('basketapp.urls', namespace='basket')),
    path('orders/', include('ordersapp.urls', namespace='orders')),

    path('products/', include('mainapp.urls', namespace='products')),
    path('history/', mainapp.history_view, name='history'),
    path('showroom/', mainapp.showroom_view, name='showroom'),
    path('contact/', mainapp.contact_view, name='contact'),

    path('admin_custom/', include('adminapp.urls', namespace='admin_custom')),
    path('admin/', admin.site.urls),

    path('social/', include('social_django.urls', namespace='social')),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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