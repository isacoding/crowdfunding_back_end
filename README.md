# MentHub: Tech Mentor Matching Platform for Women in STEM

## Project Overview

MentHub is a platform designed to connect women in STEM fields with experienced mentors to foster career growth, knowledge sharing, and professional development. The platform allows mentees to create mentorship projects, which mentors can support by pledging hours based on their expertise.

## Key Features

1. **User Profiles**
   - **Mentors** can create profiles outlining their areas of expertise and availability for mentorship.
   - **Mentees** can create profiles to showcase their career goals and the skills they wish to develop.
2. **Mentorship Projects**

   - **Mentees** can create mentorship projects specifying their career goals, skills to develop, and target mentorship hours.
   - **Mentors** can view these projects and pledge hours to help mentees meet their objectives.

3. **Pledge System**

   - Mentors pledge hours to support a mentee’s project. A progress tracker shows how many hours have been pledged versus the total target hours for the project.

4. **Basic Search/Filter**

   - Users can search for mentors or projects by expertise or area of interest.

5. **Authentication**
   - Basic sign-up and login functionality for mentors and mentees.

---

## Target Audience/User Stories

1. **Women in STEM**

   - Seeking mentorship and guidance to advance their careers.
   - Looking for project-based support to develop specific skills.

2. **Women Transitioning into STEM**

   - Needing mentorship and advice on how to transition from other fields into STEM.

3. **Mentors**
   - Experienced professionals eager to share their knowledge and mentor others.
   - Willing to pledge hours to support specific mentorship projects.

---

## Front-End Pages/Functionality

1. **Homepage:**

   - Sign-up/Login options.
   - Display mentorship projects with search and filter options based on expertise or project title.

2. **Mentorship Project Details Page:**

   - Shows project description, target hours, and progress.
   - Mentors can pledge hours to a project.

3. **Profile Page:**

   - **Mentor Profiles:** List expertise and availability.
   - **Mentee Profiles:** Share career goals and skills to develop.
   - Users can edit their personal information and manage their mentorship projects or pledges.

4. **Error Handling Page:**
   - **Failed Login Attempts:** Displays a message for invalid email or password ("Invalid email or password. Please try again.") and provides an option to reset the password.
   - **Unauthorised Access:** Shows a message ("You do not have permission to access this page.") if a user tries to access restricted areas.
   - **Invalid Input:** Provides error messages when required fields are missing or incorrectly formatted ("Please fill out all required fields correctly.").

---

## API Specification

| **URL**        | **HTTP Method** | **Purpose**                              | **Request Body** | **Success Response Code** | **Authentication/Authorisation**  |
| -------------- | --------------- | ---------------------------------------- | ---------------- | ------------------------- | --------------------------------- |
| `/mentors/`    | GET             | Returns all mentors                      | N/A              | 200                       | N/A                               |
| `/mentors/`    | POST            | Create a mentor profile                  | Mentor object    | 201                       | Login required                    |
| `/mentees/`    | GET             | Returns all mentees                      | N/A              | 200                       | N/A                               |
| `/mentees/`    | POST            | Create a mentee profile                  | Mentee object    | 201                       | Login required                    |
| `/projects/`   | GET             | Returns all mentorship projects          | N/A              | 200                       | N/A                               |
| `/projects/`   | POST            | Create a new mentorship project          | Project object   | 201                       | Login required / Must be a mentee |
| `/pledges/`    | POST            | Create a new pledge for mentorship hours | Pledge object    | 201                       | Login required / Must be a mentor |
| `/users/login` | POST            | Log in an existing user                  | User object      | 200                       | N/A                               |
| `/users/`      | POST            | Sign up a new user (mentor or mentee)    | User object      | 201                       | N/A                               |

---

## Database Schema

<img src="crowdfunding/images/menthub_database_schema_v2.jpg" alt="MentHub Database Schema" width="400"/>

# Project Requirements

Your crowdfunding project must:

[] Be separated into two distinct projects: an API built using the Django Rest Framework and a website built using React.
[x] Have a clear target audience.
[x] Have user accounts. A user should have at least the following attributes:
[x] Username
[x] Email address
[x] Password
[x] Ability to create a “project” to be crowdfunded which will include at least the following attributes:
[x] Title
[x] Owner (a user)
[x] Description
[x] Image
[x] Target amount to fundraise
[x] Whether it is currently open to accepting new supporters or not
[x] When the project was created
[x] Ability to “pledge” to a project. A pledge should include at least the following attributes:
[x] An amount
[x] The project the pledge is for
[x] The supporter/user (i.e. who created the pledge)
[x] Whether the pledge is anonymous or not
[x] A comment to go along with the pledge
[x] Implement suitable update/delete functionality, e.g. should a project owner be allowed to update a project description?
[x] Implement suitable permissions, e.g. who is allowed to delete a pledge?
[x] Return the relevant status codes for both successful and unsuccessful requests to the API.
[x] Handle failed requests gracefully (e.g. you should have a custom 404 page rather than the default error page).
[x] Use Token Authentication, including an endpoint to obtain a token along with the current user's details.
[] Implement responsive design.

## Submission

Please include the following in your readme doc:

[] A link to the deployed project.
[] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
[] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
[] A screenshot of Insomnia, demonstrating a token being returned.
[] Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).
[] Your refined API specification and Database Schema.
