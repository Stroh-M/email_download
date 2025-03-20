# Email Automation and Unsubscribe Link Extractor

## Overview
This project consists of two Python scripts designed to automate Gmail interactions using IMAP. The scripts serve different purposes:

- **getemail.py:** Connects to Gmail, searches for emails from a specified sender, downloads any attachments to a designated folder, and moves the processed emails to trash.
- **unsubscribeEmail.py:** Searches for emails containing unsubscribe links, extracts these links from the HTML content of the emails, compiles them into an HTML file, and opens that file in your default browser for interaction.

Both scripts leverage environment variables for configuration and use libraries such as `python-dotenv` and `BeautifulSoup`.

## Prerequisites
- **Python 3.12 or later** is required.
- **IMAP access** must be enabled on your Gmail account.
- **Environment Variables:** You need to set the following in a `.env` file:
  - `EMAIL_USER`: Your Gmail address.
  - `EMAIL_PASSWORD`: Your Gmail password (or an app-specific password if using two-factor authentication).
  - `EMAILS_FROM`: The sender’s email address to filter emails (used in *getemail.py*).
- The required Python packages are:
  - `python-dotenv`
  - `beautifulsoup4`

## Installation
Install the necessary packages with:
```bash
pip install python-dotenv beautifulsoup4
```

## Configuration
1. **Environment Variables:**  
   Create a `.env` file in the root directory of the project with content similar to:
   ```
   EMAIL_USER=your.email@gmail.com
   EMAIL_PASSWORD=yourpassword
   EMAILS_FROM=sender@example.com
   ```
   Replace the placeholders with your actual Gmail credentials and desired sender address.

2. **File Paths:**  
   - In **getemail.py**, attachments are saved to:  
     `C:\Users\meir.stroh\OneDrive\new\downloaded\`
   - In **unsubscribeEmail.py**, unsubscribe links are written to:  
     `C:\Users\meir.stroh\OneDrive\new\unsubscribeLinks\links.html`  
     
   Modify these paths within the scripts as needed to suit your environment.

## Usage

### Running getemail.py
This script logs into your Gmail account, downloads attachments from emails sent by a specified sender, and then moves those emails to trash before permanently deleting them.
  
To run the script, execute:
```bash
python getemail.py
```
> **Caution:** This script deletes emails. It is recommended to test with a non-critical or test account first.

### Running unsubscribeEmail.py
This script scans your Inbox for emails containing the term "Unsubscribe", parses the HTML content to extract links, and compiles these links into an HTML file. It then opens the file in your default web browser, allowing you to click on the unsubscribe links manually.

To run the script, execute:
```bash
python unsubscribeEmail.py
```

## Project Structure
- **getemail.py:**  
  Handles email connection, attachment download, and email deletion.
- **unsubscribeEmail.py:**  
  Searches for unsubscribe links in emails, processes HTML content, and opens an output file in a browser.
- **.env:**  
  Stores environment variables (this file should be kept secure and not committed to version control).

## Cautions
- **Email Deletion:** Both scripts perform deletion actions on emails. Always test on a safe account to avoid accidental loss of important data.
- **Security:** Protect your credentials by not sharing or committing the `.env` file.
- **Hard-Coded Paths:** Update file paths as necessary for your operating system and directory structure.

## Future Improvements
- **Error Handling:** Enhance logging and error handling to manage unexpected issues.
- **Configuration Flexibility:** Make file paths and other settings configurable through command-line arguments or additional environment variables.
- **Extended Filtering:** Expand email filtering criteria for more targeted processing.
- **Automated Clicking of Unsubscribe Links:**  
  The next step is to have the script automatically click on the unsubscribe links instead of manually opening the HTML file. This could be achieved using browser automation tools such as Selenium. However, this feature should be implemented with caution due to potential security implications and varying unsubscribe mechanisms.
