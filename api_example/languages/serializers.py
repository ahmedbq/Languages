from rest_framework import serializers
from .models import Language, Paradigm, Programmer

# We have a serializer for both READ and WRITE, otherwise you will not be able
# to POST this object if you set the depth to something. In return you have to
# override the get_serializer_class() function in the VIEWS


# ModelSerializer does not give you the URL
class LanguageReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')
        depth = 1


class LanguageWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'url', 'name', 'paradigm')


class ParadigmReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')
        depth = 1


class ParadigmWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Paradigm
        fields = ('id', 'url', 'name')


class ProgrammerReadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        # The difference here is the 'languages' variable representing the
        # 1 to MANY relationship with the langauges variable declared in the
        # Programmer class
        fields = ('id', 'url', 'name', 'languages')
        # This depth property is so that instead of a list of language URLs
        # you get the actual object properties showing up. It's set to 2 so
        # that it can also display the paradigm of the languages as well.
        depth = 2

class ProgrammerWriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id', 'url', 'name', 'languages')
