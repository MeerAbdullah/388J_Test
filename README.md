# CMSC388J - Final Project Writeup

## Code Repo
- [GitHub Repository](https://github.com/MeerAbdullah/388J_Test)

## Deployed Website
- [Visit Here](https://final-proj-388j.vercel.app/)

## Project Description
**Q1 Description of your final project idea:**
We made an app called Snipz. Snipz is similar to a Stack Overflow type of web app where you can upload a snippet of your code in any language, and store or share it from the website. The users upload their code and browse through other snippets and search for any specific ones. Searching can be specific like for the title of the code, different tags, languages, and difficulty. On top of that, users can comment under snippets and share them with people too via email, like/dislike them, and even save them to their account.

**Q2 Describe what functionality will only be available to logged-in users:**
1. Snippet uploads (they can put the certain tags/language on it too, and if it's rated easy, medium, hard, etc).
2. Saving snippets of code (they can have an album or something and check them later).
3. Liking, disliking, and commenting on snippets.
4. Sharing the snippets of code via email.
5. Viewing saved snippets and comments/reviews.

**Q3 List and describe at least 4 forms:**
1. Registration form - signing up new users (user, email, password)
2. Login form - for users to access their accounts
3. Uploading snippet of code form - allows users to submit their code snippets (maybe title, the code itself, coding language, tags for the code)
4. Sharing snippet form - sharing a snippet with someone (maybe share with email).
5. Review form - for commenting on snippets
6. Search Form - search for snippet given info (title, tag(s), difficulty, language).
7. Update Profile Pic form - updates profile pic
8. Update username form - updates username.

**Q4 List and describe your routes/blueprints (don’t need to list all routes/blueprints you may have–just enough for the requirement):**
- **User Blueprint**
  - /register - register a user
  - /login - login a user
  - /logout - logging out a user
  - /account - takes users to their account pages and shows additional info.
- **Snippet Blueprint**
  - /index where users can search for snippets.
  - /upload - logging out a user
  - /snippet/<snippet_id> - to display certain snippet upload
  - /like-snippet/<string:snippet_id> - likes snippet and stores user in a likes list
  - /dislike-snippet/<string:snippet_id> - dislikes snippet, stores user in dislikes list
  - /send-email/<string:snippet_id> - sends email of snippet title and url to recipient.
  - /save-snippet/<string:snippet_id> - saves snippet to given user in MongoDB
  - /my-snippets - loads all snippets saved by the user on account page.

**Q5 Describe what will be stored/retrieved from MongoDB:**
1. accounts of users - usernames, pw, email, etc
2. code snippets - info about code snippets like title, code lang, difficulty, tags, etc
3. review/comments - comments made by users
4. Saved snippets - snippets saved by users

**Q6 Describe what Python package or API you will use and how it will affect the user experience:**
We will use flask-mail as the additional python package/API, as this will allow users to send emails to other people via a text field. Using flask-mail allows users to comment with each other and allow them to even send snippets to their friends. There are multiple platforms involved in this which makes it affect the UI greatly.

**Q7 What has changed from the original proposal:**
Everything stated in the original proposal was implemented. I mentioned in a sentence in the older proposal how we would implement a download functionality for the snippets, but we did not implement that. At the time we meant ‘download’ as in saving the snippets to the users account, and that we did implement. There was additional stuff implemented such as making the code colored, and this was done using Prism.js (this wasn't mentioned in the older proposal, but we implemented it because I thought it would make the UI look prettier🙂). Only other things that were added that were not mentioned in the older proposal were additional routes to handle certain functionality, and more specific stuff but that's all. Overall though, the website itself should be straightforward to navigate and use (note: there’s more functionality when registering and logging into an account in comparison to not being logged in).


**NOTE FOR RUNNING LOCALLY**

Look at the following link to get your gmail app password to store as an environment variable to send emails: <br/>
https://blog.coffeeinc.in/how-to-send-a-mail-using-flask-mail-and-gmail-smtp-in-python-eb235e5b2048 <br/>


Do the following before sending emails. If it doesnt work, check your environment and redo these steps. <br/>

Windows: <br/>
setx MAIL_USERNAME "your_mail_username" (i.e, 'some_email@gmail.com) <br/>
set MAIL_USERNAME="your_mail_username" <br/>
echo %MAIL_USERNAME% <br/>

setx MAIL_PASSWORD "your_mail_password" <br/>
set MAIL_PASSWORD="your_mail_password" <br/>
echo %MAIL_PASSWORD% <br/>

Mac: <br/>
export MAIL_USERNAME="YOUR_MAIL_USER" (i.e, 'some_email@gmail.com) <br/>
echo $MAIL_USERNAME <br/>

export MAIL_PASSWORD="YOUR_MAIL_PASSWORD" (received from link above - make sure to read the steps) <br/>
echo $MAIL_PASSWORD <br/>

after this, all you need to do to run the program is cd /snipz then execute 'flask run' in terminal <br/>
