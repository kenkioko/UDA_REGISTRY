import csv


class ReadCSV:
    file = None
    colums = {
        'index': 'NO',
        'name': 'NAME',
        'id_no': 'ID NO',
        'contact': 'CONTACT',
        'member_no': 'MEMBER NO',
    }

    def __init__(self, file_name):
        self.file = file_name


    def get_details(self, get_colums, row):
        details = {}
        row_keys = row.keys()
        
        for col in get_colums:
            col_name = self.colums[col]

            # get column value
            if col_name in row_keys:
                details[col] = row[col_name]
                
                # phone add '0' to begining
                if col == 'contact' and not details[col].startswith("0"):
                    details[col] = "0" + details[col]

        # return details
        return details


    def read_file(self, get_colums = None):
        with open(self.file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            all_members = []

            for row in reader:
                if not get_colums:
                    get_colums = self.colums;
                    
                # get details
                details = self.get_details(get_colums, row)

                # apend to all members
                all_members.append(details)

            # return all members
            return all_members
