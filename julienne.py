from BeautifulSoup import BeautifulSoup

class Julienne:
    def __init__(self, table):
        self.soup = BeautifulSoup(table.strip())
        self.row_list = self.soup.first("tbody").findAll("tr")

    def validate(self):
        valid_toplevel = len(self.soup.contents) == 1 and self.soup.contents[0].name == "table"
        num_columns = len(self.soup.first("thead").contents)
        rows = self.row_list
        valid_body = all([len(row) == num_columns for row in rows])
        return valid_toplevel and valid_body

    def columns(self):
        return [tag.string for tag in self.soup.findAll("th")]

    def rows(self):
        rows_sans_whitespace = [[unicode(field.string) for field in row if field != '\n'] for row in self.row_list]
        return [dict(zip(self.columns(), row)) for row in rows_sans_whitespace]

