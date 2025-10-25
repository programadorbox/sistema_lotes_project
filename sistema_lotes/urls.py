from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
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
