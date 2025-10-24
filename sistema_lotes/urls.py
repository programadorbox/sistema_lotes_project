from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("lotes.urls")),
    path("clientes/", include("clientes.urls")),
    path("intenciones/", include("intenciones.urls")),
    path("usuarios/", include("usuarios.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    # APIs (para React futuro)
    # path("api/", include("intenciones.urls_api")),
    # path("api/", include("lotes.urls_api")),
    # path("api/", include("clientes.urls_api")),
]
