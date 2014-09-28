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

def do_nothing():
    pass

@with_setup(simplest_html_table, do_nothing)
def test_table_validation():
    assert Julienne(TABLE).validate()



