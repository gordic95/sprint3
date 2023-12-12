from django.shortcuts import render
from .models import User, Pereval, Coords, Images, Level
from .serializers import UserSerializer, PerevalSerializer, CoordsSerializer, ImagesSerializer, LevelSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
import django_filters


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CoordsViewSet(viewsets.ModelViewSet):
    queryset = Coords.objects.all()
    serializer_class = CoordsSerializer


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer


class LevelViewSet(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class PerevalViewSet(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer
    # добавляем фильтры, они помогут выводить перевалы по id
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['status', 'title', 'add_time', ]

    def update(self):
        instance = self.get_object()
        if instance.status == 'new':
            serializer = self.get_serializer(instance, data=self.request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'state': '1',
                        'message': 'Данные успешно обновлены'
                    }
                )
            else:

                return Response(
                    {
                        'state': '0',
                        'message': 'Ошибка обновления данных'
                    }
                )
        else:
            return Response(
                {
                    'state': '0',
                    'message': 'Нельзя изменить данные'
                }
            )


    # список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.
    def get_queryset(self):
        email = self.request.query_params.get('email')
        if email is not None:
            return Pereval.objects.filter(user__email=email)
        else:
            return Pereval.objects.all()










