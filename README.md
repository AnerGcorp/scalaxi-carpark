## Car Park Database Design

There are five tables `OwnerCarPark`, `CarPark`, `CarDriver`, `Car` and
`CarRoute`. Let's define the relationships of models(tables)

- `OwnerCarPark` and `CarPark`, there are two different scenarios, `OwnerCarPark` can have many `CarPark`s or one `CarPark` => so there will be one-to-many relationship
- `CarPark` and `Car`, a `CarPark` can have many `Car`s, so there are also one-to-many relationship
- `CarDriver` and `Car`, a `Car` has only one `CarDriver`, so there will be one-to-one relationship
- `Car` and `CarRoute`, a `Car` has only one `CarRoute` (in some cases there will be multiple route, if that is the case then there will be one-to-many relationship.) so there will one-to-one relationship

### To run the project

First clone the repository
$ git clone https://github.com/AnerGcorp/scalaxi-carpark.git
$ cd scalaxi-carpark

If you on mac or linux run the following command
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py makemigrations
$ python3 manage.py migrate

For creating super user
$ python3 manage.py createsuperuser
Fill the blanks
$ python3 manage.py runserver

If you on windows run the following command
$ py -m virtualenv env
$ \\env\\bin\\activate
$ pip install -r requirements.txt
$ py manage.py makemigrations
$ py manage.py migrate

For creating super user
$ py manage.py createsuperuser
Fill the blanks
$ py manage.py runserver

Project runs on default port 8000, open the browser and head to `http://localhost:8000/admin``, enter the admin user and password there you can manage car park.

As you will see when the cars added or deleted to the car park the total number of cars are changed.
