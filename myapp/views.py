from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import User, Task
from .serializers import UserSerializer, TaskSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    http_method_names = ['post']  
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "User created successfully"}, 
            status=status.HTTP_201_CREATED
        )

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'status']
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view returns a list of all tasks
        for the currently authenticated user.
        """
        user = self.request.user
        return Task.objects.filter(responsible=user)

    def perform_create(self, serializer):
        """
        Set the responsible user to the current user when creating a task
        """
        # Explicitly set the responsible to the current user
        serializer.save(responsible=self.request.user)

    def update(self, request, *args, **kwargs):
        # Lógica para atualizar a tarefa
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Lógica para remover a tarefa
        return super().destroy(request, *args, **kwargs)