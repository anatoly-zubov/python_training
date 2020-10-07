from sys import maxsize


class Group_contact:
    def __init__(self, firstname=None, lastname=None, workphone=None, homephone=None, fax=None, mobile=None,email = None,
                 email2 = None, email3 = None, all_emails_from_page = None, id=None, all_phones_from_page = None,
                 address = None):
        self.firstname = firstname
        self.lastname = lastname
        self.workphone = workphone
        self.homephone = homephone
        self.mobile = mobile
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_page = all_emails_from_page
        self.id = id
        self.all_phones_from_page = all_phones_from_page
        self.address = address

    def __repr__(self):
        return "%s:%s" % (self.id, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
