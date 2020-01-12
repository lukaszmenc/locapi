# LocAPI
LocAPI is a JSON format backend REST API which allows to get geolocation information based on delivered IP or URL. It gets required data from ipstack.com API.

## Installation
Create the ```.env``` file in the root of the project and insert your key/value pairs in the format shown in ```.env.example``` file.

## Usage


### Run LocAPI
Run LocAPI locally using: 
```
docker-compose up --build
```
LocAPI will run on ```https://localhost:8000/```

### API endpoints

#### Authentication

| Endpoint               | HTTP method | Result          | Parameters                                  |
| :--------------------- |:----------: | :-------------: | :-----------------------------------------: |
| ```/auth/users```      | POST        | create new user | ```username```, ```email```, ```password``` |
| ```/auth/jwt/create``` | POST        | get JWT tokens  | ```username```, ```password```              |

#### Database operations

| Endpoint                 | HTTP method   | Result                            | Parameters                         |
| :----------------------- |:------------: | :-------------------------------: | :--------------------------------: |
| ```/geolocations```      | POST          | add new entry                     | ```ip``` or ```url```              |
| ```/geolocations```      | GET           | provide all geolocations entries  |                                    |
| ```/geolocations/:id```  | GET           | provide specific entry            |                                    |
| ```/geolocations/:id```  | DELETE        | delete specific entry             |                                    |

