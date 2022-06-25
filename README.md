# Phone_Book

## Project Statement
The goal of this project is to create a simple phone book application with CRUD operations. 

## Project Features - 
1. The application provides a form where you can enter in first name, last name, and phone number. 
2. You should then be able to perform 4 basic operations: create new entries in your database, read the entries, update entries by editing any of the properties, and      delete the entries. 

## Project Implementation Details -

1. Database Used - MySQL
2. Created API for all 4 basic CRUD operations

## --------------------------------------------------------------------------------------------------------

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This is a simple Phone book where we add, update, delete, and get all the contactthe s from the database using API.

## Technologies
Project is created with:
* Python 3.9
* Django 3.1.1
* Django Rest Framework 3.12.4
* MySQL Server

## Setup

1. Installation
      * Install Python 3.9 from [Python](https://www.python.org/downloads/).
      * To install Django, open Terminal/Command prompt and run the following command
      ```
      pip install django==3.1.1
      ```
      * To install Django Rest Framework, open Terminal/Command prompt and run the following command
      ```
      pip install djangorestframework==3.12.4
      ```
      * Install MySQL Server from [MySQL](https://dev.mysql.com/downloads/mysql/).
      * Install Postman from [Postman](https://www.postman.com/downloads/).

    2. Download the zip and extract it.

3. After Setting up your MySQL server, create a Database with name "phonebook" and Enter the user and Password of root user in phonebook/settings.py
    
   ![Screenshot (67)](https://user-images.githubusercontent.com/83489527/175766740-ec8bcf17-622e-4375-a21b-7a83dd3c22dd.png)

    
4. Right click in the folder and select *Open in Terminal* and run the following command
      ```
      python manage.py makemigrations
      ```
      ```
      python manage.py migrate
      ```

      ```
      python manage.py runserver
      ```
5. You will see something like this.

    ![new](https://user-images.githubusercontent.com/83489527/171010571-b4823253-a8c7-4571-9915-e9a617296c3f.jpg)

6. Now, Open Postman and select the bottom right cornor icon for better view and click on 'Body' and select **raw** **JSON**

    ![video_image-S4vD713DpZ](https://user-images.githubusercontent.com/83489527/175374385-4d78eefa-0d32-4f51-8391-6ae791a1acd8.jpeg)


# --------------------------------------------------------------------------------------------------------

# CRUD OPERATIONS
 
  * Add New Entry :
    
    Select "POST" method and add data as shown and click on Submit. Enter the following URL in URL field.
      
       ```
       http://127.0.0.1:8000/api/contact/
       ```
    
      ![Screenshot (69)](https://user-images.githubusercontent.com/83489527/175768809-90c7c4c1-1ad7-44d9-a1d6-2d21dfbac010.png)

  
  * Read Entries :
      
    Select "GET" method and click on Submit. Enter the following URL in URL field.
    
       ```
       http://127.0.0.1:8000/api/contact/
       ```
    
      ![Screenshot (70)](https://user-images.githubusercontent.com/83489527/175768813-e1160a76-994c-4d05-bc8d-4f17eed411c0.png)

  
  * Update an Entry :
    
    Select "PUT" method and add data as shown and click on Submit. Enter the following URL in URL field.
    
       ```
       http://127.0.0.1:8000/api/contact/ + id + /
       ```
    
       ![Screenshot (71)](https://user-images.githubusercontent.com/83489527/175768817-a3dd21b0-aed2-48d1-b6a2-42a368e1252e.png)

  * Delete an Entry :
    
    Select "DELETE" method click on Submit. Enter the following URL in URL field.
        
       ```
       http://127.0.0.1:8000/api/contact/ + id + /
       ```
    
       ![Screenshot (72)](https://user-images.githubusercontent.com/83489527/175768833-199794a7-62b1-4bf3-91f2-89f5c5f23785.png)


      
      
      
    
    
     
  

