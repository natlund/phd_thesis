from matplotlib import pyplot as plt
import mpmath

flat_data = """
P: 2000
b_min: 400
b_max: 2000

b_eff: 666.667
b_avg: 1200

Periods, L: = [ 1000, 500, 250, 142.857, 100, 50, 25, 12.5, 6.25 ]
b_fars: =  [ 717.626, 694.205, 681.043, 675.049, 672.57, 669.629, 668.12, 667.396, 667.032 ]
"""

if False:
	P = 2000
	Ls = ( 1000, 500, 250, 142.857, 100, 50, 25, 12.5, 6.25 )
	LonP = [ float(L)/P for L in Ls ]
	print "LonP", LonP
	Lfracs = ["1/2","1/4", "1/8", "1/14", "1/20","1/40", "1/80","1/160","1/320"]
	print "Lfracs", Lfracs
	
	bmin = 400.0
	bmax = 2000.0
	beff = 666.667
	bavg = 1200.0
	
	bfars = ( 717.626, 694.205, 681.043, 675.049, 672.57, 669.629, 668.12, 667.396, 667.032 )
	b_mins = [ bmin/bmin for x in bfars ]
	b_maxs = [ bmax/bmin for x in bfars ]
	b_effs = [ beff/bmin for x in bfars ]
	b_avgs = [ bavg/bmin for x in bfars ]
	
	b_fars = [ bfar / bmin for bfar in bfars ]
	
	wavenumbers = (1,  2, 4,   7,       10, 20,  40,   80,   160)

if False:
	plt.scatter(LonP, b_fars)
	plt.semilogx(LonP, b_effs)
	plt.plot(LonP, b_avgs, linestyle="dashed")
	plt.plot(LonP, b_mins, linestyle="dashed")
	plt.plot(LonP, b_maxs, linestyle="dashed")
	

	plt.text(0.55,1.62,"$b_{\mathrm{eff}} = < 1/b > ^{-1} $")
	plt.text(0.55,2.95,"$b_{\mathrm{eff}} = < b > $")
	plt.text(0.55,0.95,"$b_{\mathrm{min}}$")
	plt.text(0.55,4.95,"$b_{\mathrm{max}}$")
	
	plt.xlabel("Period $L$, as fraction of domain height $P$")
	plt.ylabel("$b$, in units of $b_{\mathrm{min}}$")
	plt.title("Comparing predicted $b_{\mathrm{eff}}$ with FEM-simulated $b_{\mathrm{far}}$")
	
	plt.axis([-1, 2, 0, 6])
	Lticks = [0.5,0.25,0.125,0.05,0.025,0.0125,0.00625,0.003125]
	Lticklabels = ["1/2","1/4", "1/8", "1/20","1/40", "1/80","1/160","1/320"]
	plt.xticks(Lticks,Lticklabels)
	##plt.yticks([0.1,1,10,100],[0.1,1,10,100])
	
	plt.savefig("Lund_Thesis_FEM_plot_flat_L.pdf",format="pdf")
	plt.show()
	
flat_data_b = """
P: 2000
L: 200
b_mins: = ( 400, 200, 100, 50, 25, 16, 8, 4, 2, 1 )
b_effs: = ( 666.667, 333.333, 166.667, 83.3333, 41.6667, 26.6667, 13.3333, 6.66667, 3.33333, 1.66667 )

b_avgs: = ( 1200, 600, 300, 150, 75, 48, 24, 12, 6, 3 )
b_maxs: = ( 2000, 1000, 500, 250, 125, 80, 40, 20, 10, 5 )

b_fars: =  ( 678.271, 344.532, 177.161, 92.7196, 49.5287, 33.387, 18.2165, 9.89273, 5.28744, 2.772 )
"""
if False:
	
	P = 2000.0
	L = 200.0
	
	bmins = ( 400, 200, 100, 50, 25, 16, 8, 4, 2, 1 )
	beffs = ( 666.667, 333.333, 166.667, 83.3333, 41.6667, 26.6667, 13.3333, 6.66667, 3.33333, 1.66667 )

	bavgs = ( 1200, 600, 300, 150, 75, 48, 24, 12, 6, 3 )
	bmaxs = ( 2000, 1000, 500, 250, 125, 80, 40, 20, 10, 5 )

	bfars =  ( 678.271, 344.532, 177.161, 92.7196, 49.5287, 33.387, 18.2165, 9.89273, 5.28744, 2.772 )
	
	b_maxs_xaxis = [ float(bmax)/P for bmax in bmaxs ]
	print b_maxs_xaxis
	b_fracs = [ "1", "1/2", "1/4", "1/8", "1/16", "1/25", "1/50", "1/100", "1/200", "1/400" ]
	
	b_mins = [ bmin/bmin for bmin in bmins ]
	b_effs = [ beff/bmin for beff, bmin in zip(beffs,bmins) ]
	b_fars = [ bfar/bmin for bfar, bmin in zip(bfars,bmins) ]
	b_avgs = [ bavg/bmin for bavg, bmin in zip(bavgs,bmins) ]
	b_maxs = [ bmax/bmin for bmax, bmin in zip(bmaxs,bmins) ]

