"""testProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path



# from django.urls import path
from django.conf.urls import url,include
#from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^home/', include('nextapp.urls')),## when browser ask for /home/ in url it go to urls defined in desired]
#url(r'^$', RedirectView.as_view(url='/home/main/', permanent=True)),
    #url(r'^file/', include('testapp.urls'))
    #url(r'^$', RedirectView.as_view(url='/players/', permanent=True)),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns = format_suffix_patterns(urlpatterns)

