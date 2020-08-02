
import os
from os import path

content = """
Fk COVID-19.
I wanna go out.
"""

file_name = 'example.txt'

with open(file_name , 'w') as f:
    f.write(content)
    f.write('Fk this quarantine.')

new_content = """
This is new content.
It will replace the old one.
"""

with open(file_name, 'w') as f:
    f.write('I wish I could go on the trip with my friends.')

with open(file_name, 'a') as f:
    f.write('Fk Gavin Newsom.')

with open(file_name) as f:
    file_content = f.read()

print(file_content)

if not path.exists('output'):
    os.makedirs('output')

with open('output/new.txt', 'w') as f:
    f. write('Please give us a vaccine.')

html_content = """
<html>
    <a href="https://google.com">Link to Google.</a>
</html>
"""

with open('output/example.html', 'w') as f:
    f.write(html_content)

html_content2 = """
<html>
    <img src="Preston.jpg" width="500" height="600">
    </html>
"""

with open('output/example2.html', 'w') as f:
    f.write(html_content2)

