import re
from random import randrange


def test_firstname_on_home_page(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_page == merge_emails_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname



def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [contact.email, contact.email2, contact.email3]))))

def merge_phones_like_on_home_page(contact):
   return "\n".join(filter(lambda x: x != "",
                           map(lambda x: clear(x),
                               filter(lambda x: x is not None,
                                      [contact.homephone, contact.mobile, contact.workphone, contact.fax]))))

