from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'status']
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        # Lógica para atualizar a tarefa
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Lógica para remover a tarefa
        return super().destroy(request, *args, **kwargs)