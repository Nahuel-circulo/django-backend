from rest_framework.routers import DefaultRouter
from sentidos.api.views import FoodApiViewSet,OpinionApiViewSet,UsuarioApiViewSet,MesasApiViewSet,ReservasApiViewSet

router_sentidos = DefaultRouter()

router_sentidos.register(prefix='food',basename='food',viewset=FoodApiViewSet)
router_sentidos.register(prefix='opinion',basename='opinion',viewset=OpinionApiViewSet)
router_sentidos.register(prefix='users',basename='users',viewset=UsuarioApiViewSet)
router_sentidos.register(prefix='tables',basename='tables',viewset=MesasApiViewSet)
router_sentidos.register(prefix='reservation',basename='reservation',viewset=ReservasApiViewSet)