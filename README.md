# bookmark.egress

`bookmark.egress` is a Python script that extracts bookmark data from a Firefox `places.sqlite` file and exports it as an HTML file. The HTML file retains the organizational structure of bookmarks, and includes only the title and URL information.

By using `bookmark.egress`, users can save time and manage their bookmarks more efficiently.

## Usage

To use the program, first make sure you have Python installed on your machine. Then, download the `bookmark-egress.py` file and save it in the same directory as your `places.sqlite` file.

To run the program, open a terminal in the same directory as the `firefox-egress.py` and `places.sqlite` files, and enter the following command:

`python bookmark-egress.py`


The program will automatically locate the `places.sqlite` file and export the bookmark data to an HTML file named `bookmarks.html`.

## Technical Explanation

This script uses the SQLite library in Python to connect to a Firefox `places.sqlite` database file, which contains information about bookmarks, history, and other data. SQLite is a lightweight, serverless database engine that is embedded within many applications, including Firefox.

The script then executes a SQL query to select the title and URL for each bookmark stored in the database. Specifically, it joins the `moz_bookmarks` and `moz_places` tables on the `fk` and `id` columns, respectively, and filters for bookmarks only (`WHERE moz_bookmarks.type = 1`). The results are sorted by the `position` column in `moz_bookmarks`, which specifies the order in which the bookmarks are displayed in the browser.

Once the bookmarks data is retrieved from the database, it is written to an HTML file using Python's built-in file I/O functionality. The script first writes the necessary HTML boilerplate, including a title and heading for the bookmarks page. It then iterates through each bookmark and writes an HTML list item (`<li>`) for each one, with a link to the bookmark's URL and the title enclosed in an anchor tag (`<a>`).

To ensure that the HTML is properly formatted and that any special characters are escaped, the script uses Python's `html` library to encode the bookmark title and URL values.

Overall, this script provides a simple way to extract and export bookmark data from a Firefox database file, which can be useful for backup, analysis, or custom bookmark management applications.

## Potential Use Cases

Here are three potential use cases for this program:

* Backup: Users can export their bookmarks to an HTML file for easy access outside of Firefox.
* Custom bookmark manager: Developers building their own bookmark manager can use the program to extract bookmark data and save time.
* Team bookmark management: Administrators can easily manage and distribute bookmarks to team members.

## Privacy Considerations

When using the program, there are privacy considerations to keep in mind. Users should ensure they have permission to access the Firefox `places.sqlite` file, review the bookmark data for sensitive information, and store the HTML file in a secure location with limited access. They should also keep their system and any third-party utilities used in the program up-to-date with security patches to minimize risk.
