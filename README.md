# MentHub: Tech Mentor Matching Platform for Women in STEM

## Crowdfunding Back End

**MentHub**

---

### Planning:

**Concept/Name**  
MentHub is the name I chose for my project because it's sleek, memorable, and reflects the central role of mentorship. I also considered using MNTX for a techy feel with minimal vowels.

**Intended Audience/User Stories**

- Women in STEM looking for mentorship to navigate their careers.
- Immigrant women in tech who are seeking guidance on transitioning into the tech industry in new countries.
- Mentors who are experienced professionals in STEM fields and want to give back by mentoring other women.

**Front End Pages/Functionality**

1. **Homepage**

   - Navigation bar with Sign up/Login buttons.
   - Create Mentorship Projects button.
   - Display all mentorship projects.
   - Search bar to filter projects by category or skillset.
   - Button to view project details.
   - Footer with social media links and contact info.

2. **Mentorship Project Details Page**

   - Show project owner and mentors who pledged to the project.
   - Display project description, required skills, and target mentorship hours.
   - Progress bar showing pledged hours and total target hours.
   - History of mentor pledges with comments.
   - Button for mentors to pledge hours.
   - Button for updating project details (only available to the owner).

3. **Profile Page**

   - Separate views for mentors and mentees.
   - Mentors can list their expertise, availability, and contact preferences.
   - Mentees can list their career goals, skills they want to learn, and mentorship needs.
   - Edit buttons to update personal details.
   - View of all projects created (for mentees) or pledged to (for mentors).

4. **Error Handling Page**
   - Display error messages for failed logins, unauthorized access, or invalid inputs.
   - Show appropriate messages when certain fields are missing.

---

### API Spec

| URL                    | HTTP Method | Purpose                                                         | Request Body   | Success Response Code | Authentication/Authorisation              |
| ---------------------- | ----------- | --------------------------------------------------------------- | -------------- | --------------------- | ----------------------------------------- |
| /mentors/              | GET         | Returns a list of all mentors                                   | N/A            | 200                   | N/A                                       |
| /mentors/:id           | GET         | Returns a mentor by ID                                          | N/A            | 200                   | N/A                                       |
| /mentors/              | POST        | Create a new mentor profile                                     | Mentor object  | 201                   | Login required                            |
| /mentors/:id           | PUT         | Update a mentor profile                                         | Mentor object  | 200                   | Login required / Must be the mentor       |
| /mentors/:id           | DELETE      | Delete a mentor profile                                         | N/A            | 200                   | Login required / Must be the mentor       |
| /mentees/              | GET         | Returns a list of all mentees                                   | N/A            | 200                   | N/A                                       |
| /mentees/:id           | GET         | Returns a mentee by ID                                          | N/A            | 200                   | N/A                                       |
| /mentees/              | POST        | Create a new mentee profile                                     | Mentee object  | 201                   | Login required                            |
| /mentees/:id           | PUT         | Update a mentee profile                                         | Mentee object  | 200                   | Login required / Must be the mentee       |
| /mentees/:id           | DELETE      | Delete a mentee profile                                         | N/A            | 200                   | Login required / Must be the mentee       |
| /projects/             | GET         | Returns a list of all mentorship projects                       | N/A            | 200                   | N/A                                       |
| /projects/:id          | GET         | Returns a mentorship project by ID                              | N/A            | 200                   | N/A                                       |
| /projects?is_open=True | GET         | Returns all open mentorship projects                            | N/A            | 200                   | N/A                                       |
| /projects/             | POST        | Create a new mentorship project                                 | Project object | 201                   | Login required / Must be a mentee         |
| /projects/:id          | PUT         | Update a mentorship project                                     | Project object | 200                   | Login required / Must be project owner    |
| /projects/:id          | DELETE      | Delete a mentorship project                                     | N/A            | 200                   | Login required / Must be project owner    |
| /projects/:id/pledges/ | GET         | Returns a list of all pledges for a specific mentorship project | N/A            | 200                   | N/A                                       |
| /pledges/              | GET         | Returns a list of all pledges made by mentors                   | N/A            | 200                   | N/A                                       |
| /pledges/:id           | GET         | Returns a pledge by ID                                          | N/A            | 200                   | N/A                                       |
| /pledges/              | POST        | Create a new pledge for mentorship hours                        | Pledge object  | 201                   | Login required / Must be a mentor         |
| /pledges/:id           | PUT         | Update a pledge                                                 | Pledge object  | 200                   | Login required / Must be the pledge owner |
| /pledges/:id           | DELETE      | Delete a pledge                                                 | N/A            | 200                   | Login required / Must be the pledge owner |
| /users/                | GET         | Returns a list of all users (mentors and mentees)               | N/A            | 200                   | Login required / Must be admin            |
| /users/:id             | GET         | Returns a user by ID                                            | N/A            | 200                   | Login required                            |
| /users/                | POST        | Sign up a new user (mentor or mentee)                           | User object    | 201                   | N/A                                       |
| /users/login           | POST        | Login an existing user                                          | User object    | 200                   | N/A                                       |
| /users/:id             | PUT         | Update a user profile by ID                                     | User object    | 200                   | Login required / Must be the user         |
| /users/:id             | DELETE      | Delete a user profile by ID                                     | N/A            | 200                   | Login required / Must be the user         |

---

### DB Schema

I've designed the database schema to include the following tables:

1. **User** (for both mentors and mentees)

   - UniqueID
   - Password
   - Email
   - First Name
   - Last Name
   - Role (mentor/mentee)
   - Availability (for mentors)
   - Career Goals (for mentees)

2. **Mentorship Project** (mentorship goals, skills required, status)

   - UniqueID
   - Title
   - Owner (a mentee)
   - Description
   - Skills required
   - Target mentorship hours
   - is_open (whether the project is open to new mentors)
   - Date of creation

3. **Pledge** (hours pledged, project reference, mentor reference)
   - UniqueID
   - Amount (number of mentorship hours)
   - Comment
   - Anonymous (whether the pledge is anonymous or not)
   - Project (foreign key linking to the mentorship project)
   - Supporter (foreign key linking to the mentor)

Below is a visual representation of the schema:

---
