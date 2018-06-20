# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_test_add_user(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="fn", lastname="ln"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_test_add_user2(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="fn2", lastname="ln2"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_test_add_user3(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="fn3", lastname="ln3"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

def test_test_add_user4(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="fn4", lastname="ln4"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)