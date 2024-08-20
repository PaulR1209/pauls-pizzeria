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