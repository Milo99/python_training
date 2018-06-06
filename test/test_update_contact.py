from model.contact import Contact

def test_update_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.update_first_contact(Contact(firstname="Updated", middlename="", lastname="Updated",
                               nickname="", title="", company="", address="",
                               home="", mobile="", work_phone="", fax="",
                               email="", email2="", email3="",
                               homepage="", birth_year="", ann_year="",
                               address2="", phone2="", notes=""))
    app.session.logout()