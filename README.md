##Distinctiveness and Complexity
My app is designed for education and facilitating distribution of music to students within the Spanish music education system. Previous projects have not touched on this idea of distribution of specific data to personal accounts within the app and the ability to create a new musical part within the app. I have also utilised the ‘staff’ attribute allowing me to dynamically set what each user sees when using the authenticated features of the website.
I believe my app’s complexity satisfies the criteria as I have utilised various technology which we have seen throughout the course. I have included SASS, Javascript and incorporated technologies such as Docker to assist in deployment. I have created many more models than the project required and tackled code which had, in previous assignments, already been written for us, such as user authentication. I made the decision to process the filter results on the server as if there is a large number of results, this may take a long time using Javascript on the client.

##How to Run my Application
I have used Docker for my application utilising two containers. One for the web app and one for a Postgres database. To run the application simply use the `docker-compose up` command while in the main directory. This should pull the various images from Docker and build my application.

If you are starting with an empty database, you will need to create instruments in the admin panel. These instruments are:

Flauta
Oboe
Fagot
Trumpeta
Trompa
Trombon
Violin
Viola
Cello
Piano

##File Contents
**Static**
Within my JS folder, I have two files. “layout.js” is to control the dropdown menu on the mobile version of the site and the “part.js” is to control adding and removing a piece of music from a student’s account.

Within the “media” folder, I have various image files for implementation throughout the website.

The “scss” file contains the SCSS which is split into different files. Each page on the website has it’s own SCSS file and each of these files are then brought together within the ‘main.scss’ file. This file is then compiled and a single CSS file, which is found in the the “styles” folder and is utilised for the website. I used the “Live Sass Compiler” extension in VS Code to do this.

**Templates Folder**
Within the “templates” folder, I have included the HTML design for my project. The “layout.html” file is the base HTML file from which all the other pages extend. I have used Django template code throughout my HTML.

**Other Files**
Other files that I have created are the “Dockerfile” which outlines the container to build to host my web application. This utilised the “requirements.txt” file to set any pip apps that may be needed within my project.
The “docker-compose.yml” file brings together the web app and the Postgres database. This allows for an easier setup and sharing of code.
I also have a “.gitignore” file to exclude any files from a Git commit.
