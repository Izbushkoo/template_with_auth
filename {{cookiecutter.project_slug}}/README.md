# Begin
## Project directory must contain .env file with given in example.env variables to start your coding.

## To begin you need to up compose stack using:
    docker compose -f compose_stack.yml up -d

### Your application container name will correspond with "project_slug": {{ cookiecutter.project_slug }}

## if you need to recreate services use '--build' flag

    docker compose -f compose_stack.yml up --build -d

## even can explicitly point which one by means of:

    docker compose -f compose_stack.yml up --build {{ cookiecutter.project_slug }}

## to make migration you can execute command inside docker app container like this:

    docker container exec {{ cookiecutter.project_slug }}_app poetry run alembic upgrade head
**'poetry run'** part is needed because pure dockerfile creates environment inside the container. There is no need to do it
but that's my preference


# Create a GitHub Repo

Go to your GitHub account and create a new repo that matches the **{{ cookiecutter.project_slug }}** 
Back to your CLI, you can do the following in the root of your generated project:
    
    git init
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:<MY_USERNAME>/<MY-REPO-SLUG>.git
    git push -u origin master

