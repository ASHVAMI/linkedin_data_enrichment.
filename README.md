LinkedIn Data Enrichment Project:
This guide will walk you through the process of setting up and running the LinkedIn Data Enrichment project.

Prerequisites:

1. Python 3.7 or higher:
pip (Python package installer)
Git (optional, for cloning the repository)

Step 1: Clone or Download the Project:
If downloading manually, extract the project files to a directory of your choice.

Step 2: Set Up a Virtual Environment:
python -m venv venv

Activate the virtual environment:
On Windows: venv\Scripts\activate
On macOS and Linux: source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Configure the Project
A. Database Configuration:
Open src/database/db_config.py
Update DB_PATH if you want to change the database location

B. API Configuration:
Open config/config.py
Replace "your_rapidapi_key_here" with your actual RapidAPI key for the LinkedIn Bulk Data Scraper API

Step 5: Initialize the Database
Run the following command to set up the initial database structure:
python -c "from src.database.db_operations import DatabaseOperations; DatabaseOperations()"

Step 6: Add Sample Data (Optional)
If you want to test with sample data, you can add it to the database manually or create a script to populate it. Here's an example of how you might add a sample company:
from src.database.db_operations import DatabaseOperations
db = DatabaseOperations()
db.cursor.execute("INSERT INTO companies (company_linkedin_url) VALUES (?)", 
                  ("https://www.linkedin.com/company/google",))
db.conn.commit()

Step 7: Run the Main Script
Execute the main script to start the data enrichment process:
python src/main.py

Step 8: View the Results
After the script runs, you can check the enriched_companies table in the SQLite database to see the enriched data. You can use a SQLite browser or run SQL queries to view the results.

Running Tests
To run the unit tests:
python -m unittest discover tests

Troubleshooting:
If you encounter any database-related errors, ensure that the DB_PATH in src/database/db_config.py is correct and that you have write permissions for that location.
If you get API-related errors, double-check that your API key in config/config.py is correct and that you have an active subscription to the LinkedIn Bulk Data Scraper API.
For any other issues, check the console output for error messages and refer to the project documentation or README for more information.

Remember to deactivate your virtual environment when you're done:

deactivate

This project is set up to be easily extensible. Feel free to modify the code to suit your specific needs or to add new features as required.