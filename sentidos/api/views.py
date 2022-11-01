from rest_framework.viewsets import ModelViewSet
from sentidos.models import Food,Opinion,Usuario,Mesa,Reserva,Personal,Pedido
from sentidos.api.serializers import FoodSerializer,OpinionSerializer,UsuarioSerializer,MesaSerializer,ReservaSerializer,PersonalSerializer,PedidoSerializer


class FoodApiViewSet(ModelViewSet):
    serializer_class = FoodSerializer

    def get_queryset(self):
        queryset = Food.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category = category)
        return queryset


class OpinionApiViewSet(ModelViewSet):
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all().order_by('-id').values()


class UsuarioApiViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    def get_queryset(self):
        queryset = Usuario.objects.all()
        correo = self.request.query_params.get('email')
        passw = self.request.query_params.get('password')
        if correo is not None and passw is not None:
            print(correo,passw)
            queryset = queryset.filter(email = correo, password=passw)
        return queryset

class PersonalApiViewSet(ModelViewSet):
    serializer_class = PersonalSerializer
    def get_queryset(self):
        queryset = Personal.objects.all()
        username = self.request.query_params.get('username')
        passw = self.request.query_params.get('password')
        if username is not None and passw is not None:
            queryset = queryset.filter(username = username, password=passw)
        return queryset

class MesasApiViewSet(ModelViewSet):
    serializer_class = MesaSerializer
    queryset = Mesa.objects.all()

class ReservasApiViewSet(ModelViewSet):
    serializer_class = ReservaSerializer
    def get_queryset(self):
        queryset = Reserva.objects.all()
        horario = self.request.query_params.get('horario')
        fecha = self.request.query_params.get('fecha')
        user_id = self.request.query_params.get('user_id')
        if horario is not None:
            print(horario)
            queryset = queryset.filter(horario = horario)
        if fecha is not None:
            print(fecha)
            queryset = queryset.filter(fecha = fecha)
        if user_id is not None:
            print(user_id)
            queryset = queryset.filter(user_id = user_id)
        return queryset

class PedidosApiViewSet(ModelViewSet):
    serializer_class = PedidoSerializer
    def get_queryset(self):
        queryset = Pedido.objects.all()
        return queryset
