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