from django.urls import include, path

from config import settings
from public_website import api, views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("services/", views.services_view, name="services"),
    path("accessibilite/", views.accessibility_view, name="accessibilite"),
    path("artois-mobilites/", views.pole_emploi_status_view, name="artois-mobilites"),
    path(
        "brest-metropole/", views.etudiant_boursier_status_view, name="brest-metropole"
    ),
    path(f"api/webhook/{settings.GRIST_WEBHOOK_SECRET}", api.webhook, name="webhook"),
    path("login/", views.login_view, name="login"),
    path("oidc/", include("mozilla_django_oidc.urls")),
    path("mentions-legales/", views.legal_notice_view, name="mentions-legales"),
]
