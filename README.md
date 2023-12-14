                  Проект виртуальной стажировки онлайн-школы Skillfactory
                                Описание проекта
Мобильное приложение для оправки информации туристами о посещённых ими горных перевалов.
Мобильное приложение для Android и IOS, пользователями которого будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР ( Федерация спортивного туризма России ), как только появится доступ в Интернет, для того чтобы поделиться информацией с другими людьми, увлеющимися туризмом и преодолением горных перевалов.

                                Работа проекта

                        Внесение личной информации.
Для отправки информации туристу необходимо будет заполнить данные о себе (регистрация не требуется):
- Имя
- Фамилия
- Отчество
- Электронная почта
- Номер телефона

                          Внесение информации о горном перевале.
Для отправки информации о горном перевале, туристу необходимо будет также заполнить несколько полей:
- Название горного перевала
- Альтернативное название горного перевала
- Произвольный текст ввиде комментария
- Координаты горного перевала
- Сложность восхождения (в зависимости от времени года)
- Обработка информации.
- Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

                               Содержание проекта
- Основные пункты.
- Проект выполнен на языке программирования Python
- С использованием фреймворка Django
- В проекте используется СУБД PostgreSQL

                                 Модели проекта.
- User - содержит всю информацию о пользователе (ФИО, тел, эл. почта)
- Coords - содержит три поля (долгота, широта, высота)
- Level - содержит 4 уровня сложности
- Images - состоит из описания, самого изображения и связи с перевалом
- Pereval - включает в себя название, второе название, описание, тип связи, дата добавления, статус, а так же связи с user, coors, level

                             Сериализаторы проекта.
Каждая модель проекта имеет соответствующий сериализатор. Основным сериализатором проекта служит PerevalSerializer содержащий в себе сериализаторы остальных моделей.

class PerevalSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    coords = CoordsSerializer()
    level = LevelSerializer()
    images = ImagesSerializer(many=True)

                        Представления и маршрутизация проекта.
В качестве представлений в проекте используется наследование класса ModelViewSet. В проекте используются единственный url, предоставляющий список всех добавленных перевалов от пользователей path('submitData/', include(router.urls)), Можно просмотреть информацию об отдельном перевале по id. При этом есть возможность использовать CRUD методы, а также фильтровать добавленную информацию по электронной почте пользователя.

                                Ограничения в проекте.
В проекте существует условие при котором пользователь может изменить отправленные данные:

Данные не должны относиться к данным о самом пользователе (фамилия, имя, телефон и т.д.)
Статус модерации данной информации должен быть статусом 'new', при остальных статусах модерации, изменение данных невозможно
Пример JSON файла с данными.
[
    {
        "id": 1,
        "user": {
            "name": "Олег",
            "fam": "Петров",
            "otc": "Александрович",
            "tel": "89991112233",
            "email": "test@example.com"
        },
        "coords": {
            "latitude": 123456.0,
            "longitude": 987654.0,
            "height": 1200
        },
        "level": {
            "id": 1,
            "winter": "1a",
            "summer": null,
            "autumn": null,
            "spring": null
        },
        "images": [
            {
                "title": "гора",
                "image": "http://127.0.0.1:8000/media/images/art-voennogo-muzhchiny-v-ochkax_qiyxwWi.jpg"
            }
        ],
        "title": "Гора Арни",
        "beautyTitle": "Сухая",
        "other_titles": "Железный Арни",
        "connect": "Какой-то",
        "add_time": "2023-12-14T11:18:44.114812Z",
        "status": "new"
    }
]

                Проект покрыт тестами 
                
                Документация проекта с помощью Swagger.
http://127.0.0.1:8000/redoc/
http://127.0.0.1:8000/swagger/
http://127.0.0.1:8000/json/
