"""todo_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
import backend.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('backend.urls')),
    path('', backend.views.index, name='index'),
    path('Add',backend.views.Add,name='Add'),
    path('add',backend.views.add,name='add'),
    path('multiplay',backend.views.multiplay,name='multiplay'),
    path('t1',backend.views.t1,name='t1'),
    path('t2',backend.views.t2,name='t2'),
    path('t3',backend.views.t3,name='t3'),
    path('t4',backend.views.t4,name='t4'),
    path('t5',backend.views.t5,name='t5'),
    path('t6',backend.views.t6,name='t6'),
    path('t7',backend.views.t7,name='t7'),
    path('t8',backend.views.t8,name='t8'),
    path('t9',backend.views.t9,name='t9'),
    path('sum',backend.views.sum,name='sum'),
    path('divide',backend.views.divide,name='divide'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
