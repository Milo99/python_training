# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=first, lastname=last)
    for first in ["", random_string("FIRST", 20)]
    for last in ("", random_string("LAST", 20))
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_test_add_user(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)