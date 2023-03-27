import sqlite3
import html

# Connect to the places.sqlite file
conn = sqlite3.connect('places.sqlite')

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
