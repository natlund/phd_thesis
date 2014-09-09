#!python

import os
import subprocess

def callFreeFem(filename, meshsize, bmin, bmax, periods):	
	"""Call FreeFEM++ slip_vector.edp meshsize bmin mmax periods"""
	
	cwd = os.getcwd()
	print "Current Working Directory: ", cwd
	FEfile = os.path.join(cwd, filename)
	#FreeFemCommand = os.path.join(cwd, "FreeFem++-cs_10.16", "FreeFem++")
	FreeFemCommand = "FreeFem++"  # Now in PATH on Ubuntu 13.10
	if os.name == "nt": FreeFemCommand = "FreeFem++"  # On Windows, FreeFem++ is in PATH.
	
	# -nw  stops FreeFem++ generating graphics.
	Popenlist = [FreeFemCommand, "-nw", FEfile, meshsize, bmin, bmax, periods]
	
	print "Calling FreeFEM++"
	p = subprocess.Popen(Popenlist, stdout = subprocess.PIPE)
	
	outputstring, errorstring = p.communicate()
	outputlist = outputstring.split("\n")
	
	for line in outputlist:
		#print "LINE: ", line
		linebits = line.split()
		try:    # If line is just newline, then linebits is empty list,
				# so linebits[0] does not exist.
			if linebits[0] == "P:":
				P = linebits[1]
			elif linebits[0] == "L:":
				L = linebits[1]
			elif linebits[0] == "h:":
				h = linebits[1]
			elif linebits[0] == "b_min:":
				b_min = linebits[1]
			elif linebits[0] == "b_harm:":
				b_harm =linebits[1]
			elif linebits[0] == "b_far:":
				b_far = linebits[1]    
			elif linebits[0] == "b_avg:":
				b_avg = linebits[1]
			elif linebits[0] == "b_max:":
				b_max = linebits[1]
			
			if linebits[0] == "Parameter":
				print line
			if linebits[0] == "converted":
				print line
			
		except: pass
		
	return P, L, h, b_min, b_harm, b_far, b_avg, b_max
	
	

######################################################################
##################   Run the simulations.

def runFEM_L(Write_to_File=False):   ##  Slip lengths fixed at order P, variable L

	meshsize = "40"
	bmin = "400"
	bmax = "2000"
	
	b_fars = []
	Llist = []
	
	for periods in [1,2,4,7,10,20,40,80,160]:
		
		# Arguments:  meshsize, rougness amplitude, number of periods.
		filename = "slip_vector_flat.edp"
		results = callFreeFem( filename, meshsize, bmin, bmax, str(periods) )
		P, L, h, b_min, b_harm, b_far, b_avg, b_max = results
		print results
		
		b_fars.append(b_far)
		Llist.append(L)
	
	
	######################################################################
	##########################     Write data to file.
	
	Llist_str = ", ".join(Llist)
	b_fars_str = ", ".join(b_fars)
	
	if Write_to_File:
		with open("FEM_rawdata.txt","a") as g:
			g.write("\n" + "#"*50 + "\n")
			g.write("FEM raw data\n\n")
			
			g.write("Regime: Flat surface, fixed slip lengths \n\n")
			
			g.write("meshsize: " + meshsize + "\n\n")
			
			g.write("P: " + P +"\n")
			g.write("b_min: " + b_min +"\n")
			g.write("b_max: " + b_max +"\n\n")
			g.write("b_eff: " + str(b_harm) +"\n")
			g.write("b_avg: " + str(b_avg) +"\n\n")
			
			g.write("Periods, L: = [ " + Llist_str +" ]\n")
			g.write("b_fars: =  [ " + b_fars_str +" ]\n")


########################################################################
def runFEM_b(Write_to_File=False):   ##  Period L fixed at 10% of P, variable b

	meshsize = "40"
	numperiods = "5"
	
	b_fars = []
	Llist = []
	
	b_mins = []
	b_harms = []
	b_avgs = []
	b_maxs = []
	
	for bminimum in [400,200,100,50,25,16,8,4,2,1]:
		
		bmax = str(bminimum*5)
		bmin = str(bminimum)
		
		filename = "slip_vector_flat.edp"
		results = callFreeFem(filename, meshsize, bmin, bmax, numperiods )
		P, L, h, b_min, b_harm, b_far, b_avg, b_max = results
		print results
		
		b_fars.append(b_far)
		Llist.append(L)
		
		b_mins.append(b_min)
		b_harms.append(b_harm)
		b_avgs.append(b_avg)
		b_maxs.append(b_max)
		
	Llist_str = ", ".join(Llist)
	b_fars_str = ", ".join(b_fars)
	
	b_mins_str = ", ".join(b_mins)
	b_harms_str = ", ".join(b_harms)
	b_avgs_str = ", ".join(b_avgs)
	b_maxs_str = ", ".join(b_maxs)
	
		
	if Write_to_File:
		with open("FEM_rawdata.txt","a") as g:
			g.write("\n" + "#"*50 + "\n")
			g.write("FEM raw data\n\n")
			
			g.write("Regime: Flat surface, fixed period \n\n")
			
			g.write("meshsize: " + meshsize + "\n\n")
			
			g.write("P: " + P +"\n")
			g.write("L: " + L + "\n")
			
			g.write("b_mins: = ( " + b_mins_str +" )\n")
			g.write("b_effs: = ( " + b_harms_str +" )\n\n")
			g.write("b_avgs: = ( " + b_avgs_str +" )\n")
			g.write("b_maxs: = ( " + b_maxs_str +" )\n\n")
			
			g.write("b_fars: =  ( " + b_fars_str +" )\n")

def runFEM_sine(Write_to_File=False):   ##  Slip lengths fixed at order P, variable L

	meshsize = "40"
	bmin = "400"
	bmax = "2000"
	
	b_fars = []
	Llist = []
	hlist = []
	
	for periods in [1,2,4,7,10,20,40,70,100]:
		
		# Arguments:  meshsize, rougness amplitude, number of periods.
		filename = "slip_vector_sine.edp"
		results = callFreeFem( filename, meshsize, bmin, bmax, str(periods) )
		P, L, h, b_min, b_harm, b_far, b_avg, b_max = results
		print results
		
		b_fars.append(b_far)
		Llist.append(L)
		hlist.append(h)
	
	######################################################################
	##########################     Write data to file.
	
	Llist_str = ", ".join(Llist)
	b_fars_str = ", ".join(b_fars)
	hlist_str = ", ".join(hlist)
	
	if Write_to_File:
		with open("FEM_rawdata.txt","a") as g:
			g.write("\n" + "#"*50 + "\n")
			g.write("FEM raw data\n\n")
			
			g.write("Regime: Sinusoidal surface, fixed slip lengths \n\n")
			
			g.write("meshsize: " + meshsize + "\n\n")
			
			g.write("P: " + P + "\n")
			g.write("b_min: " + b_min + "\n")
			g.write("b_max: " + b_max + "\n\n")
			g.write("b_eff: " + str(b_harm) + "\n")
			g.write("b_avg: " + str(b_avg) + "\n\n")
			
			g.write("Periods, L: = [ " + Llist_str + " ]\n")
			g.write("b_fars: =  [ " + b_fars_str + " ]\n")
			g.write("Amplitudes, h: = [ " + hlist_str + " ]\n")


runFEM_sine(True)
