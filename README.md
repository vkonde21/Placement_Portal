# Placement_Portal
Placement portal is a web application for the placement and training department in the college. This
application helps to manage the student information with regards to the placements.This application
also notifies the students about different companies visiting the campus.

## Admin
Admin can:
1. view student details and verify them.
2. add company details such as name, location, criteria etc, delete company details .
3. create rounds for companies ,select students for the round and declare results
4. give feedback(given by companies) to students
5. view placements

## Students
Students can:
 1. update their profile, academic details and  add skills
 2. view company details, apply for companies , withdraw application and view their application status
 3. view feedbacks  
 4. If student profile is verified by admin, it cannot be updated.  
 5. Once a student gets selected for a particular company he/she is no longer eligible for further companies.  
 
  ## Technology used:
  - Frontend: HTML
  - Backend: Django
  - Database: sqlite3
 
  ## ER Diagram:
  ![.](https://go.gliffy.com/go/view/13366393.png?size=large)
  
  
  ## Relational Schema:
  ![.](https://go.gliffy.com/go/view/13365224.png?size=large)
  
  ## Requirements:
  - Python 3.7.4
  - django 3.0.6
  - crispy_forms
  
  ## Run server locally:
  1. Clone the repository
  2. Run `python manage.py runserver` in server directory
  3. Go to: `localhost:8000`
  
  ## Screenshots:
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/register.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/login.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/homepage.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/yourstatus.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/academicdetails.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/adminhome.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/addcompany.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/companycriteria.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/company_details.png)
  ![.](https://github.com/vkonde21/Placement_Portal/blob/master/screenshots/createshortlist.png)
  
  
  
