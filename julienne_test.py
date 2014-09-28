from julienne import Julienne
from nose import with_setup

def simplest_html_table():
    global TABLE 
    TABLE = """
    <table>
        <thead>
            <tr>
                <th>Function</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>validate()</td>
            </tr>
        </tbody>
    </table>
    """

@with_setup(simplest_html_table)
def test_table_validation():
    assert Julienne(TABLE).validate()

def test_column_enumeration():
    assert Julienne(TABLE).columns() == ['Function']

def test_row_enumeration():
    assert Julienne(TABLE).rows() == [{ 'Function':'validate()' }]

def test_julienne_selection():
    assert Julienne(TABLE).select(columns=['Function']) == [{ 'Function':'validate()' }]
    assert Julienne(TABLE).select(columns=[]) == [{}]

