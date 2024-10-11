# MentHub: Tech Mentor Matching Platform for Women in STEM

## Project Description

MentHub is a mentorship platform aimed at empowering women in STEM by providing a space for mentors and mentees to connect, share experiences, and foster professional growth. Through structured mentorship opportunities, MentHub facilitates career development and knowledge exchange, bridging the gap between experienced professionals and aspiring women in the STEM community.

## Concept and Name

MentHub was chosen as the name for the platform because it conveys the core idea of mentorship and community in a sleek way. The goal is to establish a hub for collaboration and growth for women navigating their careers in STEM fields.

## Target Audience/User Stories

### Women in STEM:

- Looking for guidance, mentorship, or professional advice to advance their careers.
- Seeking project-based mentorship to support specific learning objectives or professional growth.

### Women Transitioning into STEM:

- Wanting guidance on how to transition into tech or a STEM career from another field.

### Mentors:

- Experienced professionals eager to share their expertise and give back to the community by mentoring others.

## Key Features

### Mentor and Mentee Profiles:

- **Mentors** can create profiles detailing their areas of expertise, availability, and mentoring preferences (e.g., one-time catch-ups, three-month projects, or long-term mentorship).
- **Mentees** can build profiles showcasing their career aspirations, skills they want to develop, and professional background. Additionally, mentees can showcase specific projects they are working on and seek guidance or mentorship for these projects. This allows mentors to see not only the mentee’s personal journey but also the tangible work they are currently focused on and need help with.

### Project-Based Mentorship:

- Mentees can create projects that outline the skills they wish to learn or develop, their career goals, and the mentorship hours needed to achieve these objectives.
- Mentors can view these projects and pledge a set number of hours to support them. A project can receive pledges from multiple mentors, making it a collaborative learning experience.

### Flexible Matching and Communication:

- Mentors and mentees can connect regardless of geographical location through the platform, enabling virtual mentorship.
- Users can filter profiles and projects based on:
  - **Location**
  - **Expertise**
  - **Area of Interest**
  - **Availability** (e.g., short-term, long-term, or one-time)
  - **Industry Focus** (e.g., software development, data science, engineering, etc.)
  - **Skills Offered** (for mentors) or **Skills Needed** (for mentees)
- These filters ensure users find the right match that aligns with their mentorship preferences and career aspirations.

### Mentorship Pledges:

- Mentors can pledge hours to projects that align with their expertise and availability.
- A pledge includes the number of hours offered and is linked to a specific mentorship project.

### Real-Time Notifications:

- Notifications for new mentorship requests, updates on pledged projects, and important platform announcements to keep users informed.

## Front-End Pages/Functionality

### Homepage:

- **Navigation bar**: Sign up/Login buttons, Create Mentorship Projects button.
- **Display all mentorship projects**: Allows users to explore all available projects and mentorship opportunities.
- **Search and filter options**: Users can search by category, skillset, or project title.
- **Project details button**: Redirects to the mentorship project details page.
- **Footer**: Social media links, contact information, and other platform resources.

### Mentorship Project Details Page:

- Shows the project owner (mentee) and mentors who have pledged to support the project.
- Displays project description, required skills, and target mentorship hours.
- Progress bar showing the number of hours pledged versus the target hours.
- Button for mentors to pledge hours.

### Profile Page:

- **Mentor Profile View**:
  - List expertise, availability, contact preferences, and mentorship options.
- **Mentee Profile View**:
  - Share career goals, skills to develop, and mentorship needs.
  - Display all active and completed projects, with the option to highlight projects that need mentorship or guidance.
- Users can edit personal details, update project information, and manage mentorship requests.
- Mentees can also view other mentee profiles, connect with them, and collaborate on shared projects.

### Error Handling Page:

- Displays appropriate messages for failed logins, unauthorised access, or invalid inputs.
- Shows error messages when required fields are missing or incorrectly formatted.

## API Specification

