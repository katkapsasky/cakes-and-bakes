# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcakes-and-bakes.herokuapp.com%2F) | ![screenshot](documentation/validation/homepage.png) | Pass: No Errors |
| Recipe Detail | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcakes-and-bakes.herokuapp.com%2Fchocolate-brownies%2F) | ![screenshot](documentation/validation/recipe-detail.png) | Pass: No Errors |
| Sign In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcakes-and-bakes.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/validation/sign-in.png) | Pass: No Errors |
| Sign Up | [W3C](https://cakes-and-bakes.herokuapp.com/accounts/signup/) | ![screenshot](documentation/validation/sign-up.png) | Pass: No Errors |
| Sign Out | n/a | ![screenshot](documentation/validation/sign-out.png) | Pass: No Errors |
| Liked Recipes | n/a | ![screenshot](documentation/validation/liked-recipes.png) | Pass: No Errors |
| Post a Recipe | n/a | ![screenshot](documentation/validation/post-recipe.png) | Pass: No Errors |
| Edit a Recipe | n/a | ![screenshot](documentation/validation/edit-recipe.png) | Pass: No Errors |
| Manage Categories | n/a | ![screenshot](documentation/validation/manage-categories.png) | Pass: No Errors |
| Add a Category | n/a | ![screenshot](documentation/validation/add-category.png) | Pass: No Errors |
| Edit a Category | n/a | ![screenshot](documentation/validation/edit-category.png) | Pass: No Errors |

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcakes-and-bakes.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![screenshot](documentation/validation/css.png) | Pass: No Errors |

### Python

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| admin.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/recipe/admin.py) | ![screenshot](documentation/validation/py-admin.png) | Pass: No Errors |
| apps.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/recipe/apps.py) | ![screenshot](documentation/validation/py-apps.png) | Pass: No Errors |
| cakesandbakes urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/cakesandbakes/urls.py) | ![screenshot](documentation/validation/py-cakesandbakes-urls.png) | Pass: No Errors |
| recipe urls.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/recipe/urls.py) | ![screenshot](documentation/validation/py-recipe-urls.png) | Pass: No Errors |
| forms.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/recipe/forms.py) | ![screenshot](documentation/validation/py-forms.png) | Pass: No Errors |
| models.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/recipe/models.py) | ![screenshot](documentation/validation/py-models.png) | Pass: No Errors |
| settings.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/cakesandbakes/settings.py) | ![screenshot](documentation/validation/py-settings.png) | Pass: No Errors |
| tests.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/recipe/tests.py) | ![screenshot](documentation/validation/py-tests.png) | Pass: No Errors |
| views.py | [CI PEP8](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/katkapsasky/cakes-and-bakes/main/recipe/views.py) | ![screenshot](documentation/validation/py-views.png) | Pass: No Errors |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Screenshot | Notes |
| --- | --- | --- |
| Chrome | ![screenshot](documentation/browser-compatibility-chrome.png) | Works as expected |
| Safari | ![screenshot](documentation/browser-compatibility-safari.png) | Works as expected |
| Edge | ![screenshot](documentation/browser-compatibility-edge.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Screenshot | Notes |
| --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/responsivity-mobile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsivity-tablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsivity-desktop.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for accessibility issues. The overall score is 94 with a couple of minor warnings.

![screenshot](documentation/lighthouse-audit.png)

## Defensive Programming

Forms:
- Users cannot submit an empty form
- Users must fill in all required form fields

Django:
- Users cannot brute-force a URL to navigate to a restricted page
- Users cannot perform CRUD functionality while logged-out
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers

Defensive programming was manually tested with the below user acceptance testing:

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home Page | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| Register Page | | | | |
| | Click on Register link in navbar | Redirection to Register page | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Log in and redirect to homepage | Pass | |
| Log In | | | | |
| | Click on Login button | Redirection to Login page | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page and logs out | Pass | |
| Liked Recipes | | | | |
| | Click on Liked Recipes link in navbar | User will be redirected to the Liked Recipes page | Pass | |
| | View Liked Recipes | Paginated list of recipes user has liked (if any have been liked otherwise empty page) | Pass | |
| Recipe Detail | | | | |
| | Click on Recipe Title from Homepage | User will be redirected to the recipe detail page | Pass | |
| | View Recipe Detail | User can view the recipe title, image, author, total time, ingredients, method | Pass | |
| Post a Recipe | | | | |
| | Click on Post Recipe link in navbar | User will be redirected to Post Recipe page | Pass | |
| | Submit new recipe form | User fills in form and submits, awaits approval in admin panel | Pass | |
| Approve a Recipe | | | | |
| | Navigate to admin panel with /admin and approve new and edited recipes | Approved recipes appear on homepage | Pass | |
| Edit a Recipe | | | | |
| | If logged in as author click edit recipe on recipe detail page | Redirect to edit recipe form page with prepopulated fields | Pass | |
| | Submit edited recipe form | Recipe form becomes unapproved and awaits approval in admin panel | Pass | |
| Delete a Recipe | | | | |
| | If logged in as author click delete recipe on recipe detail page  | Confirm deletion with modal and remove rcipe if confirmed | Pass | |
| Manage Categories (Admin) | | | | |
| | Click on Categories link in navbar | User will be redirected to the Categories page | Pass | |
| | View Existing Categories | Paginated list of existing categories | Pass | |
| | Click on Add Category | Redirected to add category form | Pass | |
| | Submit New Category | Redirect to categories page, new category visible | Pass | |
| | Delete Category | Modal confirms deletion then category is deleted once confirm is clicked | Pass | |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature01.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature02.png) |
| As a new site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature03.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature04.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature05.png) |
| As a returning site user, I would like to ____________, so that I can ____________. | ![screenshot](documentation/feature06.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature07.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature08.png) |
| As a site administrator, I should be able to ____________, so that I can ____________. | ![screenshot](documentation/feature09.png) |
| repeat for all remaining user stories | x |

## Bugs

**Fixed Bugs**


**Unfixed Bugs**

There are no remaining bugs that I am aware of.
