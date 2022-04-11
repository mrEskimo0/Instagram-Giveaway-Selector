# Instagram Giveaway Selector

## Description

This is a python application to automate picking instagram giveaway winners. Instagram giveaways are conducted by asking people to tag 3 people in a comment under the desired post and follow specific accounts. This application goes through instagram comments and checks if the comments under the giveaway post meet these qualifications, adds the comments that qualify to a list, and randomly picks a winner from the list. This application was built using Python and Python library Instaloader. 

## Installation

* Install Python as you would normally install Python: https://www.python.org/downloads/

* Install the Instaloader library

```bash
 Pip install instaloader
 ```

* Download this repository

* Create a new instagram account: https://www.instagram.com/

* Create a file named "credentials.py" in the downloaded repository with the USERNAME and PASSWORD in it.
```python
USERNAME="instagramusername"
PASSWORD="instagrampassword"
```

## User Guide

This application is designed to be used on the command line. First users will be prompted to input the account name of the Giveaway Account. Next, users will input the account names of Accounts that giveaway contestants need to be following to win. <b>The giveaway account is automatically added to the list of accounts that need to be followed, adding it twice will cause the application to not pick a winner.</b> Once all accounts that need to be followed are added, input q to move on. The user will then be prompted to input the shortcode of the giveaway post. The Shortcode can be found by selecting the post on the browser, and finding the string of characters after /p/, and up to the final / of the url. For example, https://www.instagram.com/p/THIS IS THE SHORTCODE/, simply copy the characters that would be in "THIS IS THE SHORTCODE". 

Once the shortcode is entered, wait for the program to finish running and the winner will be printed in the command line window. 