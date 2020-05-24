from django.urls import path

from . import views

urlpatterns = [
    path("", views.InputView.as_view(), name="ImageInput"),
    path("success", views.SuccessView, name="Output"),
]
