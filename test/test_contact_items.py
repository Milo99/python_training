import re
from random import randrange

def test_contact_items_on_home_page(app):
    contacts_from_home_page = app.contact.get_contact_list()
    index = randrange(len(contacts_from_home_page))
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contacts_from_home_page[index].lastname == contact_from_edit_page.lastname
    assert contacts_from_home_page[index].firstname == contact_from_edit_page.firstname
    assert contacts_from_home_page[index].address == contact_from_edit_page.address
    assert contacts_from_home_page[index].all_emails_from_home_page == marge_emails_like_on_home_page(contact_from_edit_page)
    assert contacts_from_home_page[index].all_phones_from_home_page == marge_phones_like_on_home_page(contact_from_edit_page)

#def test_phone_on_contact_view_page(app):
#    contact_from_view_page = app.contact.get_contact_from_view_page(0)
#    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#    assert contact_from_view_page.home == contact_from_edit_page.home
#    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
#    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
#    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def clear(s):
    return re.sub("[() -]", "", s)

def marge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home, contact.mobile, contact.work_phone, contact.phone2]))))

def marge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))