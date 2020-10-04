from sys import maxsize


class Group_contact:
    def __init__(self, firstname=None, lastname=None, workphone=None, homephone=None, fax=None, mobile=None,
                 email=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.workphone = workphone
        self.homephone = homephone
        self.mobile = mobile
        self.fax = fax
        self.email = email
        self.id = id

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
