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
| Mobile (DevTools) | ![screenshot](documentation/responsive-mobile.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/responsive-tablet.png) | Works as expected |
| Desktop | ![screenshot](documentation/responsive-desktop.png) | Works as expected |
| XL Monitor | ![screenshot](documentation/responsive-xl.png) | Scaling starts to have minor issues |
| 4K Monitor | ![screenshot](documentation/responsive-4k.png) | Noticeable scaling issues |
| Google Pixel 7 Pro | ![screenshot](documentation/responsive-pixel.png) | Works as expected |
| iPhone 14 | ![screenshot](documentation/responsive-iphone.png) | Works as expected |
| x | x | repeat for any other tested sizes |

## Lighthouse Audit

Make sure to test the Lighthouse Audit results for all of your pages.

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Size | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | Mobile | ![screenshot](documentation/lighthouse-home-mobile.png) | Some minor warnings |
| Home | Desktop | ![screenshot](documentation/lighthouse-home-desktop.png) | Few warnings |
| About | Mobile | ![screenshot](documentation/lighthouse-about-mobile.png) | Some minor warnings |
| About | Desktop | ![screenshot](documentation/lighthouse-about-desktop.png) | Few warnings |
| Gallery | Mobile | ![screenshot](documentation/lighthouse-gallery-mobile.png) | Slow response time due to large images |
| Gallery | Desktop | ![screenshot](documentation/lighthouse-gallery-desktop.png) | Slow response time due to large images |
| x | x | x | repeat for any other tested pages/sizes |

## Defensive Programming

Forms:
- Users cannot submit an empty form
- Users must enter valid email addresses

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
| Gallery Page | | | | |
| | Click on Gallery link in navbar | Redirection to Gallery page | Pass | |
| | Load gallery images | All images load as expected | Pass | |
| Contact Page | | | | |
| | Click on Contact link in navbar | Redirection to Contact page | Pass | |
| | Enter first/last name | Field will accept freeform text | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter message in textarea | Field will accept freeform text | Pass | |
| | Click the Submit button | Redirects user to form-dump | Pass | User must click 'Back' button to return |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| Profile | | | | |
| | Click on Profile button | User will be redirected to the Profile page | Pass | |
| | Click on the Edit button | User will be redirected to the edit profile page | Pass | |
| | Click on the My Orders link | User will be redirected to the My Orders page | Pass | |
| | Brute forcing the URL to get to another user's profile | User should be given an error | Pass | Redirects user back to own profile |

Repeat for all other tests, as applicable to your own site.
The aforementioned tests are just an example of a few different project scenarios.

## User Story Testing

Testing user stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **features** should already align with the **user stories**,
so this should as simple as creating a table with the user story, matching with the re-used screenshot
from the respective feature.

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

It's very important to document any bugs you've discovered while developing the project.
Make sure to include any necessary steps you've implemented to fix the bug(s) as well.

For JavaScript and Python applications, it's best to screenshot the errors to include them as well.

**PRO TIP**: screenshots of bugs are extremely helpful, and go a long way!

- JS Uncaught ReferenceError: `foobar` is undefined/not defined

    ![screenshot](documentation/bug01.png)

    - To fix this, I _____________________.

- JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).

    ![screenshot](documentation/bug02.png)

    - To fix this, I _____________________.

- Python `'ModuleNotFoundError'` when trying to import module from imported package

    ![screenshot](documentation/bug03.png)

    - To fix this, I _____________________.

- Django `TemplateDoesNotExist` at /appname/path appname/template_name.html

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

- Python `E501 line too long` (93 > 79 characters)

    ![screenshot](documentation/bug04.png)

    - To fix this, I _____________________.

### GitHub **Issues**

An improved way to manage bugs is to use the built-in **Issues** tracker on your GitHub repository.
To access your Issues, click on the "Issues" tab at the top of your repository.
Alternatively, use this link: https://github.com/katkapsasky/cakes-and-bakes/issues

If using the Issues tracker for your bug management, you can simplify the documentation process.
Issues allow you to directly paste screenshots into the issue without having to first save the screenshot locally,
then uploading into your project.

You can add labels to your issues (`bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s).

Once you've sorted the issue, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following format:

**Fixed Bugs**

All previously closed/fixed bugs can be tracked [here](https://github.com/katkapsasky/cakes-and-bakes/issues?q=is%3Aissue+is%3Aclosed).

| Bug | Status |
| --- | --- |
| [JS Uncaught ReferenceError: `foobar` is undefined/not defined](https://github.com/katkapsasky/cakes-and-bakes/issues/1) | Closed |
| [Python `'ModuleNotFoundError'` when trying to import module from imported package](https://github.com/katkapsasky/cakes-and-bakes/issues/2) | Closed |
| [Django `TemplateDoesNotExist` at /appname/path appname/template_name.html](https://github.com/katkapsasky/cakes-and-bakes/issues/3) | Closed |

**Open Issues**

Any remaining open issues can be tracked [here](https://github.com/katkapsasky/cakes-and-bakes/issues).

| Bug | Status |
| --- | --- |
| [JS `'let'` or `'const'` or `'template literal syntax'` or `'arrow function syntax (=>)'` is available in ES6 (use `'esversion: 11'`) or Mozilla JS extensions (use moz).](https://github.com/katkapsasky/cakes-and-bakes/issues/4) | Open |
| [Python `E501 line too long` (93 > 79 characters)](https://github.com/katkapsasky/cakes-and-bakes/issues/5) | Open |

## Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed.
This section should include shortcomings of the frameworks or technologies used.
Although time can be a big variable to consider, paucity of time and difficulty understanding
implementation is not a valid reason to leave bugs unfixed.

If you've identified any unfixed bugs, no matter how small, be sure to list them here.
It's better to be honest and list them, because if it's not documented and an assessor finds the issue,
they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

Some examples:

- On devices smaller than 375px, the page starts to have `overflow-x` scrolling.

    ![screenshot](documentation/unfixed-bug01.png)

    - Attempted fix: I tried to add additional media queries to handle this, but things started becoming too small to read.

- For PP3, when using a helper `clear()` function, any text above the height of the terminal does not clear, and remains when you scroll up.

    ![screenshot](documentation/unfixed-bug02.png)

    - Attempted fix: I tried to adjust the terminal size, but it only resizes the actual terminal, not the allowable area for text.

- When validating HTML with a semantic `section` element, the validator warns about lacking a header `h2-h6`. This is acceptable.

    ![screenshot](documentation/unfixed-bug03.png)

    - Attempted fix: this is a known warning and acceptable, and my section doesn't require a header since it's dynamically added via JS.

If you legitimately cannot find any unfixed bugs or warnings, then use the following sentence:

There are no remaining bugs that I am aware of.
