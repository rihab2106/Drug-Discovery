from django.urls import path
from .import views


urlpatterns=[
    path("reto/", views.call_model.as_view(), name="retro"),
    # path("", views.index, name="index")
]
