* Create a new virtual environment and install all the dependencies
* start the `RabbitMQ` server, either install it or run a docker file `docker run -p 5672:5672 -p 15672:15672 rabbitmq`
* Access the messaging queue web interface `http://localhost:15672`
* Run the `main.py` file `python main.py`
* Start the Celery Worker `celery -A tasks worker --loglevel=info`
