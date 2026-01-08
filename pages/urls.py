from django.urls import path
from . import views

urlpatterns = [
    path("", views.page_list, name="page_list"),
    path("create/", views.PageCreateView.as_view(), name="page_create"),
    path("<int:pk>/", views.page_detail, name="page_detail"),
    path("<int:pk>/update/", views.PageUpdateView.as_view(), name="page_update"),
    path("<int:pk>/delete/", views.PageDeleteView.as_view(), name="page_delete"),
]