# Email Automation and Unsubscribe Link Extractor

## Overview
This project consists of two Python scripts designed to automate Gmail interactions via IMAP. The scripts serve distinct purposes:

- **getemail.py:** Connects to Gmail, searches for emails from a specified sender, downloads any attachments to a designated folder, and then moves the processed emails to trash before permanently deleting them.
- **unsubscribeEmail.py:** Scans your Inbox for emails containing the keyword "Unsubscribe," extracts unsubscribe links from the HTML content, compiles these links into an HTML file, and opens that file in your default browser for interactive use.

Both scripts utilize environment variables for configuration and employ libraries such as `python-dotenv` (with override enabled) and `BeautifulSoup`.

## Prerequisites
- **Python 3.12 or later** is required.
- **IMAP access** must be enabled on your Gmail account.
- **Environment Variables:** Create a `.env` file with the following variables:
  - `EMAIL_USER`: Your Gmail address.
  - `EMAIL_PASSWORD`: Your Gmail password (or an app-specific password if using two-factor authentication).
  - `EMAILS_FROM`: The sender’s email address used for filtering emails in *getemail.py*.
  - `DOWNLOAD_FILE_PATH`: The folder path where attachments will be saved (used in *getemail.py*).

- Required Python packages:
  - `python-dotenv`
  - `beautifulsoup4`

## Installation
Install the necessary packages using pip:
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
   DOWNLOAD_FILE_PATH=C:\path\to\your\download\folder
   ```
   Ensure that the file is correctly named and located in the same directory from which you run the scripts.

2. **File Paths:**  
   - In **getemail.py**, attachments are saved to the folder specified by `DOWNLOAD_FILE_PATH`.
   - In **unsubscribeEmail.py**, unsubscribe links are written to:  
     `C:\Users\meir.stroh\OneDrive\new\unsubscribeLinks\links.html`
     
   Modify these paths within the scripts as needed to match your environment.

## Usage

### Running getemail.py
This script logs into your Gmail account, downloads attachments from emails sent by the specified sender, and then moves those emails to trash before permanently deleting them.

To run the script, execute:
```bash
python getemail.py
```
> **Caution:** This script permanently deletes emails. Always test on a non-critical or test account first.

### Running unsubscribeEmail.py
This script scans your Inbox for emails containing the term "Unsubscribe," parses the HTML content to extract unsubscribe links, compiles them into an HTML file, and opens that file in your default browser for further action.

To run the script, execute:
```bash
python unsubscribeEmail.py
```

## Project Structure
- **getemail.py:**  
  Connects to Gmail, downloads attachments from filtered emails, and deletes processed emails.
- **unsubscribeEmail.py:**  
  Extracts unsubscribe links from emails and generates an interactive HTML file.
- **.env:**  
  Contains environment variables (ensure this file is kept secure and not committed to version control).

## Cautions
- **Email Deletion:** Both scripts perform deletion actions on emails. Always test on a safe account to avoid accidental loss of important data.
- **Security:** Protect your credentials by not sharing or committing the `.env` file.
- **Hard-Coded Paths:** Update file paths in the scripts as necessary to match your system configuration.

## Future Improvements
- **Enhanced Error Handling:** Further improve logging and error management for unexpected issues.
- **Configuration Flexibility:** Enable specifying file paths and settings via command-line arguments.
- **Extended Email Filtering:** Expand filtering criteria for more targeted email processing.
- **Automated Clicking of Unsubscribe Links:**  
  A planned enhancement is to automatically click on the unsubscribe links using browser automation tools (such as Selenium). This feature will be implemented cautiously, considering security implications and varying unsubscribe mechanisms.