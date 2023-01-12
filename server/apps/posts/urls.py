from django.contrib import admin
from django.urls import path,include
from server.apps.posts.views import posts_update,posts_delete,posts_create,posts_list,posts_retrieve
urlpatterns = [
    path("admin/", admin.site.urls),
    path("",posts_list),
    path("posts/posts_create",posts_create),
    path("posts/<int:pk>",posts_retrieve),
    path("posts/<int:pk>/delete",posts_delete),
    path("posts/<int:pk>/update",posts_update),
    
]
