from django.db import models
from .services import get_level, get_status, get_new_status


class User(models.Model):

    surname = models.CharField(max_length=255, verbose_name='Фамилия')
    name = models.CharField(max_length=255, verbose_name='Имя')
    otc = models.CharField(max_length=255, verbose_name='Отчество')
    email = models.CharField(max_length=255, verbose_name='Почта')
    phone = models.CharField(max_length=11, verbose_name='Телефон')

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Level(models.Model):

    winter = models.CharField(max_length=2, choices=get_level(), verbose_name='Зима', null=True, blank=True)
    summer = models.CharField(max_length=2, choices=get_level(), verbose_name='Лето', null=True, blank=True)
    autumn = models.CharField(max_length=2, choices=get_level(), verbose_name='Осень', null=True, blank=True)
    spring = models.CharField(max_length=2, choices=get_level(), verbose_name='Весна', null=True, blank=True)

    def __str__(self):
        l_winter = f'Зима - {self.winter};' if self.winter else ""
        l_summer = f'Лето - {self.summer};' if self.summer else ""
        l_autumn = f'Осень - {self.autumn};' if self.autumn else ""
        l_spring = f'Весна - {self.spring};' if self.spring else ""

        return f'{l_winter} {l_summer} {l_autumn} {l_spring}'

    class Meta:
        verbose_name = "Уровень"
        verbose_name_plural = "Уровни"


class Coords(models.Model):
    latitude = models.FloatField(max_length=30, verbose_name='Широта')
    longitude = models.FloatField(max_length=30, verbose_name='Долгота')
    height = models.FloatField(max_length=20, verbose_name='Высота')

    def __str__(self):
        return f'широта:{self.latitude}, долгота:{self.longitude}, высота:{self.height}'

    class Meta:
        verbose_name = "Координаты"
        verbose_name_plural = "Координаты"


class PerevalAdded(models.Model):

    beauty_title = models.CharField(max_length=255, verbose_name='Индекс')
    title = models.CharField(max_length=255, verbose_name='Название')
    other_title = models.CharField(max_length=255, verbose_name='Другое название', null=True, blank=True)
    connect = models.TextField(null=True, blank=True, verbose_name='Соединяет')
    add_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    status = models.CharField(max_length=8, choices=get_status(), default=get_new_status(), verbose_name='Статус')
    coord = models.OneToOneField(Coords, on_delete=models.CASCADE, verbose_name='Координаты')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    level = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Уровень')

    def __str__(self):
        return f'{self.beauty_title}, {self.title}'

    class Meta:
        verbose_name = "Перевал"
        verbose_name_plural = "Перевалы"


class Image(models.Model):

    title = models.CharField(max_length=255, verbose_name='Название', null=True, blank=True)
    data = models.ImageField(verbose_name='Изображение', null=True, blank=True)
    pereval = models.ForeignKey(PerevalAdded, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Фото"
        verbose_name_plural = "Фото"