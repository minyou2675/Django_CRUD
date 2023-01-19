from django.contrib import admin
from django.urls import path,include
from server.apps.posts.views import *

app_name= "app"
urlpatterns = [
     path('admin/', admin.site.urls),
     path('',idea_list, name="list"),
     path('idea/create',idea_create, name="create"),
     path('idea/<int:pk>',idea_detail,name="detail"),
     path('idea/<int:pk>/update',idea_update,name="update"),
     path('idea/<int:pk>/delete',idea_delete,name="delete"),
     path('tool/list',tool_list, name='list'),
     path('tool/create',tool_create, name="create"),
     path('tool/<int:pk>',tool_detail,name="detail"),
     path('tool/<int:pk>/update',tool_update,name="update"),
]