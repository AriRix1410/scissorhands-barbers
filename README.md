# Scissorhand's Barbers

Scissorhand's Barbers is a fictional barbershop situated in York, England. The aim of this site is to allow users the ability to make booking requests, view their confirmed bookings and to write and read testimonials.

The site is responsive and has been styled using the Agency theme from [StartBootstrap](https://startbootstrap.com/theme/agency). Languages and frameworks used for this project are HTML, CSS, JavaScript, Python and Django. Agile methodology has been used to plan and design this project using an MVC framework.

The live link to this project can be found here - http://scissorhands-barbers.herokuapp.com/

![Responsive Mockup](static/assets/img/readme/mock-up.png)

## User Stories

### First Time Visitor Goals:
1. As a First Time Visitor, I should be able to view offered services.
2. As a First Time Visitor, I should be able to read about the business.
3. As a First Time Visitor, I should be able to view testimonials.
4. As a First Time Visitor, I should be able to make an account.

### Returning Visitor Goals:
5. As a Returning Visitor, I should be able to request a booking.
6. As a Returning Visitor, I should be able to view my bookings.
7. As a Returning Visitor, I should be able to cancel or delete my bookings.
8. As a Returning Visitor, I should be able to write a testimonial.
9. As a Returning Visitor, I should be able to edit or delete my testimonials.

### Site Admin Goals:
10. As a Site Admin, I should be able to approve testimonials to filter spam or bad language.
11. As a Site Admin, I should be able to confirm bookings to minimize risk of double bookings.

## Design

- The initial design of this project was done via a Theme named Agency, a downloaded theme from [StartBootstrap](https://startbootstrap.com/theme/agency). I chose this theme because I felt it refelected the branding that I was trying to create for this business, a quirky and edgy Barbershop located in York, England. I then altered this theme to meet my own requirements.

## Features 

### Existing Features

- __Header/Navigation Bar__
  - This is featured on all pages and is fully responsive. This area includes links to the page sections Services, About, Locate Us as well as pages for Testimonials and Bookings. If the user is not logged in then there are links to register or login in. If the user is already logged in then there is a link to logout. This is replicated on each page to make navigation easier. For smaller screen sizes, the navbar becomes a drop down.
  - The logo is displayed in the top left of the page with navigation links displayed to the right.
  - The navigation bar allows users to be able to easily navigate between all sections and pages, on all devices.   

![Header/Nav Bar](static/assets/img/readme/navbar-login-register.png)
![Header/Nav Bar](static/assets/img/readme/navbar-logout.png)

- __The Landing Page/Masthead__

  - This section includes a photograph with text overlay to allow users to see exactly what the business is.
  - The masthead image is located on all pages to tie the full site together, I chose this image as it reflected the vintage style and branding I was trying to create for this business.
  - The landing page masthead displays a welcome message, a slogan and a button which navigates to the services section. On all other pages, this just displays the page name.

![Landing Page](static/assets/img/readme/landing-page.png)

- __Services__
  - This section allows users to see what services are offered at this barbers and the images used reflect this.
  - To further add to the branding and show users what Scissorhand's is about, a subheading of "Vintage Cuts, Modern Styles" is included in this section.
  - Also included is a brief paragraph with the aim in showing further services offered and that Scissorhand's caters for all potential clients regardless of their age.

  ![Services](static/assets/img/readme/services.png)

- __About__
  - This section allows users to learn abit about the business as well as information about the barbers.
  - In this section, I have wrote a brief history of the business and an introduction of the barbers such as when they qualified and what they like to do. This is to give the business a more welcoming feel towards new users.
  - Also included here are photographs of the barbers, again to provide new users with with a sense of familiarity towards the business.

  ![About](static/assets/img/readme/about-us-images.png)
  ![About](static/assets/img/readme/about-us-blurb.png)
  
- __Locate Us__
  - This section allows users to see the location of the barbershop.
  - In this section, users can see the address of the business as well as Google map of the location.
  - For this section, I have used a Google Map API to show an exact, marked location of where the barbershop would be situated. I thought this added a nice touch to the page and made for a better user experience. 

  ![Locate](static/assets/img/readme/locate.png)

- __Testimonials__
  - This section allows users to see the location of the barbershop.
  - In this section, users can see the address of the business as well as Google map of the location.
  - For this section, I have used a Google Map API to show an exact, marked location of where the barbershop would be situated. I thought this added a nice touch to the page and made for a better user experience. 

  ![Testimonials](static/assets/img/readme/locate.png)
  ![Testimonials](static/assets/img/readme/locate.png)

- __Bookings__
  - This section allows users to see the location of the barbershop.
  - In this section, users can see the address of the business as well as Google map of the location.
  - For this section, I have used a Google Map API to show an exact, marked location of where the barbershop would be situated. I thought this added a nice touch to the page and made for a better user experience. 

  ![Locate](static/assets/img/readme/locate.png)
  ![Locate](static/assets/img/readme/locate.png)
  ![Locate](static/assets/img/readme/locate.png)

- __Register/Login__
  - This 
  -
  -

### Features Left to Implement

- A feature I would like to add in the future is to have more questions and to randomise them so users would have to answer any 20 guestions that are randomly selected by the computer, in order to provide a better user experience.
- I would also like for users to be able to see their previous scores.

## Agile

Google Sheets was used to store the data for the user's name and score. When the quiz ends this data is sorted numerically in order of highest scores to lowest and when the user no longer wants to play, the top 5 highest scores are displayed.

![High Scores Sheet](/assets/images/scores-sheet.png)

This project also contains a questions Class in order to store both the prompts to the questions and also the question answers.

## Logic

### Flowchart

![Flowchart](/assets/images/flowchart.png)

## Testing

I have manually tested this project in the following ways:

- All code has been passed through the [PEP8 Python Validator](http://pep8online.com/checkresult) with no issues.

![PEP8 Run](/assets/images/pep8.png)
![PEP8 Class](/assets/images/pep8-class.png)
![PEP8 Questions](/assets/images/pep8-questions.png)

- Given invalid inputs such as names that are over 6 characters in length, names that contain symbols, answers other than a, b, c or d and inputs different to y or n when only y or n are required.
- Tested in my local terminal on Gitpod and in the Code Institute Heroku terminal.

### Bugs

- When trying to set up user input validation for my questions, I encountered an issue where the error message would print but would still accept the input and proceed further in the game. This was due to me putting the if and while statements in my loop in the wrong order. When switched, the code performed as expected.
- When writing the code for the high scores, the scores after sorting where sorted alphanumerically, this caused the high scores to be incorrect as numbers such as 11 and 14 where lower than other scores with a lower value as the first digit was lower. After recieving help in Stack Overflow, I was able to convert the scores into integers and then the scores were in the correct order.
- Initially, instead of get_all_values, I used col_values. Although this did sort the scores, I realised that by doing this, the corresponding names to the scores were not being printed and instead was just the 5 first name entries on Google sheets. By using get_all_values instead, I was able to sort by the scores column but also print the correct names for those scores.
- By using the method above, I encountered another problem where it was sorting the first column which contains the name data as opposed to the second column which contained the score data. This was due to a problem with my indexing being incorrect. After researching again, I was able to re-write this so that the data being sorted was from the scores column and the issue was fixed.

### Unfixed Bugs

- No unfixed bugs

### Validator Testing

- [PEP8 Python Validator](http://pep8online.com/checkresult) - no issues

## Deployment

- This project has been deployed to Heroku. The steps to deploy are as follows: 
  - Create a new Heroku app
  - In the settings tab, set two Config Vars, one for CREDS.json file, and one setting PORT to 8000 
  - Scroll down and set the build packs to Python and NodeJS, in that order
  - Click on depoly and link the Heroku app to the Github repositary
  - Scroll down to manual deploy and click deploy branch
  - After some time, a message will be displayed stating the app was successfully deployed
  - You can then click on view to see the deployed project.

## Credits  

### Content 

- The initial inspiration and code for this project was taken from [Mike Dane](https://www.youtube.com/watch?v=SgQhwtIoQ7o) and [Bro Code](https://www.youtube.com/watch?v=yriw5Zh406s&list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&index=2), then edited and expanded for my own requirements.
- [Stack Overflow](https://stackoverflow.com) was a great source of information throughout the project but was particularly used for help with user input validation [here](https://stackoverflow.com/questions/71757895/user-input-validation-in-python), when trying to sort the high scores [here](https://stackoverflow.com/questions/71785967/sorting-column-b-google-sheets-api-python) where I ended up physically asking for help after struggling for a considerable amount of time, with the same issues.
- [Code Institute](https://learn.codeinstitute.net/) Python Essentials tutorials were consulted throughout for clarification and understanding, especially the Love Sandwiches project which was inspiration for the get_name and check_name functions.
- [Real Python](https://realpython.com/python-sort/) and [DelftStack](https://www.delftstack.com/howto/python/sort-list-of-lists-in-python/) with help on sorting.
- [Geeks For Geeks](https://www.geeksforgeeks.org/python-get-first-and-last-elements-of-a-list/) and [Career Karma](https://careerkarma.com/blog/python-indexerror-list-index-out-of-range/) with help on list comprehension.
- The ASCII title in this project came from [Patorjk](https://patorjk.com/software/taag/#p=display&f=Standard&t=STAR%20WARS%20QUIZ)
- Questions for the quiz have came from [Ultimate Quiz Questions](https://www.ultimatequizquestions.com/star-wars-quiz-questions/), [Radio Times](https://www.radiotimes.com/tv/sci-fi/pub-quiz-star-wars/) and [Thought Catalog](https://thoughtcatalog.com/katee-fletcher/2020/04/star-wars-trivia-questions/)

### Special Thanks

- Thanks to my mentor Caleb Mbakwe for his insight and guidance throughout.