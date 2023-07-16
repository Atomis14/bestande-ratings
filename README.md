# Bestande Ratings

Web UI to represent ratings from the discontinued Bestande app (https://bestande.ch/).

## Project Setup

1. install python3 and pip
2. run `python3 -m pip install flask`
3. run `python3 app.py` from root folder
4. app runs on http://127.0.0.1:5000/

### Docker

1. run `docker build bestande .`
2. run `docker run docker run -p 5002:5000 bestande` to run it on port 5002