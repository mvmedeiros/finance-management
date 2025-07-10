from rest_framework import generics, status
from rest_framework.response import Response
from .models import Category
from .serializer import CategorySerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def create(self, request, *args, **kwargs):
        # Check if category exists before validation
        name = request.data.get('name')
        type_ = request.data.get('type')

        if name and type_: # If existent returns the existing category
            existing = Category.objects.filter(name=name, type=type_).first()
            if existing:
                serializer = self.get_serializer(existing)
                return Response(serializer.data,status=status.HTTP_200_OK)

        # Proceed with creation if not found
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response({"message": "New category created!", "category": serializer.data},status=status.HTTP_201_CREATED,headers=headers)

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer