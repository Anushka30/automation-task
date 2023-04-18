# Automate Gmail replies with Javascript and Gmail API

## 1. Create a new Google Apps Script project:

- a. Go to script.google.com and create a new project.

- b. Give your project a name, for example, "AutomatedReplyToRecruiters".

- c. In the 'Code.gs' file, delete any default content.

## 2. Customize the code:

- a. Replace `keyword1`, `keyword2`, and `keyword3` in the `REQUIRED_KEYWORDS` array with the keywords you want to search for in the email.

- b. Replace `recruiter@example.com` in the `SEARCH_QUERY` variable with the actual email address or domain you want to target.

- c. Modify the `AUTO_REPLY_MESSAGE` variable to include the message you want to send as an automated reply.

## 3. Save your script.

## 4. Enable Gmail API:

- a. Click on the plus sign next to `Services` in the left-hand panel.

- b. Find and select `Gmail API` from the list, and then click `Add`.

## 5. Set up a trigger to run the script:

- a. Click on the clock icon (triggers) in the left-hand panel.

- b. Click `Add Trigger` in the bottom right corner.

- c. Set up the trigger settings:

  - Choose which function to run: `automatedReplyToRecruiters`
  - Deployment: `Head`
  - Event source: `Time-driven`
  - Select the time interval you prefer (e.g., every 5 minutes, hourly, daily, etc.).

- d. Click `Save`.

## 6. Grant the required permissions when prompted.

Script will automatically check your Gmail account for new emails from the specified sender with the required keywords at the chosen time interval. If the email contains all the required keywords, the script will send an auto-reply and mark the email as read.
