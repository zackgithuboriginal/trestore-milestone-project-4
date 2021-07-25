
DEPLOYMENT# Trestore - Milestone Project 4

![Image of responsive page mockups]()

## Website Description

Trestore is a website that serves two purposes, the first, to facilitate the sale of native trees and seeds to customers and the second, to offer sponsorship packages to customers so that they can support the replanting of native Irish trees. In order to  During the design of the website I wanted to use a colour scheme and design that emphasised the green and environmental nature of the purpose of the website. 

In order to make the user experience as seamless and easy as possible the website also emphasises intuitive page and website interaction. With simple and clear CTA buttons from the home page and the most important page interactions highlighted with buttons styled with the website's primary branding colour.

## User Experience / UX
### User Stories
### First time user
  1. **Example User Story.**


### Repeat user 
  1. **Example User Story.**


### Site administrators
  1. **Example User Story.**

### Design

#### Design Overview
There were two driving principles behind the design of this website and these were firstly to create an environment in which there is a clear hierarchy of importance with user’s content and posts being foremost and secondly to create an easily understandable and intuitive navigation and interaction interface.

#### Colour Scheme
![Image of responsive page mockups]()
#### Primary Colours
In the creation of the branding and design for the website I decided to draw on nature and the trees that the store would be selling for the colour scheme of the website. The primary brand colour for the website is #336857 a deep green colour reminiscent #F2F8F7 #1A342C 

#### Typography


#### Imagery

### Wireframes

