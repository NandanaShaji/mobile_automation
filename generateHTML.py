file_html = open("C:\\Users\\2022413\\Downloads\\final.html","w")

full_html = '''
        <!DOCTYPE html>
        <head>
            <title>Page Title</title>
        </head>
        <body>

        <h1>This is a heading</h1>
        <p>This is a paragraph</p>

        <table>
        <tr>
            <th>Sl.No.</th>
            <th>Link Name</th>
            <th>Link href</th>
        </tr>
        <tr>
            <td>Alfreds Futterkiste</td>
            <td>Maria Anders</td>
            <td>Germany</td>
        </tr>
        <tr>
            <td>Centro comercial Moctezuma</td>
            <td>Francisco Chang</td>
            <td>Mexico</td>
        </tr>
        </table>

        <style>
        table, th, td {
        border:1px solid black;
        }
        </style>

        </body>
        </html>

'''

#write the html
file_html.write(full_html)

#saving the data into the html file
file_html.close()