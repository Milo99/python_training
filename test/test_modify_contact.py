from model.contact import Contact

def test_modify_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New_first_name"))
    app.session.logout()

def test_modify_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(firstname="New_lastname_name"))
    app.session.logout()