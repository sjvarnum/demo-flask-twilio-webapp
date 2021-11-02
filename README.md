# Demo-Flask-Twilio-Webapp

This repository is a demonstration of a web app for sending test messages to contacts.

-   Create users who can send messages. The users are added to a database and authenticated when logging in.
-   Create new contacts to send messages to. In its current state, all contacts will get the message.
-   Creates a local database for development and testing.
-   Deploys to Heroku. Install PostgreSQL add-on in Heroku and the database and tables for users and contacts will be automatically created.
-   Uses Twilio for text messaging. Can probably be swapped out to use a different SMS platform.

## Requirements

### Heroku

If you want to test a deployed version of this, the app works with Heroku and PostgreSQL add-on. You will need to create environment variables for Flask secret key and Twilio account SID and auth token.

### Twilio

The texting platform is Twilio so you can set up an account on that platform. You will need your account SID and auth token. Also, investigate how to use the test credentials that come with your account so that you can test functionality without incurring any costs initially. Of course, you will need to test real text messaging at some point prior to production.

### Bootstrap 5

The app uses Bootstrap for styling.

## To Do

Some enhancements:

1. Add a home page with instructions - ## DONE
    - Currently you navigate to /auth/login or /message/create
    - There really isn't a home landing page at /
2. Add email notifications in addition to texts?
3. Improve stying
4. Add ability to add individual phone numbers to send message to.
5. Add ability to select contacts or contact groups based on roles and other parameters/tags (students, instructors, customers, employees, admins, etc.)

![](/docs/img/send-sms-from-pc.png)

## Some Screenshots

![](/docs/img/101.jpg)
![](/docs/img/102.jpg)
![](/docs/img/103.jpg)
![](/docs/img/104.jpg)
![](/docs/img/105.jpg)
![](/docs/img/106.jpg)
![](/docs/img/107.jpg)
![](/docs/img/108.jpg)
![](/docs/img/109.jpg)
![](/docs/img/110.jpg)
![](/docs/img/111.jpg)
![](/docs/img/112.jpg)
![](/docs/img/113.jpg)
![](/docs/img/114.jpg)
