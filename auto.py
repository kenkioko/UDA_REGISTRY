import sys, argparse

from requests.api import options
from src.auto_register import AutoRegister

def main():
   
   # command line arguments parser
   parser = argparse.ArgumentParser(prog='UDA Auto Registry')
   parser.add_argument('-s', '--skip', action='store_true', help='skips if the member number set')
   parser.add_argument('-r', '--random', type=int, help='generate random records')
   parser.add_argument('-if', '--ifile', required=True, help='the input csv file')
   parser.add_argument('-of', '--ofile', help='the output csv file')
   
   try:
      # get optional arguments
      optv= parser.parse_args()

      # run the program
      auto_register = AutoRegister(
         input_file = optv.ifile, 
         output_file = optv.ofile, 
         skip = optv.skip,
         random_values = optv.random,
      )
      
      auto_register.run()
      print('finished')

   # catch exception
   except Exception as e:
      parser.print_help()
      
      # print exception
      print()
      print('Error: ', e)

      # exit program
      sys.exit(2)


# program start
if __name__ == "__main__":
   main()