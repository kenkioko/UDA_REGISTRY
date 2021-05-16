import sys, time
from src.csv_std.read import ReadCSV
from src.csv_std.write import WriteCSV
from src.request.register import Register
from src.random.random_details import RandomMembers


class AutoRegister:
    random_values = None
    skip = False
    input_file = None
    output_file = 'output_files\South C Members ' + str(time.time_ns()) + '.csv'

    def __init__(self, **kwargs):
        # set input file
        if kwargs['input_file']:
            self.input_file = 'input_files/' + kwargs['input_file']

        # set output file
        if kwargs['output_file']:
            self.output_file = 'output_files/' + kwargs['output_file']
            
        # set skip set member no
        if kwargs['skip']:
            self.skip = kwargs['skip']
            
        # set random values
        if kwargs['random_values']:
            self.random_values = kwargs['random_values']


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
        
        # run random
        if self.random_values:
            self.run_random(members)
          
        # run default with input files
        elif self.input_file:
            self.run_default(members)
            
        # run default with input files
        else:
            raise Exception("No input file or random value parsed")   


    def run_default(self, members):
        # register members
        registered_members = self.register_members(members)
        
        # write output file
        write = WriteCSV(self.output_file)
        write.write_file(registered_members)



    def run_random(self, members):
        # generate random members
        rmembers = RandomMembers(members)
        random_members = rmembers.random(self.random_values)

        # register members
        registered_members = self.register_members(random_members, 2)

        # write output file
        write = WriteCSV(self.output_file)
        write.write_file(registered_members)
