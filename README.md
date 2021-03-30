# ProteinRate
Simple Django webpage featuring short reviews of protein shakes

Visit live production page at https://protein.yellowtech.ch/

I will add a SQL dump of my reviews as soon as I've collected a few.

# Start your own page using Docker:
(can also run using the django development server)

Clone repo to a local folder.

Add ```secret.py``` in the ProteinRate subfolder following the example of ```secret.example.py```.

To use the admin page we need to collect all static files using the Django script ```manage.py```. For this we need a Python 3 installation with ```django``` installed from pip (prefferably a venv). To collect all static files use ```python manage.py collectstatic```

Build and start the Docker setup using docker-compose by ```docker-compose up -d --build``` (may need ```sudo```, stop it using ```docker-compose down```)

Visit http://localhost:8000 and log in at http://localhost:8000/secretadmin using admin admin


Please use a reverse proxy to secure the installation with HTTPS and change default admin password
