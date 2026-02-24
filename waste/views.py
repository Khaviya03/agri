from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Waste
from .serializers import WasteSerializer


class AddWasteView(generics.CreateAPIView):
    serializer_class = WasteSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Example internal market rates
    MARKET_RATES = {
        "Rice Husk": 5,
        "Coconut Shell": 7,
        "Sugarcane Bagasse": 4,
        "Wheat Straw": 6,
    }

    def perform_create(self, serializer):
        if self.request.user.role != 'farmer':
            raise PermissionDenied("Only farmers can add waste.")

        waste_type = self.request.data.get("waste_type")
        quantity = float(self.request.data.get("quantity"))

        rate = self.MARKET_RATES.get(waste_type, 3)  # default rate
        estimated_value = quantity * rate

        serializer.save(
            farmer=self.request.user,
            estimated_value=estimated_value
        )


class ListWasteView(generics.ListAPIView):
    queryset = Waste.objects.all()
    serializer_class = WasteSerializer