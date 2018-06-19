from model.contact import Contact

def test_modify_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_groups = app.group.get_group_list()
    app.contact.modify_first_contact(Contact(firstname="New_first_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_groups = app.group.get_group_list()
    app.contact.modify_first_contact(Contact(firstname="New_lastname_name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)