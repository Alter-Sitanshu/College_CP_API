from rest_framework import generics
from .models import Account
from rest_framework import permissions,authtoken,authentication
from .serializer import AccountSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse

class HomeView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class DeleteView(generics.DestroyAPIView):
    queryset = Account.objects.all()
    lookup_field = 'pk'
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

# @api_view(["PUT"])
# def UpdateView(request, *args, **kwargs):
#     instance = Account.objects.get(pk=kwargs['pk'])
#     data = request.data
#     serializer = AccountSerializer(instance, data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return JsonResponse(serializer.data)
    
class DetailView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    lookup_field = 'pk'
    serializer_class = AccountSerializer
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class UpdateView(generics.UpdateAPIView):
    queryset = Account
    serializer_class = AccountSerializer
    lookup_field = 'pk'
    authentication_classes = [
        authentication.SessionAuthentication,
        authentication.TokenAuthentication
    ]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    