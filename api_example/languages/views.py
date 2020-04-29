from django.shortcuts import render
from rest_framework import viewsets
from .models import Language, Paradigm, Programmer
from .serializers import LanguageWriteSerializer, LanguageReadSerializer
from .serializers import ParadigmWriteSerializer, ParadigmReadSerializer
from .serializers import ProgrammerWriteSerializer, ProgrammerReadSerializer


# You do not have to initialize serial_class directly since the Serializer
# classes are now split up into two different classes (WRITE and READ) as
# you can see in the SERIALIZERS class. This is so that depth can be set
# when reading an object, while keeping the writing functionality. The viewsets
# now get the serializer_class from the get_serializer_class method
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    # serializer_class = LanguageSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return LanguageWriteSerializer
        else:
            return LanguageReadSerializer


class ParadigmView(viewsets.ModelViewSet):
    queryset = Paradigm.objects.all()
    # serializer_class = ParadigmSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ParadigmWriteSerializer
        else:
            return ParadigmReadSerializer


class ProgrammerView(viewsets.ModelViewSet):
    queryset = Programmer.objects.all()
    # serializer_class = ProgrammerSerializer

    def get_serializer_class(self):
        method = self.request.method
        if method == 'PUT' or method == 'POST':
            return ProgrammerWriteSerializer
        else:
            return ProgrammerReadSerializer
