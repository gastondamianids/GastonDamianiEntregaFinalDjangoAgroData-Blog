from django.urls import path
from . import views

urlpatterns = [
    path("", views.inbox, name="inbox"),
    path("send/", views.send_message, name="send_message"),
    path("<int:pk>/", views.message_detail, name="message_detail"),
    path("<int:pk>/delete/", views.message_delete, name="message_delete"),


]
