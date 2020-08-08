
import os
from os import path

content = """
Joe Mama.
Bababooey.
"""

file_name = 'class10hw.txt'

with open(file_name , 'w') as f:
    f.write(content)
    f.write('Spider Cock!')

new_content = """
This is new content.
It will replace the old one.
"""

with open(file_name, 'w') as f:
    f.write('Nani!')

with open(file_name, 'a') as f:
    f.write('We stay pimping, not simping.')

with open(file_name) as f:
    file_content = f.read()

print(file_content)

if not path.exists('output'):
    os.makedirs('output')

with open('output/newclass10hw.txt', 'w') as f:
    f. write('Wakanda my bruddas.')

html_content = """
<html>
    <a href="https://twitter.com">Link to Twitter.</a>
</html>
"""    

with open('output/class10hw.html', 'w') as f:
    f.write(html_content)

html_content2 = """
<html>
    <img src="Twomad.jpg" width="500" height="600">
    </html>
"""

with open('output/class10hw2.html', 'w') as f:
    f.write(html_content2)
