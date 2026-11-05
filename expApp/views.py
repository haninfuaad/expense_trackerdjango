from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework  import permissions,authentication
from expApp.models import expModel
from expApp.serializer import ExpSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter


# Create your views here.
class ExpCreateListView(CreateAPIView,ListAPIView):
    serializer_class=ExpSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    

    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]

    filterset_fields = ['category', 'payment']
    search_fields = ['title']
    ordering_fields = ['amount', 'created_at']

    def perform_create(self,serializer):
        user=self.request.user
        return serializer.save(owner=user)

    def get_queryset(self):
        return expModel.objects.filter(owner=self.request.user)


class ExpRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):
    serializer_class=ExpSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    lookup_url_kwarg = "id"
    def get_queryset(self):
        return expModel.objects.filter(owner=self.request.user)


