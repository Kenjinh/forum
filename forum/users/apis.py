from rest_framework import generics, permissions
from rest_framework.response import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import User
from .serializers import UserSerializer


class ProfileAPI(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.data['_method'] == 'PATCH':
            user = request.user
            serializer = self.serializer_class(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return HttpResponseRedirect(redirect_to=reverse('Profile'))
            return Response(serializer.errors)