The wireframes for the website were developed using [Figma](https://www.figma.com/) 

 -   Home Page - Desktop Wireframe - [View]()


### Database Design / Data Modelling

![Image of data schema diagram]()


#### Object model

![Image of post collection object]()

The posts collection is where all of the posts made by users are stored in the database. It uses MongoDB's ObjectId value as a unique key and stores all other details necessary to the display and tracking of the post in its data fields.

    example_attribute:             string




## Features

#### Home Page

![Image of responsive page mockups]()

The home page has two major roles. Firstly, its role is to introduce the user to the website and enable them to understand its purpose and functionality. Secondly, the home page is the primary means of exploring user’s posts and discovering new ideas and discussions.

To achieve the first goal I aimed to make the purpose of the home page as simple and clear as possible. Upon loading the page the user is presented with a column of posts down the centre of the page with a toolbar just above them with options to filter and sort. The user upon interacting with the scrollable list of posts will get an idea of the purpose of the site and will understand that this is an environment for creating and sharing posts.

The second goal of the home page to be the primary post navigation screen is achieved by utilising several smaller features to make the functionality of viewing and exploring posts as convenient and intuitive as possible.

#### Store Page

The store page is a simply designed page, prioritising above all a clean and clear user experience and access to information and products. The page has two sections, the first of these two sections is the product sort filtering and search section. This section provides users three options to customise the display of products in the store, offering the ability to filter by category, sort by either price ascending, price descending or by category and finally to filter results by search terms. By sumitting these parameters the products displayed on the page will change to suit the needs and intersests of the customer and create a positive user experience when browsing.

The second section is the product container wherein products are displayed on card elements in a responsive grid to provide a satisfying and easy browsing experience.
The product card contains a number of features including a product image, the product name, price and SKU value, a link to the product details page for that product and a quantity input field with a button to add the product to the basket.

#### Navbar

The navbar is fixed at the top of the base template so that it appears on all pages of the site. It comtains links to all of the primary pages as well as a dropdown list providing links related to profile actions and certain restricted actions such as adding products to the store.

The colour of the navbar is the primary branding colour of the website in order to create a cohesive environment across all of the pages and applications of the site.

#### Progress Blog

#### Add / Edit Post Page

#### Sponsorship Page

#### Profile Page

#### Basket Page

#### Checkout Page

#### Order Confirmation

#### Login Register

#### Product Details

#### Footer

#### Edit / Add Product Page

## Technologies Used


### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)


### Frameworks, Libraries & Programs Used

1. [Bootstrap 5.0:](https://getbootstrap.com/)
  - Bootstrap was used to create the initial base template of the design that was then built on top of and customised further using CSS.


### Testing

### Browser and Device Size Testing
The website was tested thoroughly across all major browsers and all screen and devices sizes down to 360px. 

- [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/)

- [Google Chrome](https://www.google.com/intl/en_ie/chrome/)

- [Microsoft Edge](https://www.microsoft.com/en-us/edge)

- [Opera](https://www.opera.com/)

- A full range of sizes and devices using Chrome DevTools, [Responsive Viewer](https://chrome.google.com/webstore/detail/responsive-viewer/inmopeiepgfljkpkidclfgbgbmfcennb?hl=en) and [Am I Responsive?](http://ami.responsivedesign.is/)

### Code Validation

At the end of the project, the code was put through CSS, HTML, JS and Pep8 Python validators to ensure there were no errors presented.

#### HTML validation [W3 Nu HTML validator](https://validator.w3.org/nu/)
<details>
  <summary>Expand Section</summary>
 
<h4>Home page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of home page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/home-html.png">
</details>

<h4>Store page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of store page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/store-html.png">
</details>

<h4>Sponsorship page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of sponsorship page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/sponsorship-html.png">
</details>

<h4>Product details page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of product details page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/product-details-html.png">
</details>

<h4>Add product page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of add product page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/add-product-html-alt.png">
</details>

<h4>Edit product page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of edit product page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/edit-product-html.png">
</details>

<h4>Progress blog page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of progress blog page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/progress-html-alt.png">
</details>

<h4>Add post page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of add post page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/add-post-html-alt.png">
</details>

<h4>Edit post page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of edit post page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/edit-post-html-alt.png">
</details>

<h4>Profile page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of profile page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/profile-html.png">
</details>

<h4>Sign in page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of sign in page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/login-html.png">
</details>

<h4>Register page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of registration page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/register-html.png">
</details>

<h4>Sign out page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of sign out page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/logout-html.png">
</details>

<h4>Basket page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of basket page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/basket-html.png">
</details>

<h4>Checkout page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of checkout page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/checkout-html.png">
</details>

<h4>Order details / Order confirmation page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of order details page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/order-details-html.png">
</details>

<h4>Email admin page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of email admin page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/email-admin-html.png">
</details>

<h4>Forgot password page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of forgot password page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/forgot-password-html.png">
</details>

<h4>Change Password page html validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of change password page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/change-password-html.png">
</details>
 
</details>

#### Python Validation [PEP8 online check](http://pep8online.com/)
<details>
  <summary>Expand Section</summary>
 
<h4>basket/contexts.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of basket/contexts.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/basket-contexts.png">
</details>

<h4>basket/views.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of basket/views.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/basket-views.png">
</details>

<h4>blog/admin.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of blog/admin.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/blog-admin.png">
</details>

<h4>blog/forms.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of blog/forms.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/blog-forms.png">
</details>

<h4>blog/models.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of blog/models.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/blog-models.png">
</details>

<h4>blog/views.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of blog/views.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/blog-views.png">
</details>

<h4>checkout/webhook_handler.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of checkout/webhook_handler.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/checkout-webhook_handler.png">
</details>

<h4>checkout/webhook.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of checkout/webhooks.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/checkout-webhook.png">
</details>

<h4>home/views.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of home/views.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/home-views.png">
</details>

<h4>ms4_trestore/settings.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of ms4_trestore/settings.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/ms4-settings.png">
</details>

<h4>products/admin.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of products/admin.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/products-admin.png">
</details>

<h4>products/forms.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of products/forms.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/products-forms.png">
</details>

<h4>products/models.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of products/models.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/products-models.png">
</details>

<h4>products/views.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of products/views.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/products-views.png">
</details>

<h4>products/widgets.py python validation</h4>     
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of products/widgets.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/products-widgets.png">
</details>

<h4>userprofile/forms.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of userprofiles/forms.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/userprofile-forms.png">
</details>

<h4>userprofile/models.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of userprofile/models.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/userprofile-models.png">
</details>

<h4>userprofile/views.py python validation</h4>             
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of userprofile/views.py results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/userprofile-views.png">
</details>
 
</details>

#### CSS Validation [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
<details>
  <summary>Expand Section</summary>
 
<h4>base.css css validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of base.css results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/ms4-css-alt.png">
</details>

<h4>checkout.css css validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of checkout.css results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/checkout-css.png">
</details>

<h4>userprofiles.css css validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of userprofiles.css results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/userprofiles-css.png">
</details>

</details>

#### Javascript Validation [JSHint](https://jshint.com/)
<details>
  <summary>Expand Section</summary>
  
<h4>base.js validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of change password page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/base-js.png">
</details>

<h4>basket.js validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of change password page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/basket-js.png">
</details>

<h4>blog.js validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of change password page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/blog-js.png">
</details>

<h4>products.js validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of change password page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/products-js.png">
</details>

<h4>stripe_elements.js validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of change password page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/stripe-js.png">
</details>

  <h4>userprofile.js validation</h4>
<details>
  <summary>Expand Screenshot</summary>
  <br>
 <img alt="Image of change password page results" src="https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/userprofile-js.png">
</details>
</details>

### Performance Testing

To ensure that the website performed well and loaded all pages quickly I tested each page using [Lighthouse](https://developers.google.com/web/tools/lighthouse) where all pages received positive results


#### Home Page 
![Image of Home Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/home-lighthouse.PNG)

#### Store Page 
![Image of Store Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/store-lighthouse.PNG)

#### Sponsorship Packages Page 
![Image of Sponsorship Packages Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/sponsorship-lighthouse.PNG)

#### Product Details Page 
![Image of Product Details Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/product-details-lighthouse.PNG)

#### Progress Blog Page 
![Image of Progress Blog Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/progress-lighthouse.PNG)

#### Add Post Page 
![Image of Add Post Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/add-post-lighthouse.PNG)

#### Edit Post Page 
![Image of Edit Post Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/edit-post-lighthouse.PNG)

#### Add Product Page 
![Image of Add Product Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/add-product-lighthouse.PNG)

#### Edit Product Page 
![Image of Edit Product Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/edit-product-lighthouse.PNG)

#### Basket Page 
![Image of Basket Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/basket-lighthouse.PNG)

#### Sign Out Page 
![Image of Sign Out Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/sign-out-lighthouse.PNG)

#### Sign In Page 
![Image of Sign In Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/sign-in-lighthouse.PNG)

#### Register Page 
![Image of Register Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/register-lighthouse.PNG)

#### Checkout Page 
![Image of Checkout Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/checkout-lighthouse.PNG)

#### Order Confirmation / Order Details Page 
![Image of Order Confirmation Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/order-confirmation-lighthouse.PNG)

#### Profile Page 
![Image of Profile Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/profile-lighthouse.PNG)

#### Email Admin Page 
![Image of Email Admin Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/email-admin-lighthouse.PNG)

#### Password Reset Page 
![Image of Password Reset Page Lighthouse Testing](https://github.com/zackgithuboriginal/trestore-milestone-project-4/blob/master/docs/password-reset-lighthouse.PNG)

### Testing User Stories from User Experience (UX) Section
#### First Time User Stories

#### 1.    Goal: EXAMPLE

**Expected:** EXAMPLE

**Result:** EXAMPLE

![Image of main post view]()



### Manual Functionality Testing

Page | Action | Expected Result | Result
-------- | ------------- | ------------- | ---------
EXAMPLE | EXAMPLE ACTION | EXAMPLE RESULT | Pass



### Bugs Discovered 



## Deployment

### To Publish to Heroku



### To Connect your Database to the Project



### To Clone the Repository and Run Locally

#### To Clone Using the Command Line


#### To Clone Using GitHub Desktop



#### To Run the Project Locally


## Credits

### Code



### Content



### Media



#### Original creators and links to images



### Acknowledgements
