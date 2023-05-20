from django.urls import path
from .import views
urlpatterns = [
    path("", views.index, name="predict"),
    path("generate_smile", views.predict_smiles, name="generate_smile"),
    path("upgrade", views.upgrade, name="upgrade")
]