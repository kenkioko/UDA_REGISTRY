import time
from src.csv_std.read import ReadCSV
from src.csv_std.write import WriteCSV
from src.request.register import Register
from src.random.random_details import RandomMembers


class AutoRegister:
    skip = False
    input_file = None
    output_file = 'output_files\South C Members ' + str(time.time_ns()) + '.csv'

    def __init__(self, input_file = None, output_file = None, skip = False):
        # set input file
        if input_file:
            print(input_file)
            self.input_file = 'input_file\\' + input_file

        # set output file
        if output_file:
            print(output_file)
            self.output_file = 'output_file\\' + output_file
            
        if skip:
            print(skip)
            self.skip = skip


    def register_members(self, members, wait = None):
        registered_members = []

        # send register url
        register = Register()
        for detail in members:            
            response = register.post(detail, self.skip)

            # add member's detail
            registered_members.append(response['details'])

            # pause for seconds
            if wait > 0:
                time.sleep(wait)

        # return members
        return registered_members

    
    def run(self):
        # read csv file
        read = ReadCSV(self.input_file)
        members = read.read_file()

        # register members
        registered_members = self.register_members(members)
        
        # write output file
        write = WriteCSV(self.output_file)
        write.write_file(registered_members)


    def run_random(self):
        # read csv file
        read = ReadCSV("input_files\SOUTH C LIST.xlsx - LIST NO. 1.csv")
        members = read.read_file()

        # generate random members
        rmembers = RandomMembers(members)
        random_members = rmembers.random(1)

        # register members
        registered_members = self.register_members(random_members, 2)

        # write output file
        write = WriteCSV(self.output_file)
        write.write_file(registered_members)
