from django.urls import URLPattern, path
from .views import AdocaoList

urlpatterns = [path("", AdocaoList.as_view())]
