#!python

import os
import subprocess
import mpmath

regime = "nanopillars"

def callFreeFem(meshsize, amp, periods):	
	"""Call FreeFEM++ slip_vector.edp meshsize amplitude periods"""
	
	ampl = str( float(amp)*100) # Coz FreeFem fails at str -> float cast.
	
	cwd = os.getcwd()
	print "Current Working Directory: ", cwd
	FEfile = os.path.join(cwd, "slip_vector_" + regime + ".edp")
	FreeFemCommand = os.path.join(cwd, "FreeFem++-cs_10.16", "FreeFem++")
	if os.name == "nt": FreeFemCommand = "FreeFem++"  # On Windows, FreeFem++ is in PATH.
	
	# -nw  stops FreeFem++ generating graphics.
	Popenlist = [FreeFemCommand, "-nw", FEfile, meshsize, ampl, periods]
	
	print "Calling FreeFEM++"
	p = subprocess.Popen(Popenlist, stdout = subprocess.PIPE)
	
	outputstring, errorstring = p.communicate()
	outputlist = outputstring.split("\n")
	
	for line in outputlist:
		#print "LINE: ", line
		linebits = line.split()
		try:    # If line is just newline, then linebits is empty list,
			if linebits[0] == "b_far:": # so linebits[0] does not exist.
				b_far = linebits[1]    
			elif linebits[0] == "b_min:":
				b_min = linebits[1]
			elif linebits[0] == "b_max:":
				b_max = linebits[1]
			elif linebits[0] == "L:":
				L = linebits[1]
				
			if linebits[0] == "Parameter":
				print line
				
		except: pass
		
	return b_far, b_min, b_max, L
	
	
def calc_arclength_coeff(amp):
	# Arc length of sinusoidal surface from 0 to pi/2 (one quarter wave)
	# is Complete Elliptic Integral of Second Kind, E(m)
	# The argument m is m = -A^2, where A is amplitude of sinusoid.
	
	amplitude = float(amp)
	m = - amplitude*amplitude
	
	arclength = mpmath.ellipe(m)
	
	domainlength = mpmath.pi()/2
	
	arc_coeff = float(arclength/domainlength)
	
	return arc_coeff
	
def calc_b_eff(b_min, b_max, arc_coeff):
	denom = arc_coeff * ( 1/b_min + 1/ b_max )/2
	print "arc coefficient: ", arc_coeff
	b_eff = 1/ denom
	return b_eff

def calc_b_avg(b_min, b_max):
	b_avg = ( b_min + b_max )/2
	return b_avg
	

######################################################################
##################   Run the simulations.

meshsize = "40"
amp = "1.0"

b_fars = []
Llist = []

for periods in [1,2,4,7,10,20,40,80,160]:
	
	# Arguments:  meshsize, rougness amplitude, number of periods.
	results = callFreeFem(meshsize, amp, str(periods) )
	
	b_fars.append(results[0])
	Llist.append(results[-1])

######################################################################
#####################     Calculate effective slips.

b_min = results[1]
b_max = results[2]

arc_coeff = calc_arclength_coeff(amp)

b_eff = calc_b_eff(float(b_min), float(b_max), arc_coeff)
b_eff_flat = calc_b_eff(float(b_min), float(b_max), 1.0)


######################################################################
##########################     Write data to file.

Llist_str = " ".join(Llist)
b_fars_str = " ".join(b_fars)

with open("FEM_rawdata_adaptivemesh_" + regime + ".txt","a") as g:
	g.write("\n" + "#"*50 + "\n")
	g.write("FEM raw data\n\n")
	
	g.write("Regime: " + regime + "\n\n")
	
	g.write("meshsize: " + meshsize + "\n")
	g.write("amplitude: " + amp + "\n\n")
	
	g.write("b_min: " + b_min +"\n")
	g.write("b_max: " + b_max +"\n\n")
	
	g.write("b_eff: " + str(b_eff) +"\n")
	g.write("b_eff_flat: " + str(b_eff_flat) +"\n")
	g.write("Arclength_coefficient: " + str(arc_coeff) +"\n\n")
	
	g.write("Periods, L: " + Llist_str +"\n")
	g.write("b_fars: " + b_fars_str +"\n")

