from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny

from subcategory.models import Subcategory
from subcategory.serializers import SubcategorySerializer

"""
Authenticated views
"""


class SubcategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]


class SubcategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [
        IsAuthenticated,
        IsAdminUser,
    ]
    lookup_field = "slug"


"""
Public views
"""


class SubcategoryListAPIView(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [
        AllowAny,
    ]


class SubcategoryRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
    permission_classes = [
        AllowAny,
    ]
    lookup_field = "reference"
