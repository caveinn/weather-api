# Weather-Api

#### Api Documentation

> ## How to set up the project.

### Features.

- Python 3.9
- Django REST framework
- pipenv

---

### Installation.

- clone the repository

```
$ git clone https://github.com/caveinn/weather-api.git
```

- cd into the directory

```
$ cd weather-api
```

- Install dependencies

```
$ pipenv install
```

- After dependencies are installed, run the virtual environment

```
$ pipenv shell
```

- create environment variables
  On Unix or MacOS, run:

```
$ cp .env.example .env
```

The env should now have the following variables:

```
export WEATHER_API_KEY=<valid key>
export SECRET_KEY=<random string>
```

Note: There is no space next to '='

---

##### On terminal,

```
$ source .env
```

- Run the application

```
python mange.py run
```

- Testing the application

```
$ python manage.py test
```

- Testing code linting

```
$ flake8
```

---

## API documentation

> For the API documentation, the url is:

```
$ http://localhost:8000/api/docs/
```

- Expand the endpoint and click `try it out`

---