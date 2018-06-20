# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_test_add_user(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="fn", lastname="ln")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_mas) == sorted(new_contacts, key=Contact.id_or_mas)