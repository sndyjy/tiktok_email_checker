# TikTok Email Checker (Educational Purpose Only)

⚠️ **Disclaimer:** This project is created for **educational purposes only**.\
It is intended to demonstrate web automation using Selenium.\
**Do not use this script for any unauthorized or unethical activities.**\
The author is not responsible for any misuse of this code.

---

## Overview

This script automates the process of checking whether an email is registered on TikTok Business.\
It uses Selenium to interact with the TikTok login page and verifies email availability.

## Features

- Checks if an email is registered on TikTok Business.
- Automates email entry and login attempt.
- Uses CAPTCHA bypass (manual intervention required).
- Random wait times to reduce bot detection.
- Saves results in a `results.csv` file.

## Prerequisites

- Python 3.x installed
- Google Chrome installed
- ChromeDriver (Ensure it matches your Chrome version)
- Required Python packages:
  ```sh
  pip install selenium pandas
  ```

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/repo-name.git
   cd repo-name
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Download and place `chromedriver.exe` in the project folder.
4. Create an `emails.csv` file with an `email` column, listing the emails to check.

## Usage

Run the script with:

```sh
python checker.py
```

- The script will open a browser and check each email.
- If a CAPTCHA appears, solve it manually, then press Enter to continue.
- Results will be saved in `results.csv`.

## Example Output

```sh
test@example.com: Registered  :  Unavailable
another@example.com: Not Registered  :  Available
```

## Troubleshooting

- ❌ `'chromedriver.exe' not found?` → Ensure it's in the script directory.
- ❌ `'emails.csv' not found?` → Check the file path and format.
- ❌ `"CAPTCHA detected"` → Solve manually, then press Enter to continue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

