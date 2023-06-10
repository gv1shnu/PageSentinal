# PageSentinal

Track and monitor changes on your favorite websites, ensuring you stay up-to-date with the latest changes.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Limitations](#limitations)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Webpage Monitoring**: Monitors changes in the state of a webpage by comparing the current state with the previous state.
- **Incremental Updates**: Stores only the differences or changes in the webpage state instead of the complete content, reducing storage requirements.
- **SQLite Database**: Utilizes an SQLite database to store and retrieve webpage states and changes.
- **Parameterized Queries**: Uses parameterized queries to prevent SQL injection vulnerabilities when interacting with the database.

## Installation

Follow these steps to set up and run the Page Sentinal application:

1. Clone the repository:
	
   		git clone https://github.com/gv1shnu/PageSentinal.git


2. Navigate to the project directory:
	
   		cd PageSentinal


3. To run this project, make sure you have Python 3.11 and pip installed on your system. Install the required dependencies:
	
		pip install -r requirements.txt

## Usage

To use the PageSentinal application:

- Run the script by executing the following command in the project directory:

        python main.py

- Enter the URL of the webpage you want to monitor when prompted.
- The application will fetch the webpage content, compare it with the previous state (if any), and display whether the state has changed.
- If there are changes, the application will show the differences between the previous and current states.
- The application will store the current state and changes in an SQLite database.

## Technologies Used

- Python: The programming language used to develop the application.
- SQLite: The database system used to store and retrieve webpage states and changes.
- BeautifulSoup: A Python library used for web scraping and parsing HTML content.
- Requests: A Python library used for making HTTP requests to fetch webpage content.
- Difflib: A Python library used for calculating differences between strings.

## Limitations

- The application currently supports tracking changes in the HTML content of webpages only.
- Monitoring process is triggered manually by running the script. It does not provide automated scheduling or continuous monitoring.
- It does not handle complex webpages with dynamic content that requires JavaScript execution.
- It relies on the assumption that the webpage structure remains consistent between visits. Changes in the webpage structure may affect the accuracy of change detection.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request. Make sure to follow the existing coding style and conventions.

## License

This project is licensed under the [MIT License](LICENSE).
