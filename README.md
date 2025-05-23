# CSUF Members Automation

This project was created to help a student club at California State University, Fullerton automatically maintain an up-to-date member list and track dues payments — without needing direct API access to their system.

## Overview

Normally, access to a third-party API would be required to automate data collection and updates. However, since no API access was authorized, I implemented a workaround using Bash scripting, file automation, and cron jobs.

## Features

- **No API Access Required**: Utilizes a manual `.xlsx` file input system instead of API-based data pulls.
- **Excel-Based Workflow**: Club leaders send out an `.xlsx` template for members to fill out (including name, email, dues paid status, etc.).
- **Automated File Processing**: A scheduled cron job monitors for updates and:
  - Cleans and processes new submissions
  - Updates the master member list
  - Logs changes for reference
- **Two-File System**:
  - `raw_members.xlsx`: Contains raw data from member submissions.
  - `cleaned_members.xlsx`: Maintains an up-to-date, clean list of current members and their dues status.

## Tools Used

- Bash scripting
- Cron (Linux job scheduler)
- `xlsx2csv` or similar tools for handling `.xlsx` files in shell scripts (can be replaced with Python if desired)

## How It Works

1. Club officers distribute a pre-formatted `.xlsx` file to members.
2. Members fill in their information and email it back.
3. A cron job runs at scheduled intervals to check for new files.
4. The script processes the data and updates the cleaned member list automatically.
5. The club receives a regularly updated membership file with dues tracking built in.

## Benefits

- Eliminates the need for manual updates.
- Works without API access.
- Reduces human error.
- Provides clean, consistent, and up-to-date data for club operations.

---

**Note**: This project was developed strictly for internal club use, and no unauthorized access to any private data or systems was made.