if False:
	plt.scatter(b_maxs_xaxis, b_fars)
	plt.semilogx(b_maxs_xaxis, b_effs)
	plt.plot(b_maxs_xaxis, b_avgs )
	plt.plot(b_maxs_xaxis, b_mins, linestyle="dashed")
	plt.plot(b_maxs_xaxis, b_maxs, linestyle="dashed")
	
	plt.text(1.2,1.62,"$b_{\mathrm{eff}} = < 1/b > ^{-1} $")
	plt.text(1.2,2.95,"$b_{\mathrm{eff}} = < b > $")
	plt.text(1.2,0.95,"$b_{\mathrm{min}}$")
	plt.text(1.2,4.95,"$b_{\mathrm{max}}$")
	
	plt.xlabel("$b_{\mathrm{max}}$, as fraction of domain height $P$")
	plt.ylabel("$b$, in units of $b_{\mathrm{min}}$")
	plt.title("Comparing predicted $b_{\mathrm{eff}}$ with FEM-simulated $b_{\mathrm{far}}$")
	
	plt.axis([0.001, 10, 0, 6])
	xticks =      [1.0,    0.5,  0.25, 0.125, 0.04, 0.02, 0.01, 0.0025]
	xticklabels = [ "$1$", "$1/2$", "$1/4$", "$1/8$", "$1/25$", "$1/50$", "$1/100$", "$1/400$" ]	
	plt.xticks(xticks,xticklabels)
	##plt.yticks([0.1,1,10,100],[0.1,1,10,100])
	
	plt.vlines(0.1,0,3,linestyle="dotted")
	plt.text(0.11,0.45, "$b_{\mathrm{max}} = L$")
	
	plt.savefig("Lund_Thesis_FEM_plot_flat_b.pdf",format="pdf")
	plt.show()	

	
sinusoidal_data = """
P: 2000
b_min: 400
b_max: 2000

b_eff: 666.667
b_avg: 1200

Periods, L: = [ 1000, 500, 250, 142.857, 100, 50, 25, 14.2857, 10 ]
b_fars: =  [ 483.998, 517.538, 533.44, 540.137, 542.93, 547.395, 554.912, 555.499, 555.733 ]
Amplitudes, h: = [ 159.155, 79.5775, 39.7887, 22.7364, 15.9155, 7.95775, 3.97887, 2.27364, 1.59155 ]
"""

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

def calculate_beff(bmin, bmax):
	arc_coeff = calc_arclength_coeff(1.0)
	beff = calc_b_eff(bmin, bmax, arc_coeff)
	return beff

if True:
	P = 2000
	Ls = ( 1000, 500, 250, 142.857, 100, 50, 25, 14.2857, 10 )
	LonP = [ float(L)/P for L in Ls ]
	print "LonP", LonP
	print "compare", [1.0/2, 1.0/4, 1.0/8, 1.0/14, 1.0/20, 1.0/40, 1.0/80, 1.0/140, 1.0/200 ]
	Lfracs = ["1/2","1/4", "1/8", "1/14", "1/20","1/40", "1/80","1/140","1/200"]
	print "Lfracs", Lfracs
	
	bmin = 400.0
	bmax = 2000.0
	beff_flat = 666.667
	bavg = 1200.0
	beff = calculate_beff(bmin,bmax)
	print "Raw beff: ", beff
	b_eff = beff/bmin
	
	bfars = ( 483.998, 517.538, 533.44, 540.137, 542.93, 547.395, 554.912, 555.499, 555.733 )
	b_mins = [ bmin/bmin for x in bfars ]
	b_maxs = [ bmax/bmin for x in bfars ]
	b_effs_flat = [ beff_flat/bmin for x in bfars ]
	b_effs = [ beff/bmin for x in bfars ] 
	b_avgs = [ bavg/bmin for x in bfars ]
	
	b_fars = [ bfar / bmin for bfar in bfars ]

	hs = (159.155, 79.5775, 39.7887, 22.7364, 15.9155, 7.95775, 3.97887, 2.27364, 1.59155 )
	corr_b_fars = [ (bfar + h)/bmin for bfar, h in zip(bfars, hs) ]

