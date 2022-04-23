from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/publish/', include(('publish.urls', 'publish'))),
    # 将各app（如publish）中指定的路由导入到总路由中
]