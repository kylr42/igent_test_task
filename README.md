# Dockerizing Django with Postgres, Gunicorn, Redis, Celery and Nginx

## Want to use this project?

### Development

Uses the default Django development server.
1. Update the environment variables in the *docker-compose.yml* and *.env.dev* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```
Test it out at [http://localhost:8000](http://localhost:8000). The ```"app"``` folder is mounted into the container and your code changes apply automatically.
<br><br>

Get the following error? 
>django.db.utils.OperationalError: FATAL:  database ```"postgres"``` does not exist

Run ```docker-compose down -v``` to remove the volumes along with the containers. Then, re-build the images and run the containers.
<br><br>

### Production

Uses gunicorn + nginx.

1. Update the environment variables in the *docker-compose.yml*, *.env.prod.db* and *.env.prod* files.
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

Test it out at [http://localhost](http://localhost). No mounted folders. To apply changes, the image must be re-built.
