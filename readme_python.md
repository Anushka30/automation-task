# Automate Gmail replies with Python and Gmail API

## Prerequisites

- Gmail account
- Python 3.x
- Google API Console project with Gmail API enabled
- Google API credentials (Client ID and Secret)

## Step 1: Install the Google Client Library for Python

pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

## 2. Set up your project and obtain your Google API credentials

- a. Go to the Google API Console: https://console.developers.google.com/

- b. Create a new project or select an existing one.

- c. In the Dashboard, click "Enable APIs and Services" and enable the Gmail API.

- d. Create OAuth 2.0 credentials (Client ID and Secret) by going to "Credentials" in the left-hand panel and then clicking on "Create Credentials".

- e. Download the JSON file containing your Client ID and Secret and save it as "credentials.json" in your working directory.

## 3. Create a Python script named `automated_reply_to_recruiters.py` and copy the following code.

## 4. Customize the code:

- a. Replace `keyword1`, `keyword2`, and `keyword3` in the `REQUIRED_KEYWORDS` list with the keywords you want to search for in the email.

- b. Replace `'recruiter@example.com'` in the `query` variable with the actual email address or domain you want to target.

- c. Modify the `AUTO_REPLY_MESSAGE` variable to include the message you want to send as an automated reply.

## 5. Run the script:

`python automated_reply_to_recruiters.py`

This script will check your Gmail account for new emails from the specified sender with the required keywords. If the email contains all the required keywords, the script will send an auto-reply and mark the email as read.

<strong>Note :</strong> You will need to run the script manually or schedule it to run periodically using a task scheduler like cron on Unix-based systems or Task Scheduler on Windows. The script uses OAuth 2.0 for authentication, so you will need to authorize the app the first time you run it. After that, the access token will be saved in a `token.pickle` file in the same directory for future use.

#

## In the workflow:

- First, you set up a new Google Apps Script project.
- You customize the script with your specific requirements, such as the required keywords, sender's email address or domain, and auto-reply message.
- You save the script and set up a time-driven trigger that runs the script at regular intervals (e.g., every 5 minutes, hourly, daily, etc.).
- The trigger runs the script based on the selected time interval.
- The script searches your Gmail account for new emails from the specified sender.
- For each email found, the script checks if it contains all the required keywords.
- 6a. If the email contains all the required keywords, the script creates a draft reply with the specified message.
- 6b. If the email does not contain all the required keywords, the script does nothing and proceeds to the next email, if any.
- You can then review and send the draft email manually.

#

## Steps to Create OAuth 2.0 Credentials in the Google API Console

<ol>
 <li>Go to the Google API Console.</li>
 <li>Sign in with your Google account if you haven't already.</li>
 <li>In the top-left corner, click on the project dropdown and either select an existing project or create a new one by clicking the "New Project" button.</li>
 <li>After selecting or creating a project, you'll be redirected to the Dashboard. Click "Enable APIs and Services" at the top.</li>
 <li>In the API Library, search for "Gmail API" and select it.</li>
 <li>Click "Enable" to enable the Gmail API for your project.</li>
 <li>After the Gmail API is enabled, click "Create Credentials" in the top-right corner of the screen.</li>
 <li>In the "Create credentials" form, fill out the required information:
 <li>a. Which API are you using? Select "Gmail API".</li>
 <li>b. Where will you be calling the API from? Choose "Desktop app".</li>
 <li>c. What data will you be accessing? Select "User data".</li>
 <li>Click "Next".</li>
 <li>On the "Create OAuth 2.0 client ID" screen, enter a name for your OAuth 2.0 client. You can also add an icon if you want, but it's optional.</li>
 <li>Click "Create".</li>
 <li>After the OAuth 2.0 client is created, you'll see a popup with your Client ID and Secret. Click "Download" to download the JSON file containing your Client ID and Secret. Save this file as "credentials.json" in the same directory as your Python script.</li>
 <li>Click "Done".</li>

Now you have successfully created OAuth 2.0 credentials (Client ID and Secret) for your project. You can use these credentials in your Python script to authenticate and access the Gmail API.

</ol>
