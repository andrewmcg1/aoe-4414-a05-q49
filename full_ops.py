# script_name.py
#
# Usage: python3 eci_to_ecef.py arg1 arg2 ...
#  Text explaining script usage
# Parameters:
#  arg1: description of argument 1
#  arg2: description of argument 2
#  ...
# Output:
#  A description of the script output
#
# Written by Andrew McGrellis
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# parse script arguments
if len(sys.argv) == 3:
    c_in = float(sys.argv[1])
    n_wv = float(sys.argv[2])
else:
  print(\
   'Usage: '\
   'python3 arg1 arg2 ...'\
  )
  exit()

# write script below this line

c_out = n_wv
h_out = 1
w_out = 1

muls = n_wv * c_in
adds = n_wv * c_in
divs = 0



print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed