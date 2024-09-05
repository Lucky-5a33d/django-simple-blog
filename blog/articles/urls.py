from django.urls import path

from .views import Articles_list,Article_detail,Article_CreateView

urlpatterns = [
    path("", Articles_list.as_view(), name="index"),
    path("article/<int:pk>",Article_detail.as_view(),name="article"),
    path("article/create",Article_CreateView.as_view(),name="create")
]