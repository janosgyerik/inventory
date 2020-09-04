History
=======

The way the project was built from scratch.

---

Find a reasonable name. Imagining a future where Victoria uses this tool
on a daily basis, I imagined https://inventory.madametedart.com natural.
Hence the project name simply: "inventory".

Create dir and Git project.

Ignore `.idea`.

Initialize virtual env with `pipenv install`.

Install Django:

    pipenv shell
    pipenv install django
    
Open project in PyCharm:

- Open the base dir ("inventory")
- Configure Python interpreter:
    - Add new
    - Select pipenv option, click OK to find the one created by `pipenv` earlier
    - Verify the list of packages includes `django`

---

Create Django project, named after the project:

    django-admin startproject inventory

Copy scripts from bootstrap project.

Test run:

    ./manage.sh migrate
    ./run.sh
    ./manage.sh createsuperuser --username=admin --email=admin@localhost
    # visit site and login with admin

Create "crafts" app (because cannot be the same name as the site!):

    ./manage.sh startapp crafts
