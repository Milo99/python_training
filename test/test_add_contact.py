# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_test_add_user(app):
    app.contact.create(Contact(firstname="dfgdghdghdd", middlename="sdgrsgrgsdf", lastname="sdfgsrgsfgsfd",
                               nickname="sdfefsff", title="sd", company="rtgfdgdfggfd", address="dfbdbdfgdfdf",
                               home="3455356356", mobile="24353453456345", work_phone="34563563456", fax="3453456",
                               email="sdfsrfsfs@df.fv", email2="dsfgderfgrdfg@gb.ok", email3="sdfgsdfvgsfv@dfdf.pl",
                               homepage="www.dfgdthgdhgdfhdfgh.ok", ann_year="1980",
                               address2="sdfgsrtgdfzvr", phone2="sfdvrgrrfvrf", notes="cvdszfvrgvzrvzrgvfgvzfvrfg"))