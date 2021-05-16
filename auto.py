import sys, getopt, argparse
from src.auto_register import AutoRegister

def main(argv):
   inputfile = ''
   outputfile = ''

   try:
      # optional arguments
      parser = argparse.ArgumentParser()
      parser.add_argument('--skip', help='skips if the member number set')

      # command line options
      opts, args = getopt.getopt(argv, "hsi:o:", [
         "ifile",
         "ofile", 
         "skip"
      ])

   except getopt.GetoptError:
      print('%(prog) [-s] -i <inputfile> -o <outputfile>')
      sys.exit(2)

   for opt, arg in opts:
      if opt == '-h':
         # help
         print('%(prog) [-s] -i <inputfile> -o <outputfile>')
         sys.exit()

      elif opt in ("-i", "--ifile"):
         # input file
         inputfile = arg

      elif opt in ("-o", "--ofile"):
         # output file
         outputfile = arg

      elif opt in ("-s", "--skip"):
         # output file
         outputfile = arg
   

   # # run the program
   # auto_register = AutoRegister(inputfile, outputfile)
   # auto_register.run()

   # finish
   print('finished')

if __name__ == "__main__":
   # main(sys.argv[1:])

   # run the program
   # auto_register = AutoRegister()
   # auto_register.run_random()
   
   
   # auto_register = AutoRegister(inputfile, outputfile)
   # auto_register.run()