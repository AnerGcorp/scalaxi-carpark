## Проектирование базы данных автостоянок

Имеется пять таблиц «OwnerCarPark», «CarPark», «CarDriver», «Car» и «CarDriver».
«Автомобильный маршрут». Определим связи моделей(таблиц)

- `OwnerCarPark` и `CarPark`, существует два разных сценария: `OwnerCarPark` может иметь множество `CarPark` или один `CarPark` =>, поэтому будет связь «один ко многим».
- `CarPark` и `Car`, `CarPark` может иметь много `Car`, поэтому существует также связь один-ко-многим.
- `CarDriver` и `Car`, у `Car` есть только один `CarDriver`, поэтому связь будет один к одному.
- `Car` и `CarRoute`, `Car` имеет только один `CarRoute` (в некоторых случаях будет несколько маршрутов, в этом случае будет связь один-ко-многим). поэтому будет один отношение -к-одному

### Чтобы запустить проект

Сначала клонируйте репозиторий

```
$ git clone https://github.com/AnerGcorp/scalaxi-carpark.git
$ cd scalaxi-carpark
```

Если вы используете Mac или Linux, выполните следующую команду

```
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

Для создания суперпользователя

```
$ python3 manage.py createsuperuser
```

Заполнить бланки

```
$ python3 manage.py runserver
```

Если вы в Windows выполните следующую команду

```
$ py -m virtualenv env
$ \\env\\bin\\activate
$ pip install -r requirements.txt
$ py manage.py makemigrations
$ py manage.py migrate
```

Для создания суперпользователя

```
$ py manage.py createsuperuser
```

Заполнить бланки

```
$ py manage.py runserver
```

Проект запускается на порту 8000 по умолчанию, откройте браузер и перейдите по адресу `http://localhost:8000/admin`, введите пользователя и пароль администратора, там вы сможете управлять парковкой.

Как вы увидите, когда автомобили добавляются или удаляются из автостоянки, общее количество автомобилей изменяется.
