from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    otc = models.CharField(max_length=50, verbose_name='Отчество')
    email = models.CharField(max_length=50, verbose_name='Электронная почта', unique=True)
    tel = models.CharField(max_length=50, verbose_name='Телефон', unique=True)

    def __str__(self):
        return f'{self.name} {self.fam} {self.otc}'


class Pereval(models.Model):
    new = 'new'
    pending = 'pending'
    accepted = 'accepted'
    rejected = 'rejected'
    TYPE = [
        (new, 'Новый'),
        (pending, 'Ожидается'),
        (accepted, 'Принят'),
        (rejected, 'Отклонен'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, verbose_name='Пользователь')
    coords = models.OneToOneField('Coords', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Координаты')
    level = models.ForeignKey('Level', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Уровень')

    title = models.CharField(max_length=50, null=True, blank=True, verbose_name='Название')
    beautyTitle = models.CharField(max_length=50, default=None, verbose_name='Форма рельефа')
    other_titles = models.CharField(max_length=50, null=True, blank=True, verbose_name='Другое название')
    connect = models.CharField(max_length=50, verbose_name='Вид соединения')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    status = models.CharField(max_length=10, choices=TYPE, default=new, verbose_name='Статус')


class Coords(models.Model):
    latitude = models.FloatField(max_length=50, verbose_name='Широта')
    longitude = models.FloatField(max_length=50, verbose_name='Долгота')
    height = models.IntegerField(verbose_name='Высота')

    def __str__(self):
        return f'широта: {self.latitude}, долгота: {self.longitude}, высота: {self.height}'

    class Meta:
        verbose_name = 'Координата'
        verbose_name_plural = 'Координаты'


class Images(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название',  null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True, verbose_name='Фото')
    pereval = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images', null=True, blank=True)

    def __str__(self):
        return f'{self.pk} {self.title} {self.image}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Level(models.Model):
    LEVELS = [
        ('1a', '1А'),
        ('1b', '1Б'),
        ('2a', '2А'),
        ('2b', '2Б'),
    ]
    winter = models.CharField(max_length=6, choices=LEVELS, verbose_name='Зима', null=True, blank=True)
    summer = models.CharField(max_length=6, choices=LEVELS, verbose_name='Лето', null=True, blank=True)
    autumn = models.CharField(max_length=6, choices=LEVELS, verbose_name='Осень', null=True, blank=True)
    spring = models.CharField(max_length=6, choices=LEVELS, verbose_name='Весна', null=True, blank=True)

    def __str__(self):
        return f'{self.winter}, {self.summer}, {self.autumn}, {self.spring}'

    class Meta:
        verbose_name = 'Категория сложности'
        verbose_name_plural = 'Категория сложности'

