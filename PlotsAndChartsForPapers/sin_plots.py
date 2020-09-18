#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
import sys, math
def main (argv):

  plt.rcParams["savefig.format"] = 'pdf'

  #markers=['.','o','v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D','d','|','_',',']
  #markers=['v','^','<','>','1','2','3','4','8','s','p','P','*','h','H','+','x','X','D','d','|','_',',','.','o']
  markers = ['^', 'o', 's', 'p', 'x', 'd', '+', 'v', '*', '|', '<','>','1','2','3','4','8','h' ]
  #colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']
  colors=['tab:blue',  'tab:red', 'tab:green', 'tab:orange','tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan']

  plt.rc('text', usetex=True)
  plt.rc('font', family='serif')
  plt.margins(x=0,y=0)

  X = np.array ([])
  Y1 = np.array ([])
  Y2 = np.array ([])
  
  for i in range(0,1000):
    val = i/10.0
    X  = np.append (X, val)
    Y1 = np.append (Y1, math.cos (math.sqrt(val)))
    Y2 = np.append (Y2, math.sin (math.sqrt(val)))
  
  'fig = plt.figure (figsize= (10,4))

  plt.xlim ([0,100])

  plt.plot (X, Y1)
  plt.plot (X, Y2, linestyle=':')
  
  plt.title ('Comparison of two functions $\cos (\sqrt{x})$ and $\sin (\sqrt{x})$')
  plt.xlabel ('$x$ value')
  plt.ylabel ('Function value')
  plt.legend(['$\cos (\sqrt{x})$', '$\sin (\sqrt{x})$'])
  plt.savefig('FunctionCompare.pdf', bbox_inches='tight')
  
  import tikzplotlib
  out_file_name = 'function_compare.tex' 
  tikzplotlib.save(out_file_name,axis_height='8cm', axis_width='15cm', strict=True)
  
  plt.show ()


if __name__ == "__main__":
  main(sys.argv[1:])
