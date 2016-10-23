# ridecell
RideCell Coding Project

Populate Parking:


Initial Setup:
1. create a virual environment
2. git clone repository
3. You to install libpq-dev and python-dev
4. pip install -r requirements.txt
5. Install the GeoDjango required libraries:
- brew install postgresql
- brew install postgis
- brew install libgeoip
6. ./manage runserver


Example Curl Requests:

To create a new User:
curl -v -H "Content-Type: application/json" -X POST -d '{"username":"test@test.com","password":"123456"}' "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com/users/"
curl -v -H "Content-Type: application/json" -X POST -d '{"username":"test@test.com","password":"123456", "phone_number": "123456789"}' "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com/users/"
curl -v -H "Content-Type: application/json" -X POST -d '{"username":"test2@test.com","password":"123456", "phone_number": "123456789"}' "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com/users/"

To get/patch/put a user
curl -v -H "Authorization: Token {{ valid_access_token }}" "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/users/1/"
curl -v -H "Authorization: Token {{ valid_access_token }}" -H "Content-Type:application/json" -X PATCH -d '{"phone_number": 2222222222}'  "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/users/17/"
curl -v -H "Authorization: Token {{ valid_access_token }}" -H "Content-Type:application/json" -X PATCH -d '{"token": {{ valid_stripe_token}} }'  "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/users/17/"

To get access token for existing User:
curl -v -H "Content-Type:application/json" -X POST -d '{"username":"test@test.com","password":"123456"}' "http://ridecell.garyguo.ca/users/access_token/"

To get parking locations

curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/"
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/?latitude=43.761539&longitude=-79.433088&distance=1000"
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/?latitude=43.761539&longitude=-79.433088&distance=100"
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/?price=400"
curl -v "http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/parking/?latitude=43.761539&longitude=-79.433088&distance=1000&price=400"


To make a reservation
curl -v -H "Authorization: Token {{ valid_access_token }}" -H "Content-Type:application/json" -X POST -d '{"parking_location_id":"1"}' http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/reservations/

To get/patch/put/delete a reservation
curl -v -H "Authorization: Token {{ valid_access_token }}" http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/reservations/2/
curl -v -H "Authorization: Token {{ valid_access_token }}" -H "Content-Type:application/json" -X PATCH -d '{"parking_location_id": 2}' http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/reservations/2/
curl -v -H "Authorization: Token {{ valid_access_token }}" -X DELETE http://ec2-54-201-57-60.us-west-2.compute.amazonaws.com:8000/reservations/2/
