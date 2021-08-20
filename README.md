<h1 align="center">Django API Views (Custom + REST)</h1>

<p align="center">
  <img src="img/home.png" alt="Home Page" width="800">
</p>


**Main Task:** create a django application, with an endpoint (view) that accepts input parameters, validates them and returns the correct response.

<h5 align="center">Input parameters</h5>

**`email`** parameter must be a valid email, length no more than 100 characters. It should be checked for all forbidden characters, combinations of characters, etc. Mail in the `gmail.com` and `icloud.com` domains should not be accepted.

**`password`** parameter - the password must consist of alphanumeric characters, underscore, starts with an capital letter. Length from 7 to 16 characters.

**`first_name`** - only letters and dashes.

**`last_name`** - only letters, dash and space.


### 📝 &nbsp;Requirements

- **Django** == `3.2.6`
- **Python** == `3.8.6`
- **django-crispy-forms** == `1.12.0`
- **django-extensions** == `3.1.3`
- **djangorestframework** == `3.12.4`
- **dnspython** == `2.1.0`
- **PyJWT** == `1.7.1`
- **python-decouple** == `3.4`


### 📷 Part 1 (with screenshots)

This part includes the implementation of the main task and a separate endpoint that will display request records filtered by the current IP address (where the request came from).

The implementation of this part is in folder `api/` and accordingly on url `../api/v1/get/` and `../api/v1/post/`.

`../api/v1/post/` - contains the implementation of the main task.

`../api/v1/get/`-  display request records filtered by the current IP address.


Parameters Validation        |  Valid Parameters | Email must be Unique
:-------------------------:|:-------------------------:|:-------------------------:
<img src="img/custom_validation.png" title="Parameters Validation" width="100%"> |<img src="img/custom_valid_request.png" title="Valid Parameters" width="100%">|<img src="img/custom_email_unique.png" title="Unique Email" width="100%">


Request Records         |  Parameters Validation (Postman) | Request Records (Postman)
:-------------------------:|:-------------------------:|:-------------------------:
<img src="img/custom_requests_list.png" title="Request Records" width="100%"> |<img src="img/postman_custom_validation.png" title="Parameters Validation (Postman)" width="100%">|<img src="img/postman_custom_requests_list.png" title="Request Records (Postman)" width="100%">


### 📷 Part 2 (with screenshots)

This part expands our task by including what was covered in the previous paragraph via RESTful implementation.

The implementation of this part is in folder `rest/`.

`POST` request -  implementation of the main task.

`GET` request - display request records filtered by the current IP address.


Parameters Validation        |  Valid Parameters | Email must be Unique
:-------------------------:|:-------------------------:|:-------------------------:
<img src="img/rest_validation.png" title="Parameters Validation" width="100%"> |<img src="img/rest_valid_request.png" title="Valid Parameters" width="100%">|<img src="img/rest_email_unique.png" title="Unique Email" width="100%">


Request Records         |  Valid Parameters (Postman) | Request Records (Postman)
:-------------------------:|:-------------------------:|:-------------------------:
<img src="img/rest_requests_list.png" title="Request Records" width="100%"> |<img src="img/postman_rest_validation.png" title="Valid Parameters (Postman)" width="100%">|<img src="img/postman_rest_requests_list.png" title="Request Records (Postman)" width="100%">


### 📷 Part 3 (with screenshots)

The hardest part. Users appear in the application at the system level. Now, instead of requests, we will store users. The user himself must register through a separate endpoint (`/register/`), where the sent parameters will be checked. After registration, the user goes to the authorization endpoint (`/login/`) and a token is returned to him (`JWT`). Further, all requests are authorized through the user's token.

The implementation of this part is in folder `authentication/`.

- `authentication/register/` - allows you to register.

- `authentication/login/` - allows you to log in.

- `authentication/user-info/` - contains information about the logged in user.


**Registration of New Users** - the main logic is implemented in the `RegistrationSerializer` class and in `RegistrationAPIView`.

**User Login** - `LoginSerializer` class and `LoginAPIView`.

**Retrieving and Updating User Data** - `UserSerializer` and `UserRetrieveUpdateAPIView`.


`authentication/backends.py` - custom backend to support JWT .

Registration (Validation)        |  Successful Registration | Login (Validation)     |  Login (Wrong Password)
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
<img src="img/auth_register_validation.png" title="Registration (Validation)" width="100%"> |<img src="img/auth_register_success.png" title="Successful Registration" width="100%">|<img src="img/auth_login_validation.png" title="Login (Validation)" width="100%"> |<img src="img/auth_login_wrong_password.png" title="Login (Wrong Password)" width="100%">

Successful Login        |  GET User Info (without token) | GET User Info (Success)     |  Change User Email
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
<img src="img/auth_login_success.png" title="Successful Login " width="100%"> |<img src="img/auth_user_info_403.png" title="GET User Info (without token)" width="100%">|<img src="img/auth_user_info_success.png" title="GET User Info (Success)" width="100%"> |<img src="img/auth_user_info_patch.png" title="Change User Email" width="100%">



<h5 align="center">Main Logic</h5>

The key idea is to create our own User model instead of the Django model and write our own views to support returning JSON instead of HTML.

With token-based authentication, the server provides the client with a token after a successful login/register request.

This token is unique to the user who is logged in and is stored in the database along with the user ID. The client is expected to send a token with future requests so that the server can identify the user.
The server does this by searching the database table that contains all the created tokens.

If a matching token is found, the server continues to verify that the token is still valid. If the corresponding token is not found, we say that the user is not authenticated.

### 💡 &nbsp;Additional Info

**JSON Web Token** (`JWT`) is an open standard that defines a compact and self-contained way for securely transmitting information between two parties.

Using `JWT` is a good option because it is an open standard. This means that all `JWT` implementations should be fairly similar, which is an advantage when working with different languages and technologies. `JWTs` also contain information about the user, which is convenient for the client side.


## 📫 &nbsp;Get in touch

<p align="center">
<a href="https://www.linkedin.com/in/yevhenii-shendrikov-6795291b8/"><img src="https://img.shields.io/badge/-Jack%20Shendrikov-0077B5?style=flat&logo=Linkedin&logoColor=white"/></a>
<a href="mailto:jackshendrikov@gmail.com"><img src="https://img.shields.io/badge/-Jack%20Shendrikov-D14836?style=flat&logo=Gmail&logoColor=white"/></a>
<a href="https://www.facebook.com/jack.shendrikov"><img src="https://img.shields.io/badge/-Jack%20Shendrikov-1877F2?style=flat&logo=Facebook&logoColor=white"/></a>
<a href="https://t.me/jackshen"><img src="https://img.shields.io/badge/-@jackshen-0088cc?style=flat&logo=Telegram&logoColor=white"/></a>
</p>