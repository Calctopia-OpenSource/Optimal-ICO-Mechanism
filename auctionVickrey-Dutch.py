from random import randint
import sys

if len(sys.argv) != 4:
	print 'auctionVickrey-Dutch.py <#units> <#buyers> <max increment between bids (>2)>';
	sys.exit(2);

# parameters
n = int(sys.argv[1]); # number of units
m = int(sys.argv[2]); # number of buyers
max_t = 9; # starting high price
q = [0 for x in range(max_t+2)];
q[0] = max_t+1;

v = [[0 for x in range(m)] for y in range(n+1)]; # marginal values, note that v_i(0) = 0 for all i

for buyer in range(m):
	v[0][buyer] = 0;
	firstValue = randint(1, max_t);
	maxIncrement = randint(3, int(sys.argv[3]) );
	for unit in range(1, n+1):
		if (maxIncrement > 1):
			if (unit == 1):
				v[unit][buyer] = firstValue + maxIncrement;
			else:
				v[unit][buyer] = v[unit-1][buyer] + maxIncrement;
			maxIncrement -= 1;
		else:
			v[unit][buyer] = v[unit-1][buyer];

#arrays and variables
d = [0 for x in range(m)]; # demand
d_previous = [0 for x in range(m)]; # copy of previous demand
c = [0 for x in range(m)]; # units clinched
r = [0 for x in range(m)]; # residual demand
r_previous = [0 for x in range(m)]; # copy of previous residual demand
s = [0 for x in range(m)]; # payments to buyers
old_sum_demands = 0;
sum_demands = 0;
t_m = 0;
seqEconomyCalculated = False;

for t in range(max_t+1):

	if (t>0): # save a copy of previous demand
		d_previous = d[:];
	if (seqEconomyCalculated): # save a copy of previous residual demand
		r_previous = r[:];

	# (S1.1) calculate maximal demand for step t
	for i in range(m):
		if (v[1][i] - v[0][i] < q[t]):
			d[i] = 0;
		else:
			max_j = 0;
			for j in range(1, n):
				if (v[j][i] - v[j-1][i] >= q[t]):
					if (j > max_j):
						max_j = j;
			d[i] = max_j;

	# (S1.2) 
	old_sum_demands = sum_demands;
	sum_demands = 0;
	for i in range(m):
		sum_demands += d[i];
	if (sum_demands < n):
		for i in range(m):
			c[i] = d[i];
		q[t+1] = q[t] - 1;
		continue; # goto (S1.1)

	#(S1.3) -> we have a CE of the main economy
	if (sum_demands >= n and old_sum_demands < n):
		t_m = t; # now residual demands can be calculated
		# set c_i to be any sequential allocation
		if (not seqEconomyCalculated):
			sum_dprevious = 0;
			for i in range(m):
				c[i] = d_previous[i];
				sum_dprevious += d_previous[i];
			if (sum_dprevious < n):
				# assign additional units to bidders at random such that no bidders gets more than his maximal demand in iteration t
				toBeAssigned = n - sum_dprevious;
				everyoneClinched = False;
				while (toBeAssigned > 0):
						# first assign to bidders with no clinched units
						if (not everyoneClinched):
							for i in range(m):
								if (c[i] == 0):
									if (toBeAssigned > d[i]):
										c[i] += d[i];
										toBeAssigned -= d[i];
									else:
										c[i] += toBeAssigned;
										toBeAssigned = 0;
						everyoneClinched = True;
						# then randomly assign to the rest
						randBuyer = randint(0, m-1);
						demanded = d[randBuyer];
						if (c[randBuyer] < demanded):
							if (toBeAssigned > demanded):
								c[randBuyer] += demanded;
								toBeAssigned -= demanded;
							else:
								c[randBuyer] += toBeAssigned;
								toBeAssigned = 0;
			seqEconomyCalculated = True;

	# calculate residual demand
	if (t >= t_m):
		for i in range(m):
			sumDemands = 0;
			for j in range(m):
				if (i != j):
					sumDemands += d[j] - c[j];
			if (c[i] < sumDemands):
				r[i] = c[i];
			else:
				r[i] = sumDemands;

	#(S1.4) calculate payments
	for i in range(m):
		s[i] = s[i] + (q[t] * (r[i] - r_previous[i]));


	#(S1.5)
	allEqual = True;
	for i in range(m):
		if (r[i] != c[i]):
			allEqual = False;
			break;
	if (allEqual):
		break;
	if (q[t] == 0):
		break;

	q[t+1] = q[t] - 1;


# final allocation in c[m], final payment vector in s[m]
print "Final price"
print q[t]
print "Final allocation"
print c
print "Payment vector"
print s