if False:
	plt.scatter(LonP, b_fars)
	plt.semilogx(LonP, b_effs)
	plt.plot(LonP, b_effs_flat, linestyle="dashed")
	plt.plot(LonP, b_avgs, linestyle="dashed")
	plt.plot(LonP, b_mins, linestyle="dashed")
	#plt.scatter(LonP, corr_b_fars, color="black", marker="+")
	
	plt.text(0.55,1.35,"$b_{\mathrm{eff}}$") # = < \sqrt{1 + |h'|^2}/b > ^{-1} $")
	plt.text(0.55,2.98,"$ < b > $")
	plt.text(0.55,1.65,"$b_{\mathrm{eff (flat)}}$")
	plt.text(0.55,0.98,"$b_{\mathrm{min}}$")
	#plt.text(0.55,4.95,"$b_{\mathrm{max}}$")
	
	plt.xlabel("Period $L$, as fraction of domain height $P$")
	plt.ylabel("$b$, in units of $b_{\mathrm{min}}$")
	plt.title("Comparing predicted $b_{\mathrm{eff}}$ with FEM-simulated $b_{\mathrm{far}}$")
	
	plt.axis([0.002, 2, 0, 3.5])
	Lticks = [0.5,0.25,0.125,0.05,0.025,0.0125,0.005]
	Lticklabels = ["$1/2$","$1/4$", "$1/8$","$1/20$","$1/40$","$1/80$","$1/200$"]
	plt.xticks(Lticks,Lticklabels)
	##plt.yticks([0.1,1,10,100],[0.1,1,10,100])
	
	plt.savefig("Lund_Thesis_FEM_plot_sine_1.pdf",format="pdf")
	plt.show()
	
	
def percent(b_far,b_eff):   # The new, clearer percentage function.
	"""Difference between measured and predicted, as % of predicted"""
	result = (b_far - b_eff)/b_eff * 100
	return result
	
if True:
	percent_b_effs = [ percent(bfar, beff) for bfar in bfars ]
	print percent_b_effs
	percent_b_effs_corr = [ percent(bfar_corr, b_eff) for bfar_corr in corr_b_fars ]
	
	plt.scatter(LonP, percent_b_effs, color="red", marker="^")
	plt.semilogx(LonP, [0 for L in LonP])
	plt.semilogx(LonP, [5 for L in LonP],linestyle="dashed",color="blue")
	plt.semilogx(LonP, [-5 for L in LonP],linestyle="dashed",color="blue")
	plt.scatter(LonP, percent_b_effs_corr, color="black", marker="+")
	
	plt.text(0.55,4,"5%")
	plt.text(0.55,-1,"0%")
	plt.text(0.55,-6,"-5%")
	
	#plt.text(0.1,-30,"Eg. Measured $b$ is 4.3% less \n than predicted if $L = b_{\mathrm{min}}$")
	message = "Eg. Simulated $b_{\mathrm{far}}$ is 5.6% less than \n predicted $b_{\mathrm{eff}}$ when $L$ is $1/4$ domain height."
	myarrow = {"arrowstyle":"->"}#"shrink":0.05}
	plt.annotate(message, [0.25,-6], xytext = [0.01,-20], arrowprops=myarrow)

	
	plt.xlabel("Period $L$, as fraction of domain height $P$")
	#plt.ylabel("$b$, in units of $b_{\mathrm{min}}$")
	plt.ylabel("Difference between $b_{\mathrm{far}}$ and $b_{\mathrm{eff}}$, as % of $b_{\mathrm{eff}}$")
	plt.title("Comparing predicted $b_{\mathrm{eff}}$ with FEM-simulated $b_{\mathrm{far}}$")
	
	plt.axis([0.003, 1, -30, 20])
	Lticks = [0.5,0.25,0.125,0.05,0.025,0.0125,0.005]
	Lticklabels = ["$1/2$","$1/4$", "$1/8$","$1/20$","$1/40$","$1/80$","$1/200$"]
	plt.xticks(Lticks,Lticklabels)
	##plt.yticks([0.1,1,10,100],[0.1,1,10,100])
	
	#plt.savefig("Lund_Thesis_FEM_plot_sine_pcnt.pdf",format="pdf")
	#plt.savefig("Lund_Thesis_FEM_plot_sine_pcnt_corr.pdf",format="pdf")
	
	plt.show()
