from BeautifulSoup import BeautifulSoup

class Julienne:
    def __init__(self, table):
        self.soup = BeautifulSoup(table.strip())

    def validate(self):
        valid_toplevel = len(self.soup.contents) == 1 and self.soup.contents[0].name == "table"
        num_columns = len(self.soup.first("thead").contents)
        rows = self.soup.first("tbody").findAll("tr")
        valid_body = all([len(row) == num_columns for row in rows])
        return valid_toplevel and valid_body
