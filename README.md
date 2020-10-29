# Django-Blog-Application
Hello everyone,

I created a basic blog application in Django in case you would like to use as a base and build any of your requirements on it.

Just to make sure that you have something to view inside of the application, I also included db.sqlite3, which includes a few posts, comments and categories.
In case you would like to see the live version of my blog application, you can always visit my page using the link: <a href="https://www.ozan.pl">Ozan.pl</a>.

To be able to use the blog application, you firstly need to clone in your local computer:

```
git clone https://github.com/ozntel/Django-Blog-Application.git
```

Then please create a new virtual environment in desired path and activate:

```
virtualenv -p python3 BlogAppEnv
source BlogAppEnv/bin/activate
```

Then navigate to the project directory you cloned from github and install the requirements just to make sure that you have all required packages installed:

```
pip install -r requirements.txt
```

Now you need to make migration and migrate, so please go to directory of project and use the commands below:

```
python manage.py makemigrations
python manage.py migrate
```

Within the database, as I mentioned, you will have sample posts, comments and categories, which you can edit from the admin page. I also included the admin page within the main page.

You can initially use these credentials:

```
Username : superuser
Password : 123456
```

or you can simply create a superuser for yourself using the following command:

```
python manage.py createsuperuser
```

The logic of the application is really simple. You have main view, where you can see all of the posts that have status "visible". In case you want users to write a post in your page, the post will not be visible initially and you can change the status after checking the content.

The same rule is applicable for comments. When the comment is submitted, the visible status is set to False and you need to change the status to True to make them visible in the page.

I have a separate application created for notifications and both user and superuser receive a message from the system once a post or comment is submitted so that it can be approved immediately. 

There is a separate page created, in which users can view their posts even though it is not approved yet. The status of the post is also visible in this specific page on the right bottom of post list element. 

Within the project, I included also TINYMCE, which makes easier to edit the content. However, the link is created for me so please register to TINYMCE and get your own link. Otherwise, you will always receive a notification that your domain is not registered, however, you can still ignore this notification and use the editor. 

In case you have any question, please feel free to use link <a href="https://www.ozan.pl/contact/">Ozan.pl Contact</a>. I will be happy to help if I am capable of.

Regards,
Ozan Tellioglu
