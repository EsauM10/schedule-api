from rest_framework import generics
from .models import Task
from .permissions import IsAuthor
from .serializers import TaskSerializer


class TaskList(generics.ListCreateAPIView):
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        user = self.request.user
        created_at = self.request.query_params.get('created_at')

        if(created_at is not None):
            return Task.objects.filter(author=user, created_at=created_at)
        return Task.objects.filter(author=user)



class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthor]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    
