#RideCell Coding Project

##Initial Setup:
1. create a virual environment
2. git clone repository
3. You need to install libpq-dev and python-dev
4. pip install -r requirements.txt
5. Install the GeoDjango required libraries:
    - brew install postgresql
    - brew install postgis
    - brew install libgeoip
6. ./manage runserver


##Example Curl Requests:

###To create a new User:
```
curl -v -H "Content-Type: application/json" -X POST -d '{"username":"test@test.com","password":"123456"}' "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com/users/"
curl -v -H "Content-Type: application/json" -X POST -d '{"username":"test@test.com","password":"123456", "phone_number": "123456789"}' "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com/users/"
```

###To get/patch/put a user
```
curl -v -H "Authorization: Token {{ valid_access_token }}" "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/users/1/"
curl -v -H "Authorization: Token {{ valid_access_token }}" -H "Content-Type:application/json" -X PATCH -d '{"phone_number": 0000000000}'  "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/users/1/"
curl -v -H "Authorization: Token {{ valid_access_token }}" -H "Content-Type:application/json" -X PATCH -d '{"token": {{ valid_stripe_token}} }'  "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/users/1/"
```

Note that stripe tokens can be obtained from the "Stripe Token" button at http://ridecell.garyguo.ca

###To get access token for existing User:
```
curl -v -H "Content-Type:application/json" -X POST -d '{"username":"test@test.com","password":"123456"}' "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/users/access_token/"
```

###To get parking locations
```
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/"
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/?latitude=43.761539&longitude=-79.433088&distance=1000"
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/?latitude=43.761539&longitude=-79.433088&distance=100"
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/?price=400"
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/?latitude=43.761539&longitude=-79.433088&distance=1000&price=400"
```


###To make a reservation
```
curl -v -H "Authorization: Token {{ valid_access_token }}" -H "Content-Type:application/json" -X POST -d '{"parking_location":1}' http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/reservations/
```
###To get/patch/put/delete a reservation
```
curl -v -H "Authorization: Token {{ valid_access_token }}" http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/reservations/2/
curl -v -H "Authorization: Token {{ valid_access_token }}" -H "Content-Type:application/json" -X PATCH -d '{"parking_location":2}' http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/reservations/2/
curl -v -H "Authorization: Token {{ valid_access_token }}" -X DELETE http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/reservations/2/
```


###To View Reservation History
```
curl -v -H "Authorization: Token 67c6e15089d7fe51f5a5365e89f95e539137f49b" -H "Content-Type:application/json" -X POST -d '{"parking_location":1}' local.ridecell.co:8000/reservations/
curl -v -H "Authorization: Token 67c6e15089d7fe51f5a5365e89f95e539137f49b" -H "Content-Type:application/json" local.ridecell.co:8000/reservations/history/
curl -v -H "Authorization: Token 67c6e15089d7fe51f5a5365e89f95e539137f49b" -H "Content-Type:application/json" "local.ridecell.co:8000/reservations/history/?limit=5&offset=5"
curl -v -H "Authorization: Token 67c6e15089d7fe51f5a5365e89f95e539137f49b" -H "Content-Type:application/json" local.ridecell.co:8000/reservations/history/?start_datetime="2016-11-14T22:33:48.471607"
curl -v -H "Authorization: Token 5c90863be399d30b55f68350d56a3e151e275e6b" -H "Content-Type:application/json" local.ridecell.co:8000/reservations/history/
```

###To Extend A Reservation
```
curl -v -H "Authorization: Token 67c6e15089d7fe51f5a5365e89f95e539137f49b" -H "Content-Type:application/json" local.ridecell.co:8000/reservations/16/
curl -v -H "Authorization: Token 67c6e15089d7fe51f5a5365e89f95e539137f49b" -H "Content-Type:application/json"  -X PATCH -d '{"extension_in_minutes":60}' local.ridecell.co:8000/reservations/16/extend/
```

###To Create Alerts
```
curl -v -H "Authorization: Token 5c90863be399d30b55f68350d56a3e151e275e6b" -H "Content-Type:application/json" -X POST -d '{"time_start":"2016-11-15T12:30:00", "time_end": "2016-11-15T14:30:00", "latitude":43.761539, "longitude":-79.433088, "radius":50 }' local.ridecell.co:8000/alerts/
curl -v -H "Authorization: Token 5c90863be399d30b55f68350d56a3e151e275e6b" -H "Content-Type:application/json" -X POST -d '{"time_start":"2016-11-15T12:30:00", "time_end": "2016-11-14T14:30:00", "latitude":43.761539, "longitude":-79.433088, "radius":50 }' local.ridecell.co:8000/alerts/
curl -v -H "Authorization: Token 5c90863be399d30b55f68350d56a3e151e275e6b" -H "Content-Type:application/json" -X POST -d '{"time_start":"2016-11-15T14:30:00", "time_end": "2016-11-15T16:30:00", "latitude":43.761539, "longitude":-79.433088, "radius":100 }' local.ridecell.co:8000/alerts/
```

Note that ridecell.alerts.tasks.process_alerts_periodic_task is the periodic task to simulate creation of alerts