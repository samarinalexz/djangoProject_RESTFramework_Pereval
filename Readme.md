# Виртуальная стажировка

## Проект "Pereval Rest API"

Федерации спортивного туризма России [pereval.online](https://pereval.online) (ФСТР) заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней.

Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет.

Модератор из ФСТР будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.
___

*Турист с помощью мобильного приложения будет передавать в ФСТР следующие данные о перевале:*
+ ***Информацию о себе:***
  + ***Фамилия***
  + ***Имя***
  + ***Отчество***
  + ***Электронная почта***
  + ***Номер телефона***
+ ***Название объекта***
+ ***Координаты объекта и его высоту***
+ ***Уровень сложности в зависимости от времени года***
+ ***Несколько фотографий***

*После этого турист нажимает кнопку «Отправить» в мобильном приложении. Мобильное приложение вызовет метод **Pereval**.*

 ***Метод:***
 
```
POST/perevals/create/
```
 
 *принимает JSON в теле запроса с информацией о перевале. Пример JSON-а:*

```
{
  "beauty_title": "пер. ",
  "title": "Перевал",
  "other_titles": "Перевал 1",
  "connect": "", // что соединяет перевал (текстовое поле)
 
  "add_time" // Заполняется автоматически текущей датой в формате "2024-01-01 00:00:00",
  "user": {
        "email": "your@mail.ru", 		
        "surname": "Фамилия пользователя",
        "name": "Имя пользователя",
        "otc": "Отчество пользователя",
        "phone": "89991234567"}, 
 
   "coord":{
        "latitude": "0.0", // Координаты заполняются дробными числами с одним числом после точки.
        "longitude": "0.0",
        "height": "0.0"}
 
  level:{
        "winter": "", // Категория трудности. В разное время года перевал может иметь разную категорию трудности
        "summer": "1А",
        "autumn": "1А",
        "spring": ""},
 
   images: [{title:"Заголовок 1", data:"<фото1>"}, {title:"Заголовок 2", data:"<фото2>"}]
}
```

***Результат метода: JSON***

+ *status — код HTTP, целое число:*
 
   *500 — ошибка при выполнении операции;*

   *400 — Bad Request (при нехватке полей);*

   *200 — данные успешно добавлены.*
    
+ *message — строка:*

   *Причина ошибки (если она была);*
    
   *Отправлено успешно;*

   *Если отправка успешна, дополнительно возвращается id вставленной записи.*
    
       *id — идентификатор, который был присвоен объекту при добавлении в базу данных.*
    
    
***Примеры oтветов:***

    `{ "status": 500, "message": "Ошибка подключения к базе данных","id": null}`

    `{ "status": 400, "message": "Неверный запрос","id": null}`

    `{ "status": 200, "message": null, "id": 5 }`


*После того, как турист добавит в базу данных информацию о новом перевале, сотрудники ФСТР проведут модерацию для каждого нового объекта и поменяют поле status.*

***Список определенных значений для поля status:***

+ *'new'*
+ *'pending' — модератор взял в работу*
+ *'accepted'  — модерация прошла успешно*
+ *'rejected' — модерация прошла, информация не принята*


______

 ***Метод:*** 

```
GET/perevals/edit/<id>
```
*получает одну запись (перевал) по её id с выведением всей информацию об перевале.*

____

***Метод:***

```
PATCH/perevals/edit/<id>
```

*позволяет отредактировать существующую запись, если она в статусе "new". При этом редактировать можно все поля (кроме ФИО, адрес почты и номер телефона). 
В качестве результата изменения приходит ответ содержащий следующие данные:*

 *state:*
     *1 — если успешно удалось отредактировать запись в базе данных.*
     *0 — в отредактировать запись не удалось.*
    
 *message: сообщение о причине неудачного обновления записи.*
 
_____

***Метод:***
   
```
GET/perevals/?user__email=<email>
```

*позволяет получить данные всех объектов, отправленных на сервер пользователем.* 

В качестве реализации использована фильтрация по адресу электронной почты пользователя с помощью пакета **django-filter**

______


***Документация сгенерирована с помощью пакета `drf-yasg`*** 

*Документация **swagger**: http://127.0.0.1:8000/swagger/*<br/>
*Документация **redoc**: http://127.0.0.1:8000/redoc/*

______

***Дополнительно:***

1. *Реализовано повторное использование существующего объекта модели `PerevalUser` при создании нового объекта модели `PerevalAdded`. Если запрос (метод `POST/perevals/`) на добавление записи отправляет пользователь, ранее уже отправлявший такой запрос (определяется по `email`), то для текущей записи используются ранее записанные данные пользователя, а не создается новый пользователь (объект модели `PerevalUser`).* 
2. *Для создания и изменения объектов моделей со связанными данными вложенных сериализаторов использован пакет `drf-writable-nested`*

_______

***Проект опубликован на двух хостингах: pythonanywhere.com и beget.com***

*API **Pereval на pythonanywhere.com**: http://samarinalex.pythonanywhere.com/perevals/<br/>*
*Документация **swagger на pythonanywhere.com**: https://samarinalex.pythonanywhere.com/swagger/<br/>*
*Документация **redoc на pythonanywhere.com**: http://samarinalex.pythonanywhere.com/redoc/<br/>*
*API **Pereval на beget.com**: http://samariut.beget.tech/perevals/<br/>*
*Документация **swagger на beget.com**: https://ssamariut.beget.tech/swagger/<br/>*
*Документация **redoc на beget.com**: http://samariut.beget.tech/redoc/<br/>*

______
