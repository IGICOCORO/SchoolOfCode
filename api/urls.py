# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('', views.liste_demandes, name='liste_demandes'),
#     # path('demandes/creer/', views.creer_demande, name='creer_demande'),
# ]

from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register('demandes', views.DemandeCongeViewSet)
router.register('employes', views.EmployeViewSet)
router.register('types', views.TypeCongeViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api_auth', include('rest_framework.urls')),
]