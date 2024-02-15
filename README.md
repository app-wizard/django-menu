# Lotus Pavilion - Asian Cuisine Web Menu

Welcome to the Lotus Pavilion, an Asian cuisine restaurant that brings the convenience of exploring our diverse menu right to your fingertips. My project, hosted at [herokuapp.com](https://django-menu-87d486944791.herokuapp.com/), offers a web version of our restaurant's menu, designed to enhance the dining experience of our guests even before an attendant presents them with a physical menu. By simply scanning a QR code found on promotional materials within the establishment, visitors can delve into our offerings, enjoying an intuitive navigation system for searching and sorting dishes. Additionally, our web menu features a review functionality for dishes, aiding in decision-making and distinguishing our service in a competitive market.

## Project Goal

The objective of this project, as assigned by [Code Institute](https://codeinstitute.net/ie/), is to construct a website facilitating multiple users to interact with a shared database, exemplified by capabilities such as performing CRUD (Create, Read, Update, Delete) operations. This endeavor aims to showcase the practical application of Django models, a login system, user access separation (e.g., admins vs. non-admins, object owners vs. non-owners), and agile project management, culminating in a comprehensive digital solution that serves both the restaurant and its patrons.

## Strategy

During the development of the Lotus Pavilion web menu, we adopted an Agile methodology, leveraging a Kanban board via GitHub Projects for task management and workflow optimization. User stories were prioritized using the MoSCoW method, guiding our development focus towards delivering the highest value features. The project was deployed on Heroku with PostgreSQL as the database solution and Cloudinary for media storage, ensuring a seamless and efficient backend and media management. The frontend utilized a Bootstrap template, significantly reducing development time. Our choice of Django for the backend accelerated the development process further, thanks to its comprehensive suite of out-of-the-box functionalities, including a fully-featured admin panel. This strategic combination of technologies and methodologies enabled us to create an intuitive, efficient web menu system for the Lotus Pavilion, enhancing the dining experience for our guests.

### User Stories

#### Planned for Future Implementation
- **Dish Availability Display**: To show if a dish is currently available or not.
- **Newsletter Subscription**: To allow users to subscribe to updates and news.
- **Collect Feedback**: To enable users to provide feedback on dishes.

#### Epic 1: User Account Management
- **Create an Account**: "As a user, I want to create an account so that I can have a personalized experience."
- **Log In**: "As a user, I want to log in to my account so that I can access my personal settings."
- **Log Out**: "As a user, I want to log out of my account so that my account is secure when not in use."
- **Update Profile**: "As a user, I can update my profile information so that my personal information is up to date."

#### Epic 2: Site Stability and Performance
- **Testing**: "As a restaurant owner, I want my site to operate stably so that the user experience is improved."

#### Epic 3: Menu Interaction
- **Electronic Menu**: "As a restaurant visitor, I can open the website to view the electronic menu so that I can choose a dish conveniently."
- **Search the Menu**: "As a restaurant visitor, I want to have the ability to search the menu so that I can find dishes quickly."
- **Filter Option**: "As a client, I want to filter dishes so that I can browse promotional items easily."

#### Epic 4: Reviews Management
- **Leave Reviews**: "As a user, I want to leave reviews about dishes so that I can help others make an informed choice."
- **Display Reviews**: "As a user, I want to read reviews about dishes so that I can make a more informed decision."

#### Epic 5: Menu Administration
- **Setup Menu from Admin Panel**: "As a restaurant owner, I want to add and remove dishes from the menu so that I can keep the menu up-to-date."

#### Epic 6: Website Setup and Deployment
- **Setup and Deploy**: "As a restaurant owner, I want to create a website with an electronic version of the menu to enhance convenience for users."

#### Epic 7: Customer Engagement and Feedback
- **Newsletter Subscription**: "As a user, I can subscribe to a newsletter so that I can stay informed about the latest news and offers."
- **Collect Feedback**: "As the website owner, I can collect feedback directly from users to understand their needs and improve the website."

For detailed descriptions and acceptance criteria of each user story, please visit the [User Stories section on GitHub](https://github.com/app-wizard/django-menu/issues).

## Features

### Existing Features

- **Homepage**
  - The homepage greets visitors with a captivating slogan and a photograph of the restaurant's interior, immersing them in the ambiance of Asian cuisine.
  - ![Homepage](media\scrhome.jpg)

- **Menu Navigation Button**
  - This functional button enables visitors to view all dishes or navigate to specific categories within the menu.
  - ![Menu Navigation](media\scrnav.jpg)

- **Information Section**
  - Offers detailed information about the restaurant, allowing visitors to learn more about what makes it special.
  - ![Information Section](media\scrinfo.jpg)

- **Delivery Information Section**
  - Provides essential details regarding delivery services.
  - ![Delivery Information](media\scrdelivery.jpg)

- **About Us Information Section**
  - Provides essential details regarding company.
  - ![About Us Information](media\scraboutus.jpg)

- **Sign In Section**
  - Directs users to a login page, where they can either sign in or proceed to register a new account.
  - ![Sign In Section](media\scrsignin.jpg)
  - ![Registration](media\scrreg.jpg)
  

- **Administrator Access**
  - Admin users are provided with a dedicated admin panel for comprehensive site management.
  - ![Administrator Access ](media\scradminmenu.jpg)

- **User Profile Page**
  - A page that allows all users to update their personal information and customize their profile photo.
  - ![User Profile Page ](media\scrprofile.jpg)

- **Full-text Search**
  - Embedded in the site's header, this feature supports efficient searches across the menu, with additional methods to prevent empty query searches.
  - ![Full-text Search ](media\scrsearch.jpg)
  - ![Full-text Search Empty ](media\scrsearch2.jpg)

- **Search Results Page**
  - Displays either a "no results found" message for unsuccessful searches or a catalog page with items for successful searches.
  - ![Search Results Page](media\scrsearchres1.jpg)
  - ![Search Results Page](media\serachres2.jpg)

- **Catalog Page**
  - Showcases dishes from the menu with pricing and brief descriptions, complemented by pagination for easier navigation.
  - ![Menu Page](media\scrmenu.jpg)

- **Filtering Functionality**
  - Allows users to filter dishes by discounts and sort them by ascending or descending prices.
  - ![Filtering Functionality Screenshot Placeholder](media\scrfilter.jpg)

- **Product Page**
  - By clicking on a dish card, users are taken to a detailed page where they can view an enlarged photo, and read or leave comments.
  - ![Product Page](media\scrcard.jpg)

- **Comment Functionality**
  - Restricted to registered users for posting, with the ability to edit or delete their comments. Unconfirmed comments are only visible to their authors.
  - ![Comment Functionality](media\scrcomment2.jpg)

- **Pop-up Messages**
  - Utilizes convenient pop-up messages to notify users about various actions.
  - ![Pop-up Messages](media\scrmssg.jpg)

- **Admin Panel Customization**
  - For administrators, the admin panel has been customized for ease of use, including features for confirming comments and adjusting menu items and prices.
  - ![Admin Panel 1](media\sxradmin1.jpg)
  - ![Admin Panel 2](media\sxradmin2.jpg)

### Features to Implement in the Future

In addition to addressing the currently unimplemented user stories, future enhancements of the Lotus Pavilion web menu are planned to significantly improve user engagement and compliance with legal standards:

- **Dish Availability Display**: Introducing real-time status updates on dish availability to help customers make informed choices.
- **Newsletter Subscription**: Implementing a subscription feature for customers to stay updated with the latest news and offers.
- **Collect Feedback**: Creating a platform for customers to provide feedback on dishes and services, fostering a community and improving customer satisfaction.

Further improvements are aimed at enhancing the user registration process by:
- Enabling login through Google and social media platforms for a more streamlined and convenient user experience.
- Providing users with the ability to delete their accounts, ensuring a transparent and trustful interaction with the service.

Additionally, the privacy policy section will be expanded to fully comply with current legislation, ensuring that the Lotus Pavilion's web menu not only meets but exceeds legal requirements for privacy and data protection.

## Design

The design of the Lotus Pavilion web menu is a testament to the fusion of tradition and modernity, encapsulating the essence of Asian culinary excellence. The website's visual narrative is crafted with an exquisite blend of rich wooden textures and a warm, inviting color palette, featuring deep browns and muted golds that echo the elegance of the restaurant's physical space.

### Color Scheme and Typography
The color scheme is a thoughtful selection of earthy tones, accented with the vibrant hues of Asian spices and the serene ambiance of a traditional lotus pond at dusk. This palette is harmoniously paired with a clean and contemporary typography that balances the visual warmth with crisp readability.

### Responsiveness and Interactivity
Attention to responsive design ensures that the site's allure is preserved across all devices, offering an inviting and seamless experience whether on desktop or mobile. Interactive elements, such as the filter dropdown and search functionality, are designed for intuitive engagement, inviting users to explore the menu with ease.

### Imagery and Aesthetics
High-resolution images showcase the menu offerings, with each dish presented as a work of art, highlighting the fresh ingredients and meticulous presentation. The homepage sets the stage with a narrative, "Step into a world where every bite tells a story of centuries-old traditions," inviting visitors on a culinary journey.

### Custom Styling and Bootstrap Framework
The foundation of the design is built on a Bootstrap template, which accelerates development and ensures a high level of polish with its pre-designed components. Custom styles are layered to enhance unique features, adding character and personality to the site. This combination guarantees both efficiency in development and a bespoke user interface.

### Data Model

The Lotus Pavilion web menu leverages a robust data model hosted on Heroku with PostgreSQL (https://www.elephantsql.com/) for database services. For media storage, Cloudinary is employed, effectively managing the images associated with the menu items.

The data model is structured around several core Django models:

- `User`: Built on Django's default user model, extended with an image field via Cloudinary for user profile pictures.
- `Category`: Represents different categories under which menu items are organized, with fields for name and slug.
- `Product`: The central entity representing individual menu items, linked to `Category` with fields for name, description, image, price, discount, and quantity.
- `Comment`: Allows for user interaction with the menu items, containing fields for the comment body, approval status, creation timestamp, and foreign keys linking to `User` and `Product`.

The ERD encapsulates the relationships between these models, with `Product` being associated with `Category` and `Comment` being related to both `Product` and `User`. The diagram highlights the one-to-many relationships, where a single category can encompass multiple products, and a product can have numerous comments from different users.

Entity Relationship Diagram:

![ERD](media\edr.png)

### Imagery

The Lotus Pavilion's digital menu is a visual feast, showcasing a selection of images that capture the essence and allure of Asian cuisine. 

#### Unique Menu Item Visuals
The menu's imagery is not static; each dish is vividly brought to life with unique visuals generated by [Craiyon](https://www.craiyon.com/), an AI-powered service that pushes the boundaries of graphic generation. Complementing these are resources from [Freepik](https://www.freepik.com/), which provide a rich library of graphical elements that enhance the storytelling of our culinary offerings.

#### Cloudinary for Media Management
For managing these images, [Cloudinary](https://cloudinary.com/)'s cloud-based platform is utilized, ensuring that the visual assets are optimized for performance across all devices and user scenarios. Cloudinary's service enables dynamic manipulation of images, which is essential for maintaining responsiveness and visual impact in a diverse digital landscape.

### Languages Used:

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks, Libraries, and Packages Used:

- [Bootstrap:](https://getbootstrap.com/) The Bootstrap framework facilitated the creation of a responsive and visually appealing web interface.
- [Cloudinary:](https://cloudinary.com/) Cloudinary was utilized for robust image management and storage solutions.
- [Django:](https://www.djangoproject.com/) Django served as the backbone web framework due to its versatility and security features.
- [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) This extension was employed to render elegant Django forms quickly.
- [Gunicorn:](https://gunicorn.org/) Gunicorn acted as the HTTP server, interfacing with Django to serve web pages on Heroku.
- [Django Crispy Bootstrap 5:](https://django-crispy-forms.readthedocs.io/en/latest/) Enhanced form rendering using Bootstrap 5 style.
- [DJ-Database-URL:](https://pypi.org/project/dj-database-url/) This utility allows for database configurations to be defined by a URL.
- [DJ3-Cloudinary-Storage:](https://pypi.org/project/dj3-cloudinary-storage/) An integration layer for storing media files with Cloudinary in Django 3+.
- [Psycopg2:](https://pypi.org/project/psycopg2/) The PostgreSQL adapter for Python, facilitating database connections and operations.
- [Whitenoise:](http://whitenoise.evans.io/en/stable/) Allows the app to serve its own static files, making it self-contained and reducing the dependency on external services.

#### Visual Studio Code Extensions:
- Live Server: For real-time local development.
- Pylance: Python language support with type checking and auto-completion.
- ESLint: JavaScript linting.
- Django: Syntax support for Django templates.

#### Command Line Tools:
- [Git](https://git-scm.com/): Version control.
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli): Deploying and managing the Heroku app.
- Black: Code formatting.
- flake8: Code quality checking.

These tools and extensions have been instrumental in building a robust and user-friendly web application, ensuring a streamlined workflow and high-quality code.

#### Web Applications Used for Development and Testing:
- [Am I Responsive](http://ami.responsivedesign.is): To check the responsiveness of the application.
- [Chrome DevTools](https://developer.chrome.com/docs/devtools/): For testing, debugging, and performance analysis.
- [HTML Validator](https://validator.w3.org/) and [W3 CSS Validator](https://jigsaw.w3.org/css-validator/): To validate HTML and CSS files.
- [JSHint](https://jshint.com/): To check JavaScript code quality.
- [Photoshop](https://www.adobe.com/products/photoshop.html): Image editing and customization.
- [Unsplash](https://unsplash.com/): High-quality stock photography.

## Testing

### Browser Compatibility

The application underwent comprehensive testing on a MacBook Air (Retina, 13-inch, 2018) running macOS Monterey 12.5, utilizing the following browsers to ensure optimal performance and compatibility:

- Safari 14
- Google Chrome Version 121.0.6167.160
- Firefox Browser Version 122.0.1

Additionally, mobile testing was conducted on iOS devices with Safari Version 15.6:

- iPhone 12 Pro Max running iOS 17.3

### Responsiveness

Responsiveness was meticulously tested across various devices, from the compact iPhone 5 screen (320px wide) to expansive displays such as the 5K iMac Pro (5120 x 2880 px), ensuring a seamless user experience across a broad spectrum of screen sizes.

#### W3C Markup Validator:

The W3C Markup Validator were used to validate the HTML on all pages of the project to ensure there were no syntax errors in there. To validate the HTML files all Django template tags were manually removed with the HTML code copied and inserted to the base template.
