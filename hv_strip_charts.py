import sys
import csv
from ROOT import *
import argparse
import os
import numpy as np
import math
import operator
import inspect


parser = argparse.ArgumentParser(description = 'HV current plots')
parser.add_argument('-file', '--input_file', nargs=1, help = "give file path to .txt file for Current Strip Chart", type = str, required =False)
parser.add_argument('-plot', '--plotGEM', default = None, nargs ='*', help = "speficy which GEM to plot.", action = "store", type = str, required = False)
parser.add_argument('-s', '--save', default = False, action = "store_true", help = "Choose to save plot or not", required = False)

def retrieve_name(var):
    callers_local_vars = inspect.currentframe().f_back.f_locals.items()
    return [var_name for var_name, var_val in callers_local_vars if var_val is var]


args = parser.parse_args()

save = args.save
plotGEM = args.plotGEM

input_file = args.input_file

if not input_file:
	file = open('/Users/john/UVa/GeN-RP/gen-rp_inline_all_slots.txt')
else: 
	file = open(args.input_file[0])

print "Input file is:", file

csvreader = csv.reader(file)


header = []
header = next(csvreader)

rows = []
for row in csvreader:
	rows.append(row)

time = []

##Inline layers
inline1_G0 = []
inline1_G1 = []
inline1_G2 = []
inline1_G3 = []
inline2_G0 = []
inline2_G1 = []
inline2_G2 = []
inline2_G3 = []
inline3_G0 = []
inline3_G1 = []
inline3_G2 = []
inline3_G3 = []
inline4_G0 = []
inline4_G1 = []
inline4_G2 = []
inline4_G3 = []
inline5_G0 = []
inline5_G1 = []
inline5_G2 = []
inline5_G3 = []
inline6_G0 = []
inline6_G1 = []
inline6_G2 = []
inline6_G3 = []


##Side Layers
polR0_G0 = []
polR0_G1 = []
polR0_G2 = []
polR0_G3 = []
polR1_G0 = []
polR1_G1 = []
polR1_G2 = []
polR1_G3 = []

polL0_G0 = []
polL0_G1 = []
polL0_G2 = []
polL0_G3 = []
polL1_G0 = []
polL1_G1 = []
polL1_G2 = []
polL1_G3 = []

#GRAPHS
#TC_inline1_G0 = TCanvas("Inline Layer 1 - G0", "Current vs Time")
TG_inline1_G0 = TGraph()
TG_inline1_G1 = TGraph()
TG_inline1_G2 = TGraph()
TG_inline1_G3 = TGraph()
TG_inline2_G0 = TGraph()
TG_inline2_G1 = TGraph()
TG_inline2_G2 = TGraph()
TG_inline2_G3 = TGraph()
TG_inline3_G0 = TGraph()
TG_inline3_G1 = TGraph()
TG_inline3_G2 = TGraph()
TG_inline3_G3 = TGraph()
TG_inline4_G0 = TGraph()
TG_inline4_G1 = TGraph()
TG_inline4_G2 = TGraph()
TG_inline4_G3 = TGraph()
TG_inline5_G0 = TGraph()
TG_inline5_G1 = TGraph()
TG_inline5_G2 = TGraph()
TG_inline5_G3 = TGraph()
TG_inline6_G0 = TGraph()
TG_inline6_G1 = TGraph()
TG_inline6_G2 = TGraph()
TG_inline6_G3 = TGraph()

TG_polR0_G0 = TGraph()
TG_polR0_G1 = TGraph()
TG_polR0_G2 = TGraph()
TG_polR0_G3 = TGraph()
TG_polR1_G0 = TGraph()
TG_polR1_G1 = TGraph()
TG_polR1_G2 = TGraph()
TG_polR1_G3 = TGraph()



#for t in range(0,len(rows),1):
	#print row[0]

for t in range(len(rows)):
	time.append(float(rows[t][0]))
	##Inline layers
	inline1_G0.append(100000000*float(rows[t][2]))
	inline1_G1.append(100000000*float(rows[t][4]))
	inline1_G2.append(100000000*float(rows[t][6]))
	inline1_G3.append(100000000*float(rows[t][8]))
	inline2_G0.append(100000000*float(rows[t][10]))
	inline2_G1.append(100000000*float(rows[t][12]))
	inline2_G2.append(100000000*float(rows[t][14]))
	inline2_G3.append(100000000*float(rows[t][16]))
	inline3_G0.append(100000000*float(rows[t][18]))
	inline3_G1.append(100000000*float(rows[t][20]))
	inline3_G2.append(100000000*float(rows[t][22]))
	inline3_G3.append(100000000*float(rows[t][24]))
	inline4_G0.append(100000000*float(rows[t][26]))
	inline4_G1.append(100000000*float(rows[t][28]))
	inline4_G2.append(100000000*float(rows[t][30]))
	inline4_G3.append(100000000*float(rows[t][32]))
	inline5_G0.append(100000000*float(rows[t][34]))
	inline5_G1.append(100000000*float(rows[t][36]))
	inline5_G2.append(100000000*float(rows[t][38]))
	inline5_G3.append(100000000*float(rows[t][40]))
	inline6_G0.append(100000000*float(rows[t][42]))
	inline6_G1.append(100000000*float(rows[t][44]))
	inline6_G2.append(100000000*float(rows[t][46]))
	inline6_G3.append(100000000*float(rows[t][48]))

	##Side Layers
	polR0_G0.append(100000000*float(rows[t][50]))
	polR0_G1.append(100000000*float(rows[t][52]))
	polR0_G2.append(100000000*float(rows[t][54]))
	polR0_G3.append(100000000*float(rows[t][56]))
	polR1_G0.append(100000000*float(rows[t][58]))
	polR1_G1.append(100000000*float(rows[t][60]))
	polR1_G2.append(100000000*float(rows[t][62]))
	polR1_G3.append(100000000*float(rows[t][64]))

	#PolL0_G0
	#PolL0_G1
	#PolL0_G2
	#PolL0_G3
	#PolL1_G0
	#PolL1_G1
	#PolL1_G2
	#PolL1_G3


