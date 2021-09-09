# Django service that works via the VK API and duplicates group messages in VK to a group chat in Telegram.

## Tasks
1. Receives messages within the VK group
1. Saves to Postgres database
1. Sends a message to a group in Telegram

### Required Field
- `TG_TOKEN`: The Telegram Bot Token that you got from [@BotFather](https://t.me/BotFather)
- `TG_CHAT_ID`: This is to authenticate your Telegram chat id. You can get this from [@getmyid_bot](https://t.me/getmyid_bot)

- `VK_TOKEN`: The Vk Bot Token that you got from [vk.com](https://vk.com/dev/access_token)

## Want to use this project?

- Using Docker-compose, you can edit and build your image in seconds:
```
sudo apt install docker-compose
```
- Build and run Docker image:
```
sudo docker-compose up
```
- After editing files with nano for example (nano start.sh):
```
sudo docker-compose build
sudo docker-compose up
```
OR
```
sudo docker-compose up --build
```
- To stop Docker: 
```
sudo docker ps
```
```
sudo docker stop id
```
- To clear the container (this will not affect the image):
```
sudo docker container prune
```
- To delete the image:
```
sudo docker image prune -a
```
- Video from Tortoolkit repo
<p><a href="https://youtu.be/c8_TU1sPK08"> <img src="https://img.shields.io/badge/See%20Video-black?style=for-the-badge&logo=YouTube" width="160""/></a></p>

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
