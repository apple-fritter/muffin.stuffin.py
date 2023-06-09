import argparse
import os
import sqlite3
import html

# Parse the command-line arguments
parser = argparse.ArgumentParser(description='Extract Firefox bookmarks to an HTML file.')
parser.add_argument('--path', type=str, help='path to the Firefox places.sqlite file')
args = parser.parse_args()

# If the path is not provided, prompt the user to input it
if not args.path:
    while True:
        path = input('Please enter the path to the Firefox places.sqlite file: ')
        if os.path.exists(path):
            break
        print('Error: The specified file does not exist.')

# Otherwise, use the provided path
else:
    path = args.path

# Connect to the places.sqlite file
conn = sqlite3.connect(path)

# Query the bookmarks data
query = "SELECT moz_bookmarks.title, moz_places.url FROM moz_bookmarks JOIN moz_places ON moz_bookmarks.fk = moz_places.id WHERE moz_bookmarks.type = 1 ORDER BY moz_bookmarks.position;"
bookmarks = conn.execute(query).fetchall()

# Close the connection
conn.close()

# Write the bookmarks data to an HTML file
with open('bookmarks.html', 'w') as f:
    f.write('<html>\n')
    f.write('<head><title>Bookmarks</title></head>\n')
    f.write('<body>\n')
    f.write('<h1>Bookmarks</h1>\n')
    f.write('<ul>\n')
    for bookmark in bookmarks:
        title = html.escape(bookmark[0])
        url = html.escape(bookmark[1])
        f.write(f'<li><a href="{url}">{title}</a></li>\n')
    f.write('</ul>\n')
    f.write('</body>\n')
    f.write('</html>\n')
