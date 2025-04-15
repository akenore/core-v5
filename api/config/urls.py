
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView

urlpatterns = [
    path('superadmin/', admin.site.urls),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path("graphql", GraphQLView.as_view(graphiql=True)),
    path('', include('api.urls')),
    path('', include('_auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)