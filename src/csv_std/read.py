import csv


class ReadCSV:
    file = None

    def __init__(self, file_name):
        self.file = file_name

    def read_file(self):
        with open(self.file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            all_members = []

            for row in reader:
                index = row['NO']
                name = row['NAME']
                id_no = row['ID NO']
                contact = row['CONTACT']
                member_no = row['MEMBER NO']

                # phone add '0' to begining
                if not contact.startswith("0"):
                    contact = "0" + contact
            
                # make Member details
                details = {
                    'index': index,
                    'name': name,
                    'id_no': id_no,
                    'contact': contact,
                    'member_no': member_no
                }

                # apend to all members
                all_members.append(details)

            # return all members
            return all_members
