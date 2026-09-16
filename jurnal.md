# DJ-CAR-ZONE
## Build Python Django Real Project: Django Web Development

## Section 1: Introduction
#### 1.1 Introduction
		Pass
#### 1.2 Full Project Overview
		Pass
#### 1.3 Keys To Course Success
		Pass
#### Initial commit

        modified:   .gitignore
        new file:   jurnal.md


## Section 2: Setup

#### 2.1 Install Sublime & Cmder
		Pass
#### 2.2 Windows and Project Location
		Pass
#### 2.3 Create & Clone Remote Repository
		Pass

#### 2.4 Create Virtual Environment and Install Django

		$ python --version
		Python 3.13.0

		$ python -m pip --version
		pip 26.2.1 from C:\laragon\bin\python\python-3.13\Lib\site-packages\pip (python 3.13)

		$ python -m venv venv31361

		$ source venv31361/Scripts/activate
		(venv31361)

		$ python -m pip install django
		Collecting django
		  Using cached django-6.1.1-py3-none-any.whl.metadata (3.9 kB)
		...
		Successfully installed asgiref-3.12.1 django-6.1.1 sqlparse-0.6.0 tzdata-2026.4

		$ python.exe -m pip install --upgrade pip
		...
		Successfully installed pip-26.2.1

		$ django-admin --version
		6.1.1

		$ touch requirements.txt
		$ python -m pip freeze > requirements.txt

        modified:   jurnal.md
        new file:   requirements.txt

#### 2.5 Create Django Project

		$ django-admin startproject config .

		$ tree config
		config
		|-- __init__.py
		|-- asgi.py
		|-- settings.py
		|-- urls.py
		`-- wsgi.py

#### 2.6 Create Django App

		$ mkdir apps
		$ python manage.py startapp pages apps/pages
		$ tree apps -L 2
		apps
		`-- pages
		    |-- __init__.py
		    |-- admin.py
		    |-- apps.py
		    |-- migrations
		    |-- models.py
		    |-- tests.py
		    `-- views.py

#### 2.7 Register the pages app and Display Hello World

        modified:   apps/pages/apps.py
        modified:   apps/pages/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   jurnal.md

		$ python manage.py check
		System check identified no issues (0 silenced).
		(venv31361)

		$ python manage.py runserver
		Watching for file changes with StatReloader
		Performing system checks...

		System check identified no issues (0 silenced).

		You have 18 unapplied migration(s). Your project may not work properly until you apply the migration
		s for app(s): admin, auth, contenttypes, sessions.
		Run 'python manage.py migrate' to apply them.
		September 15, 2026 - 19:20:29
		Django version 6.1.1, using settings 'config.settings'
		Starting WSGI development server at http://127.0.0.1:8000/
		Quit the server with CTRL-BREAK.


#### 2.8 Update Remote Repository

		$ git push -u origin main
		Enumerating objects: 44, done.
		Counting objects: 100% (44/44), done.
		Delta compression using up to 4 threads
		Compressing objects: 100% (38/38), done.
		Writing objects: 100% (42/42), 6.66 KiB | 758.00 KiB/s, done.
		Total 42 (delta 15), reused 0 (delta 0), pack-reused 0 (from 0)
		remote: Resolving deltas: 100% (15/15), completed with 1 local object.
		To https://github.com/ingskillsetstraining/dj-car-zone
		   700d6a0..75ad5b9  main -> main
		branch 'main' set up to track 'origin/main'.


## Section 3: Templates, Views, Urls

#### 3.1 Create Home Page

        new file:   apps/pages/templates/pages/home.html
        new file:   apps/pages/urls.py
        modified:   apps/pages/views.py
        modified:   config/urls.py
        modified:   jurnal.md

#### 3.2 Create Other Pages

        new file:   apps/pages/templates/pages/about.html
        new file:   apps/pages/templates/pages/cars.html
        new file:   apps/pages/templates/pages/contact.html
        new file:   apps/pages/templates/pages/services.html
        modified:   apps/pages/urls.py
        modified:   apps/pages/views.py
        modified:   jurnal.md


## Section 4: Html Template, Static & Media Files

#### 4.1 Activating Django Templates and Moving Template Pages

        modified:   config/settings.py
        modified:   jurnal.md
        renamed:    apps/pages/templates/pages/about.html -> templates/pages/about.html
        renamed:    apps/pages/templates/pages/cars.html -> templates/pages/cars.html
        renamed:    apps/pages/templates/pages/contact.html -> templates/pages/contact.html
        renamed:    apps/pages/templates/pages/home.html -> templates/pages/home.html
        renamed:    apps/pages/templates/pages/services.html -> templates/pages/services.html

#### 4.2 Add Template to Home Page

        modified:   jurnal.md
        modified:   templates/pages/home.html

#### 4.3 Static and Media Files Configuration

        modified:   config/settings.py
        modified:   config/urls.py

#### 4.4 Loding Static and Media Files

        modified:   .gitignore
        modified:   config/urls.py
        modified:   jurnal.md
        modified:   templates/pages/home.html

#### 4.5 Create and Load Base Template

        modified:   apps/pages/views.py
        modified:   jurnal.md
        new file:   templates/base.html

#### 4.6 Extends base.html to home page

        modified:   apps/pages/views.py
        modified:   jurnal.md
        modified:   templates/pages/home.html

#### 4.7 Template Inheritance

        modified:   jurnal.md
        modified:   templates/base.html
        modified:   templates/pages/home.html

#### 4.8 Partials and Include

        modified:   jurnal.md
        modified:   templates/base.html
        modified:   templates/pages/home.html
        new file:   templates/partials/1_top_header.html
        new file:   templates/partials/2_main_header.html
        new file:   templates/partials/3_intro_section.html
        new file:   templates/partials/4_footer.html
        new file:   templates/partials/5_page_search.html
        new file:   templates/partials/6_modal.html
        new file:   templates/partials/7_scripts.html

#### 4.9 Components and Include

        modified:   jurnal.md
        new file:   templates/pages/components/home/1_slider.html
        new file:   templates/pages/components/home/2_featured_car.html
        new file:   templates/pages/components/home/3_latest_car.html
        new file:   templates/pages/components/home/4_team.html
        modified:   templates/pages/home.html

#### 4.10 Pages Template Implementation

        modified:   config/urls.py
        modified:   jurnal.md
        modified:   templates/pages/about.html
        modified:   templates/pages/cars.html
        modified:   templates/pages/contact.html
        modified:   templates/pages/services.html

#### 4.11 Dynamic Navigation Link

        modified:   jurnal.md
        modified:   templates/partials/2_main_header.html

#### 4.12 Adding Active State to Menu

        new file:   apps/pages/templatetags/__init__.py
        new file:   apps/pages/templatetags/navigation_tags.py
        modified:   jurnal.md
        modified:   templates/base.html
        modified:   templates/partials/2_main_header.html
