#pip install matplotlib (on terminal)
#act1- find student marks using bargraph and linegraph

import matplotlib.pyplot as plt

name=["Prachi","Rashi","Aryan","Ahmed"]
marks=[45,50,30,42]   

perc = []
for x in marks:
	res = (x/50)*100
	perc.append(res)

print(perc)

def lineGr():
  plt.plot(name,marks)
  plt.title("Students Marks Line Graph")
  plt.xlabel("Names")
  plt.ylabel("Marks")
  plt.show()

lineGr()

def barGr():
  plt.bar(name,perc)
  plt.title("Students' Percentage BarGraph")
  plt.xlabel("Names")
  plt.ylabel("Percentage")
  plt.show()

barGr()