from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Crop
from .serializers import CropSerializer


class AddCropView(generics.CreateAPIView):
    serializer_class = CropSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        if self.request.user.role != 'farmer':
            raise PermissionDenied("Only farmers can add crops.")
        serializer.save(farmer=self.request.user)


class ListCropsView(generics.ListAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer