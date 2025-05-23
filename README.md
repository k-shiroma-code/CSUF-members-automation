# CSUF Members Automation

## Overview
This script automates the update of a club’s member list by merging the official TitanLink roster (`titanlink_roster.csv`) with an existing master file (`club_members.xlsx`). It ensures new members are added, updated if their dues status changes, and prevents duplication.

## How It Works
- The VP of Finance downloads the latest roster from TitanLink.
- They run `updated_members.py`.
- The script merges and cleans the data, updating `club_members.xlsx`.

## Features
- Automatically removes duplicate entries based on email.
- Keeps the latest version of each member's record.
- Simple, fast, and portable — no database or API access needed.

## Usage

1. Place the latest `titanlink_roster.csv` and your existing `club_members.xlsx` in the same folder.
2. Run the script:

```bash
python updated_members.py
