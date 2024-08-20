# Paul's Pizzeria

This is a Django based website for a restaurant with a contact page and online booking system. Users can log in and book online, and also edit and cancel their bookings from the website. Users can also see the menu, all contact details and the address of the website. Every page on this website is fully responsive for all screen sizes.

[Live Link](https://pauls-pizzeria-9a41d2e84409.herokuapp.com/)

![Am I responsive](/readme/readme_images/am_i_responsive.png)

## Features

### Navbar

The navigation bar allows access to all other pages and when viewing in tablet screens and smaller, it turns into a drop down menu. When logged in, the button on the right changes to a logout button, and adds a 'my bookings' link next to the book now link.

![Nav Bar](/readme/readme_images/header.png)

### Footer

The footer displays a shorthand version of the opening times, the address, working social media and email links, and copyright information.

![Footer](/readme/readme_images/footer.png)

### Home Page

The left hand side of my home page consists of the name and brief description of the restaurant and an image. The right hand side consists of the opening times, location and phone number, with nav links to the menu and booking page.

![Home Page Left](/readme/readme_images/home.png)

### Menu

The menu page is a static page that shows the menu and prices.

![Menu](/readme/readme_images/menu.png)

### Contact Page

This is a contact form for users to fill out for large table bookings, parties, and other general enquiries. This form can be accessed by the site owner through the admin page. These forms are stored in the order of most recent at the top. I used crispy forms to create this.

![Contact form](/readme/readme_images/contact.png)

![Admin page](/readme/readme_images/admin-contact.png)

### Booking Page

This page is where the user books a table. The name and email are autofilled from the login information. User is unable to select a previous date and will throw an error if the user tries to book a past time. The time slots available are every half an hour between 12pm and 9pm from Wednesday - Sunday. You cannot book outside of these times. User can only book a table between 1 and 8 people, otherwise will throw an error. All fields are required to be filled in. I used crsipy forms to create this.

![Booking form](/readme/readme_images/booking.png)

This form is stored to the database as a booking form and then automatically assigns to an available table. Once the booking has a table assigned to it, it is stored to the database as a reservation. The booking is assigned to the table for a 2 hour slot. If a table is not available for the user at their desired time, it will throw an error, notifying the user their is no available table at this time.

This is an overview of the admin page. I used summernote for the admin page.

![Admin page](/readme/readme_images/admin-home.png)

This is the booking form page on the database.

![Booking form page](/readme/readme_images/admin-booking.png)

These are the tables in the database, in which the booking assigns to.

![Tables page](/readme/readme_images/admin-table.png)

These are the reservations on the database. These represent the booking form assigned to the table. This is where the site owner will go to when checking if they have any bookings. Reservations are automatically ordered by time. The site owner can filter by date, so that they can see what bookings they have today for example, and assigned on, so they can see if any new bookings have come through. They can also search by name if they need to find a specific booking.

![Reservations page](/readme/readme_images/admin-reservation.png)

### My Bookings Page

Once a users booking is stored as a reservation, it can be accessed by the user on this page, in order to view, edit, or cancel the booking. If you change your time or date, or number of guests, and their is not an available table, it will throw an error. The user can only view, edit, or cancel their own bookings.

![My Bookings Page](/readme/readme_images/mybookings.png)

![Edit booking page](/readme/readme_images/edit-booking.png)

![Cancel booking page](/readme/readme_images/cancel-booking.png)

### Authentication

In order to book a table, and view, edit or cancel your bookings, you must be logged into your account, otherwise this is unaccessable. I created authentication using allauth.

![Sign up](/readme/readme_images/signup.png)

![Sign in](/readme/readme_images/signin.png)

![Sign out](/readme/readme_images/signout.png)

## Design Process

### User Stories

I created [user stories](https://github.com/users/PaulR1209/projects/2) to outline what features I wanted and needed to add into my project.

### Planning

From here I was able to roughly figure out what models and database schema I needed to achieve completing my user stories. I sketched out the models and design in a notepad, by hand.

### Logo

I created my logo on [Leonardo AI](https://app.leonardo.ai/)

### Color Theme

I then took the colors of my logo and decided on a theme of an Italian red #CD212A, black and white.

### Background Image

I then found a stock photo of a pizza for my background image to fit with the color and restaurant theme. I found this on [Pexels](https://www.pexels.com/).

### Typography

The font family I used for all of my typography is Roboto.

## Models

### Authentication

I used Allauth to create the authentication. I used the Django Blog walkthrough project as a step by step guide to get this fully functioning, and I stuck with the default fields.

### Contact Page

I used crispy forms alongside custom CSS to build the contact form. 

#### Fields:

- `name`: CharField
- `email`: EmailField
- `phone`: PhoneNumberField
- `subject`: CharField
- `message`: TextField
- `created_on`: DateTimeField(auto_now_add=True)

#### Relationships:

If a `user` is logged in, the `name` and `email` fields automatically fill with the users name and email.

### Booking Form

This model represents the booking form used to submit a booking

#### Fields:

- `user`: ForeignKey: User ID of the user booking
- `name`: CharField: name of the user booking
- `email`: EmailField: email address of the user booking
- `phone`: Charfield: phone number of the user booking
- `date`: DateField: date of booking
- `time`: TimeField: time of booking
- `end_time`: TimeField: end time of the time slot allocated
- `guests`: IntegerField: number of guests
- `created_on`: DateTimeField: timestamp of when the booking was created

I also have a save function that combines the `time` and `date` into a datetime field, then adds 2 hours, and saves it as the `end_time`. This is so that when bookings are assigned, they will be assigned a 2 hour slot.

#### Relationships:

In order to access and submit a booking form, you must be logged in. So the booking is assigned to the `user` logged in.

### Tables

This model represents all tables in the restaurant

#### Fields:

- `table_number`: IntegerField(unique): the table number in the restaurant
- `table_capacity`: IntegerField: the maximum amount of guests the table can hold

### Reservation

This model assigns the booking to a table.

#### Fields:

- `booking`: OneToOneField: grabs the data submitted in the booking form
- `table`: ForeignKey: grabs the table data
- `assigned_on`: DateTimeField: timestamps when the booking was assigned to the table

#### Relationships:

This model has a one to one relationship with the `booking form`, as one `booking form` is assigned to one `reservation`, and also has a foreign key referencing the `table`. This is not a one to one field in case multiple tables are needed for the booking.

## Future Updates

My future goals for this project is to be able to assign muliple tables to one booking.

## Technologies

### Python Modules

- asgiref==3.8.1
- crispy-bootstrap5==2024.2
- dj-database-url==0.5.0
- Django==4.2.14
- django-allauth==0.57.2
- django-crispy-forms==2.3
- django-phonenumber-field==8.0.0
- django-summernote==0.8.20.0
- gunicorn==20.1.0
- oauthlib==3.2.2
- phonenumbers==8.13.42
- psycopg2==2.9.9
- PyJWT==2.9.0
- python3-openid==3.2.0
- requests-oauthlib==2.0.0
- sqlparse==0.5.1
- whitenoise==6.5.0

### Django

- Django as my framework
- allauth for my authentication system
- Jinja templating for inserting data onto pages

### Deployment

- [PostgreSQL from Code Institute](https://dbs.ci-dbs.net/) for database hosting.
- [Heroku](https://dashboard.heroku.com/apps) to deploy my project

### Front End

- HTML
- Bootstrap and custom CSS

### Development

- [GitPod](https://codeinstitute-ide.net/workspaces)/VS Code for the IDE
- [GihHub](https://github.com/dashboard) for version conrol and repository hosting
- [Google Fonts](https://fonts.google.com/) for typography

### Other References

- Code Institute walkthrough project for help setting up django and allauth

## Manual Testing

### Contact Form

- Try to submit form without fields being filled in.
- Test each field against their specific field types
- Check relevent success message loads
- Check admin page to see if form has saved

### Booking Form

- Try to submit form without fields being filled in.
- Test each field against their specific field types
- Check relevent success message loads
- Check admin page to see if form has saved
- See if I can book a past date and/or time
- See if I can book less than 1 or more than 8 guests
- Try booking for a table or time that is unavailable

### View Bookings

### Edit/Cancel Booking

### Authentication