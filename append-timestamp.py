import datetime
import sys
import shutil
print ("hola")
if len(sys.argv) != 2:
    print("Error, You should specify an input file")
    exit(-1)

input = sys.argv[1]
output = "output.txt"

shutil.copyfile(input, output)

with open(output, "a") as outputfile:
    cur_timestamp = str(datetime.datetime.now())
    outputfile.write("\n"+cur_timestamp)