#Set Graph Points
for i in range(len(rows)):
	TG_inline1_G0.SetPoint(i, time[i], inline1_G0[i])
	TG_inline1_G1.SetPoint(i, time[i], inline1_G1[i])
	TG_inline1_G2.SetPoint(i, time[i], inline1_G2[i])
	TG_inline1_G3.SetPoint(i, time[i], inline1_G3[i])
	TG_inline2_G0.SetPoint(i, time[i], inline2_G0[i])
	TG_inline2_G1.SetPoint(i, time[i], inline2_G1[i])
	TG_inline2_G2.SetPoint(i, time[i], inline2_G2[i])
	TG_inline2_G3.SetPoint(i, time[i], inline2_G3[i])
	TG_inline3_G0.SetPoint(i, time[i], inline3_G0[i])
	TG_inline3_G1.SetPoint(i, time[i], inline3_G1[i])
	TG_inline3_G2.SetPoint(i, time[i], inline3_G2[i])
	TG_inline3_G3.SetPoint(i, time[i], inline3_G3[i])
	TG_inline4_G0.SetPoint(i, time[i], inline4_G0[i])
	TG_inline4_G1.SetPoint(i, time[i], inline4_G1[i])
	TG_inline4_G2.SetPoint(i, time[i], inline4_G2[i])
	TG_inline4_G3.SetPoint(i, time[i], inline4_G3[i])
	TG_inline5_G0.SetPoint(i, time[i], inline5_G0[i])
	TG_inline5_G1.SetPoint(i, time[i], inline5_G1[i])
	TG_inline5_G2.SetPoint(i, time[i], inline5_G2[i])
	TG_inline5_G3.SetPoint(i, time[i], inline5_G3[i])
	TG_inline6_G0.SetPoint(i, time[i], inline6_G0[i])
	TG_inline6_G1.SetPoint(i, time[i], inline6_G1[i])
	TG_inline6_G2.SetPoint(i, time[i], inline6_G2[i])
	TG_inline6_G3.SetPoint(i, time[i], inline6_G3[i])

	TG_polR0_G0.SetPoint(i, time[i], polR0_G0[i])
	TG_polR0_G1.SetPoint(i, time[i], polR0_G1[i])
	TG_polR0_G2.SetPoint(i, time[i], polR0_G2[i])
	TG_polR0_G3.SetPoint(i, time[i], polR0_G3[i])
	TG_polR1_G0.SetPoint(i, time[i], polR1_G0[i])
	TG_polR1_G1.SetPoint(i, time[i], polR1_G1[i])
	TG_polR1_G2.SetPoint(i, time[i], polR1_G2[i])
	TG_polR1_G3.SetPoint(i, time[i], polR1_G3[i])

	
#STORE ALL TGs
all_gems = [inline1_G0, inline1_G1, inline1_G2, inline1_G3,
			inline2_G0, inline2_G1, inline2_G2, inline2_G3,
			inline3_G0, inline3_G1, inline3_G2, inline3_G3,
			inline4_G0, inline4_G1, inline4_G2, inline4_G3,
			inline5_G0, inline5_G1, inline5_G2, inline5_G3,
			inline6_G0, inline6_G1, inline6_G2, inline6_G3,
			polR0_G0, polR0_G1, polR0_G2, polR0_G3,
			polR1_G0, polR1_G1, polR1_G2, polR1_G3
			]

all_gems_names = []
for i in range(len(all_gems)):
	all_gems_names.append(retrieve_name(all_gems[i])[0])

all_TGs = [	TG_inline1_G0, TG_inline1_G1, TG_inline1_G2, TG_inline1_G3,
			TG_inline2_G0, TG_inline2_G1, TG_inline2_G2, TG_inline2_G3,
			TG_inline3_G0, TG_inline3_G1, TG_inline3_G2, TG_inline3_G3,
			TG_inline4_G0, TG_inline4_G1, TG_inline4_G2, TG_inline4_G3,
			TG_inline5_G0, TG_inline5_G1, TG_inline5_G2, TG_inline5_G3,
			TG_inline6_G0, TG_inline6_G1, TG_inline6_G2, TG_inline6_G3,
			TG_polR0_G0, TG_polR0_G1, TG_polR0_G2, TG_polR0_G3,
			TG_polR1_G0, TG_polR1_G1, TG_polR1_G2, TG_polR1_G3
			]


name = []
cnt = 0
#PLOTTING

if('all' in plotGEM):
	for tg in range(len(all_TGs)):
		name.append("TC_"+retrieve_name(all_gems[tg])[0])
		name[tg] = TCanvas("", retrieve_name(all_gems[tg])[0])
		min_val = min(all_gems[tg])
		all_TGs[tg].Draw()
		#all_TGs[tg].GetYaxis().SetRangeUser(min_val-0.25, 0)
		name[tg].Update()
	


else:
 	for plot in plotGEM:
 		name.append("TC_"+plot)
		name[cnt] = TCanvas("", plot)
		
		all_TGs[all_gems_names.index(plot)].Draw()
		name[cnt].Update()
		
		cnt += 1
		



		

#TC_inline1_G0.Draw()
#TG_inline1_G0.Draw()
#all_TGs[0].Draw()
#TC_inline1_G0.Update()



raw_input("\nPress Enter to continue...")

