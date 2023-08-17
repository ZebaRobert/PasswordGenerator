
# PasswordGenerator

Welcome to the PasswordGenerator project! This is a command-line interface (CLI) based password generating application built in Python. It allows users to generate secure passwords based on their preferences and store them for later access.

**Contents:**
- [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [First Time Visitor Goals](#first-time-visitor-goals)
  - [Returning Visitor Goals](#returning-visitor-goals)
  - [Frequent Visitor Goals](#frequent-visitor-goals)
- [Design (Flow Chart)](#design-flow-chart)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Languages Used](#languages-used)
- [Deployment](#deployment)
- [Testing](#testing)
  - [Known Bugs](#known-bugs)
  - [Resolved Bugs](#resolved-bugs)
  - [Validation](#validation)
  - [Full Testing](#full-testing)
- [Credits](#credits)
  - [Content](#content)
  - [Acknowledgments](#Acknowledgments)

## User Experience

### User Stories

- **First Time Visitor:**
  - As a first-time visitor, I want to understand how the application works and how I can generate passwords for different platforms.
  - I want to be able to easily create a new account and securely store my generated passwords.

- **Returning Visitor:**
  - As a returning visitor, I want to quickly log in to my existing account and generate passwords with different strength levels and lengths.
  - I want to review and manage the passwords I've previously generated and see which platforms they are associated with.

- **Frequent Visitor:**
  - As a frequent visitor, I want to efficiently update and manage stored passwords, ensuring security and organization.
  - I want a streamlined and user-friendly password generation process each time I use the application.

### First Time Visitor Goals

- Understand the purpose and functionality of the application.
- Learn how to create an account and log in.
- Generate passwords for various platforms.

### Returning Visitor Goals

- Log in to the existing account.
- Generate new passwords with different strength levels and lengths.
- Review and manage previously generated passwords.

### Frequent Visitor Goals

- Efficiently update and manage stored passwords.
- Experience a streamlined password generation process.
- Maintain a secure and organized repository of passwords.

## Design (Flow Chart)

![Flow Chart](/docs/screenshots/flow-diagram.png)

## Features

- **Login System:** The application features a login system that uses the [`pickle`](https://docs.python.org/3/library/pickle.html) library to save and load instances of user classes as files. This allows users to store their generated passwords securely.

- **Password Generation:** Users can generate passwords with different levels of strength: weak, medium, and strong. They can also choose the length of the password, ranging from 0 to 30 characters.

- **Platform-specific Passwords:** Users can specify the platform for which they are generating the password. The platform and password are saved as key-value pairs in the user class instance.

- **Password Access:** Users can access all the passwords they have previously created, providing a convenient way to manage their generated passwords.

## Technologies Used

- Python
- [`pickle`](https://docs.python.org/3/library/pickle.html) library
- [`os`](https://docs.python.org/3/library/os.html) library
- [`string`](https://docs.python.org/3/library/string.html) module
- [`random`](https://docs.python.org/3/library/random.html) module

## Languages Used

- Python

## Deployment

The PasswordGenerator application is deployed using both Heroku and GitHub.

## Testing

The PasswordGenerator application has undergone testing to ensure its functionality and reliability. The following issues were identified and resolved:

- **Known Bugs:** None

- **Resolved Bugs:**
  1. Passwords weren't stored with the class instance when the program was closed.
     - Bug Details: The `generated_passwords` dictionary was initially defined outside the class constructor. Moving it inside the constructor resolved the issue.
  2. Class instance files remained open after user logout.
     - Bug Details: A code error causing the `main()` function to be called multiple times resulted in unclosed files. Restructuring the code resolved this issue.
  3. Users could access functions not currently available.
     - Bug Details: The `handle_input` function allowed users to use certain keywords that weren't offered at the time. Restructuring the function to allow only appropriate keywords resolved this issue.

### Validation

The Python code for this project has been validated using the [PEP8](https://pep8ci.herokuapp.com/) validator provided by Code Institute.

![Python Validation](/docs/screenshots/python-validator.png)

## Full Testing

| Feature                                      | Expected Outcome | Testing Performed | Result | Pass/Fail |
|----------------------------------------------|------------------|-------------------|--------|-----------|
| User Creation                               | User can create an account | Created multiple accounts | No problems | Pass |
| Restrictions for Creating New User           | Cannot create an account with the same username as someone else | Tried creating multiple accounts with the same username | Was unable to create multiple accounts | Pass |
| Logging in with Previously Created Account  | Can log in with previously created account | Tried logging in with previously created account | Successfully logged in with previous account | Pass |
| Deleting Accounts                           | Can delete account if username known | Deleted multiple accounts | Successfully deleted every one | Pass |
| Displaying Previously Stored Passwords       | Can display previously created password | Requested previous password | Successfully displayed on the screen | Pass |
| Generating New Passwords                    | Can generate new password | Provided information and prompted for password | Successfully generated password | Pass |
| Storing Passwords with the Class Instance   | Can store password/platform combination for later use | Stored passwords in dictionary of the User   | Passwords safely stored | Pass |
| Stop & Exit                                  | Can navigate back or exit the app | Typed "stop" and/or "exit" when appropriate | Commands executed properly | Pass |

## Credits
### Content
 - Content for this project was written by Robert Zeba
### Acknowledgments
I would like to acknowledge the following people who helped me along the way in completing this project:
- My family & friends for their feedback and support during the development of the project.
- My Code Institute Mentor Graeme Taylor
---

