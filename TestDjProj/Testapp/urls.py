from django.urls import path

from . import views


urlpatterns = [
    path('list/<int:index>', views.show_list, name="show_list"),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path("create/", views.create_list, name="create_list"),
    path("register/", views.register, name="register"),
    path("my_lists/", views.my_lists, name="my_lists"),
    path("delete_list/<int:list_id>", views.delete_list, name="delete_list"),
    path("delete_item/<int:list_id>/<int:item_id>", views.delete_item, name="delete_item"),
    path("change_item_status/<int:list_id>/<int:item_id>", views.change_item_status, name="change_item_status"),
]