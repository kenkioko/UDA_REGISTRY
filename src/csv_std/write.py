import csv


class WriteCSV:
    file = None

    def __init__(self, file_name):
        self.file = file_name

    def write_file(self, data):
        csv.list_dialects()
        fieldnames = [
            'NO',
            'NAME',
            'ID',
            'CONTACT',
            'MEMBER NO'
        ]

        with open(self.file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for row in data:
                # write rows            
                writer.writerow({
                    'NO': row['index'], 
                    'NAME': row['name'],
                    'ID': row['id_no'],
                    'CONTACT': row['contact'],
                    'MEMBER NO': row['member_no']
                })             
              
            # print success
            print()
            print('File successfuly written. Filename: ' +self.file)
