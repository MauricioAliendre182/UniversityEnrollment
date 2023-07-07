# University Enrollment Project
## V 1.0

## Description
This is a Django project to create a page to enroll students to different subjects.

There are five main sections:

* Student
* Course
* Career
* Enrollment
* Contact

In the **Student** section we have the following:

![Django1](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/3c69297e-86b0-4728-8eb7-4a56360eaed6)

In the **Course** section we have the following:

![Django2](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/2571aa65-79c9-4407-afae-d945617b17ef)

In the **Career** section we have the following:

![Django3](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/2c6f6c5b-af6f-40eb-adf6-5577709539ba)

In the **Enrollment** section we have the following:

![Django4](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/d3856bea-9e0a-4a2e-99d5-71ed53cfe98e)

In the **Contact** section we have the following:

![Django5](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/dd259950-06c3-49a1-bc30-e2fa25d679de)

To configure the SMTP server you will need a gmail account, you need to annotate your credentials in the file **settings.py** 

![Django6](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/04f830d8-f00f-4203-8591-81bd9047182d)

To get the password it is neccesary to allow less secure app access, for that, you can go to [app password account](https://myaccount.google.com/u/0/apppasswords) and configure a new app password, you can use this [video](https://www.youtube.com/watch?v=Y_u5KIeXiVI) as guidance 

## Features and Tools
- Windows x64
- Django
- PostgreSQL
- Docker and docker-compose
- Postman

## Installation


### First Step: Install Docker
> Go to the next link: https://docs.docker.com/desktop/install/windows-install/ and install Docker for windows

![image](https://user-images.githubusercontent.com/86843637/208322964-ba2a4134-e02a-462c-be26-5408523e8b54.png)

> Open Docker Desktop

![image](https://user-images.githubusercontent.com/86843637/208489175-9bfed906-4b0f-408d-9f04-d01bfe514ce2.png)

### Second Step: Copy the repository

```bash
git clone https://github.com/MauricioAliendre182/UniversityEnrollment.git
```
```bash
cd UniversityEnrollment/UniversityManagement
```

### Third Step: Execute docker-compose up
> Firstly you have to check the docker compose version that you have

![image](https://user-images.githubusercontent.com/86843637/208323872-d7946d27-9505-4603-94cd-983c1c66b44a.png)

> Secondly go to the `docker-compose.yml` file and verify if the version matches, If that is not the case change the version to the docker-compose version

![image](https://user-images.githubusercontent.com/86843637/208324014-22ee7792-0c02-4099-8149-8c50c112e0ab.png)

> Thirdly, uncomment the line 20 and comment the line 21 in the file **docker-compose.yml**, this is to make the migrations and have the tables created

![Django7](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/ca449968-14aa-421f-8aaa-e14bf784b2de)

> Fourthly, execute the command `docker-compose up` on your terminal, the corresponding images will be dowonload and the containers will be active

> Fifthly, once the containers were created execute `docker-compose down` or stop the containers from **Docker Desktop**

> Lastly, uncomment the line 21 and comment the line 20 in the file **docker-compose.yml** and execute `docker-compose up` once again


## API
The project counts with API service, the endpoints are the following:

* http://localhost:8000/academic/api/v1/token/
* http://localhost:8000/academic/api/v1/token/refresh/
* http://localhost:8000/academic/api/v1/students/
* http://localhost:8000/academic/api/v1/students/<pk>/
* http://localhost:8000/academic/api/v1/courses/
* http://localhost:8000/academic/api/v1/courses/<pk>/
* http://localhost:8000/academic/api/v1/career/
* http://localhost:8000/academic/api/v1/career/<pk>/
* http://localhost:8000/academic/api/v1/enrollment/
* http://localhost:8000/academic/api/v1/enrollment/<pk>/

To use the endpoints it is neccesary to request a **token** for that we will use the first endpoint

![Django8](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/45c4d875-a0da-48e5-b7c9-7f8c2e4c8f90)

Copy the token in the "access" field and paste it in the **Authorization** header with the word **Bearer** in front of it

![Django9](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/f0310bdf-4b8c-45cb-b8dc-e493b3b491af)


## Result
You can access to the link: http://localhost:8000/academic/register/ to start interact with the application

![Django10](https://github.com/RodrigoValda/TestTitanWordpress/assets/86843637/ec41af91-d11b-4ee9-88e4-7b98869444b4)

## License

This project is free an can be used for anyone
