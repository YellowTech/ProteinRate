# ProteinRate
Simple Django webpage featuring short reviews of protein shakes

Visit live production page at https://protein.yellowtech.ch/

# Start your own page using Docker:
(can also run using the django development server)

Clone repo to a local folder.

Add ```secret.py``` in the ProteinRate subfolder following the example of ```secret.example.py```.

Build and start the Docker setup using docker-compose by ```docker-compose up -d --build``` (may need ```sudo```, stop it using ```docker-compose down```)

Visit http://localhost:8000 and log in at http://localhost:8000/secretadmin using admin admin


Please use a reverse proxy to secure the installation with HTTPS
