"""urgaz_tutorials URL Configuration

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
from os import name
from django.contrib import admin
from django.urls import path
from app.views.main import *
from app.views.service import *
############################
from statistic.views.main import *
from statistic.views.create import *
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordChangeView
urlpatterns = [
    ##########   APP
    path('xiidot1303/', admin.site.urls),
    path('', main, name='main'),
    # services
    path('services', services, name='services'),
    path('service/get_ip', service_get_ip, name='service_get_ip'),
    path('service/net_use', service_net_use, name='service_net_use'),
    path('service/get/net_use/<str:file>/', service_get_net_use, name='service_get_net_use'),
    path('service/install_printers', service_install_printers, name='service_install_printers'),





    ######## STATISTIC 
    path('statistic/<int:smena>/', statistic_menu, name='statistic'),
    path('statistic/table', statistic_table, name='statistic_table'),
    path('accounts/login/', LoginView.as_view()),
    path('statistic', main_menu, name='main_menu'),

    #workers
    path('workers/all', workers_all, name='workers_all'),
    path('create/worker', WorkerCreateView.as_view(), name='create_worker'),

    #stanok
    path('tools/all', stanoks_all, name='stanok_all'),
    path('create/tool', StanokCreateView.as_view(), name='create_stanok'),

    #report
    path('reports/all/<str:st>/<int:year>/<int:month>/<int:day>/', reports_all, name='reports_all'),
    path('create/report', ReportCreateView.as_view(), name='create_report'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
