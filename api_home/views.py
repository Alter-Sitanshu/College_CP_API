from rest_framework import generics
from .models import Account
from rest_framework import permissions
from .serializer import AccountSerializer


class HomeView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

