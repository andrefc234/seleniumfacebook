

# Facebook Login Bot with Selenium

This project demonstrates how to automate the login process on Facebook using Selenium, a powerful web automation tool.

## Prerequisites

- Python 3 installed on your system.
- Chrome WebDriver installed and available in your system PATH.

## Setup

1. Clone the repository to your local machine:

   ```bash
   git clone [<repository_url>](https://github.com/andrefc234/seleniumfacebook)
   ```

2. Navigate to the project directory:

   ```bash
   cd seleniumfacebook
   ```

3. Create a virtual environment named "venv":

   ```bash
   python3 -m venv venv
   ```

4. Activate the virtual environment:

   - For macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - For Windows:

     ```bash
     venv\Scripts\activate
     ```

5. Install Selenium within the virtual environment:

   ```bash
   pip install selenium
   ```

6. Download the Chrome WebDriver and ensure it's available in your system PATH. You can download it from the [ChromeDriver website](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Usage

To run the Facebook login bot script, execute the following command:

```bash
python app.py
```

Replace `app.py` with the name of the Python script containing the Selenium code.

The script will open Facebook's login page, enter the provided credentials, and attempt to log in. Make sure to replace the placeholder credentials with your actual Facebook email and password in the script.

## Troubleshooting

- If you encounter any issues with the Chrome WebDriver, ensure that you have the correct version compatible with your Chrome browser.
- Make sure that your system has the necessary permissions to execute scripts and access the Chrome WebDriver.

---

Feel free to customize the README.md according to your specific project details and requirements. This template provides a basic structure to help users set up the environment, install dependencies, and run the provided Python script.
