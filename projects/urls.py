from django.urls import path
from projects import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.projects_list, name="projects_list"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

