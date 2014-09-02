# Plot FEM simulation data for PhD Thesis.

import matplotlib.pyplot as pp

"""
##################################################

FEM raw data

Regime: nanopillars

meshsize: 40
amplitude: 1.0

b_min: 1
b_max: 5

b_eff: 1.37060645682
b_eff_flat: 1.66666666667
Arclength_coefficient: 1.21600672342

Periods, L: 10 5 2.5 1.42857 1 0.5 0.25 0.125 0.0625
b_fars: 0.659694 1.03236 1.21028 1.28299 1.31127 1.34634 1.3769 1.38384 1.38728
"""

def max_percent(aa,bb):
	"""Maximum of: percentage difference between a and b, or b and a."""
	a = float(aa);  b = float(bb)
	result = (max(a/b, b/a) - 1) * 100
	return result
	
def old_percent(b_far,b_eff):  # As used in PRE paper.  New function is clearer.
	""" Percentage that b_far is different from b_eff. """
	result = abs(1.0 - (b_far/b_eff)) * 100
	return result

def percent(b_far,b_eff):   # The new, clearer percentage function.
	"""Difference between measured and predicted, as % of predicted"""
	result = (b_far - b_eff)/b_eff * 100
	return result

regime = "nanopillars"

b_eff = 1.37060645682
b_eff_flat = 1.66666666667
Arclength_coefficient = 1.21600672342

Ls = (10,  5, 2.5, 1.42857, 1, 0.5, 0.25, 0.125, 0.0625)
b_fars = (0.659694, 1.03236, 1.21028, 1.28299, 1.31127, 1.34634, 1.3769, 1.38384, 1.38728)

b_effs = [ b_eff for L in Ls]
b_effs_flat = [ b_eff_flat for L in Ls]

percent_b_effs = [percent(b_far,b_eff) for b_far, b_eff in zip(b_fars, b_effs)]
percent_b_effs_flat = [percent(b_far,b_eff_flat) for b_far, b_eff_flat in zip(b_fars, b_effs_flat)]

print percent_b_effs

#############################   Plot data: b_far and b_eff
pp.scatter(Ls, b_fars)
pp.semilogx(Ls, b_effs)
pp.plot(Ls, b_effs_flat, linestyle="dashed")

pp.text(11,1.35,"$b_{\mathrm{eff}}$")
pp.text(0.2,1.7,"Naive $b_{\mathrm{eff}}$ assuming surface is flat")

pp.xlabel("$L$, in units of $b_{\mathrm{min}}$")
pp.ylabel("$b$, in units of $b_{\mathrm{min}}$")
pp.title("Comparing predicted $b_{\mathrm{eff}}$ with FEM-simulated $b_{\mathrm{far}}$")

pp.axis([0.02, 30, 0, 2])
pp.xticks([0.1,1,10],["0.1","1","10"])
##pp.yticks([0.1,1,10,100],[0.1,1,10,100])

pp.savefig("Lund_Thesis_FEM_plot.pdf",format="pdf")
pp.show()


#############################   Plot discrepancies from b_far to b_eff

pp.scatter(Ls, percent_b_effs, color="red", marker="^")
pp.semilogx(Ls, [0 for L in Ls])
pp.semilogx(Ls, [5 for L in Ls],linestyle="dashed",color="blue")
pp.semilogx(Ls, [-5 for L in Ls],linestyle="dashed",color="blue")

pp.text(12,4,"5%")
pp.text(12,-1,"0%")
pp.text(12,-6,"-5%")

#pp.text(0.1,-30,"Eg. Measured $b$ is 4.3% less \n than predicted if $L = b_{\mathrm{min}}$")
message = "Eg. Simulated $b_{\mathrm{far}}$ is 4.3% less \n than predicted $b_{\mathrm{eff}}$ at $L = b_{\mathrm{min}}$"
myarrow = {"arrowstyle":"->"}#"shrink":0.05}
pp.annotate(message, [1,-5], xytext = [0.1,-30], arrowprops=myarrow)


pp.xlabel("$L$, in units of $b_{\mathrm{min}}$")
pp.ylabel("Difference between $b_{\mathrm{far}}$ and $b_{\mathrm{eff}}$, as % of $b_{\mathrm{eff}}$")
pp.title("Comparing predicted $b_{\mathrm{eff}}$ with FEM-simulated $b_{\mathrm{far}}$")

pp.axis([0.02, 30, -60, 20])
pp.xticks([0.1,1,10],["0.1","1","10"])
##pp.yticks([0.1,1,10,100],[0.1,1,10,100])

pp.savefig("Lund_Thesis_FEM_plot_pcnt.pdf",format="pdf")
pp.show()





####################### Old Graph with both data and discrepancy
if False:
	pp.scatter(Ls, b_fars)
	pp.loglog(Ls, b_effs)
	pp.plot(Ls, b_effs_flat, linestyle="dashed")
	
	pp.scatter(Ls, percent_b_effs, color="red", marker="^")
	pp.scatter(Ls, percent_b_effs_flat, color="cyan", marker="+") 
	
	pp.xlabel("$L$, in units of $b_{\mathrm{min}}$")
	pp.ylabel("$b$, in units of $b_{\mathrm{min}}$")
	pp.title("Comparison with FEM: " + regime)
	
	pp.axis([0.02, 30, 0.2, 200])
	pp.xticks([0.1,1,10],["0.1","1","10"])
	##pp.yticks([0.1,1,10,100],[0.1,1,10,100])
	
	pp.show()
	
