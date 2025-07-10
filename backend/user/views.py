from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializer import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # Check if User exists before validation
        username = request.data.get('username')

        if username: # If existent returns the existing User
            existing = User.objects.filter(username=username).first()
            if existing:
                serializer = self.get_serializer(existing)
                return Response(serializer.data,status=status.HTTP_200_OK)

        # Proceed with creation if not found
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "New user created!", "category": serializer.data},status=status.HTTP_201_CREATED,headers=headers)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