| URL                    | HTTP Method | Purpose                                              | Request Body   | Success Response Code | Authentication/Authorisation              |
| ---------------------- | ----------- | ---------------------------------------------------- | -------------- | --------------------- | ----------------------------------------- |
| /mentors/              | GET         | Returns a list of all mentors                        | N/A            | 200                   | N/A                                       |
| /mentors/:id           | GET         | Returns a mentor by ID                               | N/A            | 200                   | N/A                                       |
| /mentors/              | POST        | Create a new mentor profile                          | Mentor object  | 201                   | Login required                            |
| /mentors/:id           | PUT         | Update a mentor profile                              | Mentor object  | 200                   | Login required / Must be the mentor       |
| /mentors/:id           | DELETE      | Delete a mentor profile                              | N/A            | 200                   | Login required / Must be the mentor       |
| /mentees/              | GET         | Returns a list of all mentees                        | N/A            | 200                   | N/A                                       |
| /mentees/:id           | GET         | Returns a mentee by ID                               | N/A            | 200                   | N/A                                       |
| /mentees/              | POST        | Create a new mentee profile                          | Mentee object  | 201                   | Login required                            |
| /mentees/:id           | PUT         | Update a mentee profile                              | Mentee object  | 200                   | Login required / Must be the mentee       |
| /mentees/:id           | DELETE      | Delete a mentee profile                              | N/A            | 200                   | Login required / Must be the mentee       |
| /projects/             | GET         | Returns a list of all mentorship projects            | N/A            | 200                   | N/A                                       |
| /projects/:id          | GET         | Returns a mentorship project by ID                   | N/A            | 200                   | N/A                                       |
| /projects?is_open=True | GET         | Returns all open mentorship projects                 | N/A            | 200                   | N/A                                       |
| /projects/             | POST        | Create a new mentorship project                      | Project object | 201                   | Login required / Must be a mentee         |
| /projects/:id          | PUT         | Update a mentorship project                          | Project object | 200                   | Login required / Must be project owner    |
| /projects/:id          | DELETE      | Delete a mentorship project                          | N/A            | 200                   | Login required / Must be project owner    |
| /projects/:id/pledges/ | GET         | Returns a list of all pledges for a specific project | N/A            | 200                   | N/A                                       |
| /pledges/              | GET         | Returns a list of all pledges made by mentors        | N/A            | 200                   | N/A                                       |
| /pledges/:id           | GET         | Returns a pledge by ID                               | N/A            | 200                   | N/A                                       |
| /pledges/              | POST        | Create a new pledge for mentorship hours             | Pledge object  | 201                   | Login required / Must be a mentor         |
| /pledges/:id           | PUT         | Update a pledge                                      | Pledge object  | 200                   | Login required / Must be the pledge owner |
| /pledges/:id           | DELETE      | Delete a pledge                                      | N/A            | 200                   | Login required / Must be the pledge owner |
| /users/                | GET         | Returns a list of all users (mentors and mentees)    | N/A            | 200                   | Login required / Must be admin            |
| /users/:id             | GET         | Returns a user by ID                                 | N/A            | 200                   | Login required                            |
| /users/                | POST        | Sign up a new user (mentor or mentee)                | User object    | 201                   | N/A                                       |
| /users/login           | POST        | Login an existing user                               | User object    | 200                   | N/A                                       |
| /users/:id             | PUT         | Update a user profile by ID                          | User object    | 200                   | Login required / Must be the user         |
| /users/:id             | DELETE      | Delete a user profile by ID                          | N/A            | 200                   | Login required / Must be the user         |

## Database Schema

The database schema has been simplified to support core functionalities and reduce complexity. The platform is built around three primary tables: **User**, **Mentorship Project**, and **Pledge**.

![MentHub Database Schema](crowdfunding/images/menthub_database_schema.png)

## Next Steps

1. Implement advanced search options for a more refined user experience.
2. Enhance the notification system for more personalised updates.
3. Develop a dashboard for users to track mentorship progress and feedback.
