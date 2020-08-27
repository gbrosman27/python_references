from bs4 import BeautifulSoup


html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")

# Returns the first instance of the id.
id_soup = soup.find(id="first")
print(id_soup.get_text())

# Returns all the classes.
class_soup = soup.find_all(class_="special")
print(class_soup)

# Uses the CSS to grab the data.
soup_id_css = soup.select("#first")
print(soup_id_css)

# Find_all returns a list.
data_soup = soup.find_all(attrs={"data-example": "yes"})
print(data_soup)

# Select data via CSS. Select returns a list.
d = soup.select("[data-example]")
print(d)
