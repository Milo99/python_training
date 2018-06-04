# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_test_add_user(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="dfgdghdghdd", middlename="sdgrsgrgsdf", lastname="sdfgsrgsfgsfd",
                        nickname="sdfefsff", title="sd", company="rtgfdgdfggfd", address="dfbdbdfgdfdf",
                        home="3455356356", mobile="24353453456345", work_phone="34563563456", fax="3453456",
                        email="sdfsrfsfs@df.fv", email2="dsfgderfgrdfg@gb.ok", email3="sdfgsdfvgsfv@dfdf.pl",
                        homepage="www.dfgdthgdhgdfhdfgh.ok", birth_year="1980", ann_year="1980",
                        address2="sdfgsrtgdfzvr", phone2="sfdvrgrrfvrf", notes="cvdszfvrgvzrvzrgvfgvzfvrfg"))
    app.session.logout()