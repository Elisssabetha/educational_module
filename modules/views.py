from django.shortcuts import render
from rest_framework import generics


class ModulesCreateAPIView(generics.CreateAPIView):
    pass


class ModulesListAPIView(generics.ListAPIView):
    pass


class ModulesRetrieveAPIView(generics.RetrieveAPIView):
    pass


class ModulesUpdateAPIView(generics.UpdateAPIView):
    pass


class ModulesDestroyAPIView(generics.DestroyAPIView):
    pass
