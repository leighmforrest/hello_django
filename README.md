# HELLO DJANGO

A boilerplate Django project for you! Uses a custom user, pytest, django-pytest. 

---

## Github Actions

To push code to your server via GitHub actions, please set up the following repository secrets:

| Variable | Value |
| ----------- | ----------- |
| APP_DIRECTORY | Absoulte path of the project directory on the server.        |
|PRIVATE_KEY | The private key found on your local machine that is used to SSH into the VPS server.
| SERVER_IP | IP address of the VPS server.|
| USERNAME | Username of the sudo user on the VPS.

## Static Files

To properly render your static files on your VPS using nginx, add this line to the top of `/etc/nginx/nginx.conf` file:

`user <APP_USER>;` Otherwise, your project's static files may not have permission to put them on the page.