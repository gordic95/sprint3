from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'fam',  'otc', 'tel', 'email')


class CoordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coords
        fields = ('latitude', 'longitude', 'height')


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('title', 'image')


class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'


class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)



    class Meta:
        model = Pereval
        fields = '__all__'

    def validate(self, data):
        if self.instance is not None:
            instance_user = self.instance.user
            data_user = data['user']
            user_field_for_validation = [
                instance_user.name != data_user['name'],
                instance_user.fam != data_user['fam'],
                instance_user.otc != data_user['otc'],
                instance_user.tel != data_user['tel'],
                instance_user.email != data_user['email'],
            ]
            if data_user is None or any(user_field_for_validation):
                raise serializers.ValidationError('Нельзя изменить данные пользователя')
        return data




