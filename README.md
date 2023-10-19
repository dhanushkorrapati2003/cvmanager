# CV Manager
This is a CV manager where users can upload, search, view and delete the resumes that they uploaded.

## Instructions for setup and things to take note of 
### 1. Setup your Database
- Modify the DATABASES variable in the settings.py file accordingly. I have used a local MYSQL database during development. It varies from machine to machine, so connect it to your own database.
- After setting up the database, run **python manage.py makemigrations** to make the migrations and apply the migrations with **python manage.py migrate**. This will bring your database up to speed.
### 2. File structure
**Note:** Only deviations from the standard django file structure are mentioned. Others are to be assumed as default.

- The app inside the project is called **upload**. The templates folder contains an admin folder in which all the files for the admin route are kept.
- There is a views folder in which views belonging to a route are kept in a single file.
- There's a validators.py file which contains the validator to check the file size of resume upload.

### 3. File Uploads
Currently, all files uploaded are set to be stored in the media folder in the project. The MEDIA_ROOT and the MEDIA URLs are set in the settings.py file for this purpose. When deploying, this can be set to an S3 bucket or it's equivalent in other cloud providers.

### 4. Routing
- **/admin** route won't take you to Django Admin. It will take you to the admin mode of the website.
- To access Django admin, the route is **/admindjango** .
- Hitting the URL will take you to **/search** by default if logged in or to **/login** if not logged in.

### Imp: Dependencies
- There's a requirements.txt file which contains all the requirements needed to run the project. Use **pip** installer to install all the dependencies. 
- **DO NOT** forget to create and actiavte a virtual environment before installing all the requirements. Working on this project in a virtual environment will help you avoid any dependency clashes.


## Some Intuition behind the project
### 1. Only admin can create new users
So, there's no need for a Sign Up page.
### 2. Only admin can see the logs behind a cadidate's details.
So, only admin will have the option view history.
### 3. Non-admins will only see the details that they uploaded.
So, there's a filter in the search view for the non-admin users to display only details uploaded by them.


