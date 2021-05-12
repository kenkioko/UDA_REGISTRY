from src.random.random_id import RandomIdNo
from src.random.random_name import RandomName
from src.random.random_contact import RandomContact

class RandomMembers:
    input_data = None

    def __init__(self, input_data):
        self.input_data = input_data

    def random(self, total = 1):
        member_details = []
        index = 0

        while len(member_details) < total:
            # get random name
            rnames = RandomName(self.input_data)
            name = rnames.random()

            # get random Id
            rid = RandomIdNo()
            id_no = rid.random()

            # get random contaxt
            rcontact = RandomContact()
            contact = rcontact.random()          

            member = {
                'index': str(index),
                'name': name['first'] + " " + name['last'],
                'id_no': str(id_no),
                'contact': str(contact),
                'member_no': ''
            }
            
            member_details.append(member)
            index = index + 1

        # return the membera
        return member_details
