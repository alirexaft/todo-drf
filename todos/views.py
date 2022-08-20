from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer


class ListTodo(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset


class DetailTodo(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset


class TodoCreation(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            Todo.objects.create(user=self.request.user, title=serializer.validated_data['title'])
            return Response(data={'status': 'Created'}, status=status.HTTP_201_CREATED)
        return Response(data={'status': 'Wrong'}, status=status.HTTP_400_BAD_REQUEST)


class TodoUpdate(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset


class TodoDelete(DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TodoSerializer

    def get_queryset(self):
        queryset = Todo.objects.filter(user=self.request.user)
        return queryset
