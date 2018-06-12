from model.contact import Contact

def test_modify_firstname(app):
    app.contact.modify_first_contact(Contact(firstname="New_first_name"))

def test_modify_lastname(app):
    app.contact.modify_first_contact(Contact(firstname="New_lastname_name"))