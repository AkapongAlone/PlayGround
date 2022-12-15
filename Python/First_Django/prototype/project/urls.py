"""first_backend URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main import views
# from django.conf.urls.static import static
# from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^',include('cal_data.urls')),
    path('',views.hello,name="home"),
    path('add',views.add),
    path('get_model',views.get_model),
    path('first',views.main),
    path('check',views.check),
    path('process',views.main_2),
    path('edit',views.edit),
    path('wi',views.wi),
    path('insert_wi',views.wi_insert),
    path('add_tool',views.add_tool),
    path('pattern',views.pattern),
    path('editmodel',views.overview),
    path('skip',views.skip),
    path('csv',views.csv),
    path('delete',views.delete),
] + staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)