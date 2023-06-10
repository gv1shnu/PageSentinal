import os.path
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime
import requests
from urllib.parse import urlparse
import difflib


def is_valid_url(url):
    """
    Checks if a URL is valid.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    """
    try:
        _result = urlparse(url)
        return all([_result.scheme, _result.netloc])
    except ValueError:
        return False


def calculate_diff(prev_state, curr_state):
    """
    Calculates the differences between the previous state and the current state.

    Args:
        prev_state (str): The previous webpage state.
        curr_state (str): The current webpage state.

    Returns:
        str: The calculated differences between the states.
    """
    previous_lines = prev_state.splitlines(keepends=True)
    current_lines = curr_state.splitlines(keepends=True)

    _diff = difflib.unified_diff(previous_lines, current_lines)
    return ''.join(_diff)


if __name__ == '__main__':
    print("Welcome to PageSentinal")

    site = input("Enter URL: ")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.124 Safari/537.36'
    }
    if is_valid_url(site):
        try:
            response = requests.get(site, headers=headers).content
            soup = BeautifulSoup(response, 'html.parser')
            if not os.path.exists('db'):
                os.mkdir('db')
            with sqlite3.connect('db/website_states.db') as conn:
                cursor = conn.cursor()

                table_name = 'website_table_' + ''.join(c if c.isalnum() else '_' for c in site)
                cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
                table_exists = cursor.fetchone()

                if table_exists:
                    # Table already exists, proceed with checking and saving state
                    cursor.execute(f'SELECT state FROM {table_name} ORDER BY id DESC LIMIT 1')
                    result = cursor.fetchone()

                    if result:
                        # Website state exists, compare with the current state
                        previous_state = result[0]
                        if previous_state == str(soup):
                            print("Website state unchanged.")
                        else:
                            print("Website state has changed.")
                            diff = calculate_diff(previous_state, str(soup))
                            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                            cursor.execute(f'INSERT INTO {table_name} (state, timestamp) VALUES (?, ?)', (diff, timestamp))
                            print("New state saved.")

                else:
                    # Table does not exist, create the table and save the current state
                    cursor.execute(f'''
                            CREATE TABLE {table_name} (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                state TEXT,
                                timestamp DATETIME
                            )
                        ''')

                    # Save the current state
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute(f'INSERT INTO {table_name} (state, timestamp) VALUES (?, ?)', (str(soup), timestamp))
                    print("Table created. Saving current state.")

                # Commit the changes and close the connection
                conn.commit()

        except requests.exceptions.RequestException as e:
            print("Error occurred during the HTTP request:", str(e))

        except sqlite3.Error as e:
            print("SQLite error occurred:", str(e))

        except Exception as e:
            print("An error occurred:", str(e))

    else:
        print("Invalid URL")

