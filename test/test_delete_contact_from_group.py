from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_delete_random_contact_from_random_group(app):

    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db.get_contacts_in_group(group)) == 0:
        if len(db.get_contacts_not_in_group(group)) == 0:
            app.contact.create(Contact(firstname="test"))
        contact = random.choice(db.get_contacts_not_in_group(group))
        app.contact.add_to_group(contact, group)
    contacts = db.get_contacts_in_group(group)
    contact2 = random.choice(contacts)
    app.contact.delete_from_group(contact2, group)
    new_contacts = db.get_contacts_in_group(group)
    assert len(contacts) - 1 == len(new_contacts)
