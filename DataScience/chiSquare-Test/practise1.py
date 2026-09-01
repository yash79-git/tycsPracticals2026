import numpy as np
import scipy.stats as stats
# observed -given
observed=np.array([
    [10,20,30],
    [40,50,60]
])
print("Observed",observed)

# counting each rows
rowSum=observed.sum(axis=1)
print("Row Sum ",rowSum)

# counting each columns
colSum=observed.sum(axis=0)
print("Column Sum ",colSum)

# Total sum
totalSum=observed.sum()
print("Total Sum",totalSum)

# Expected
expected=np.outer(rowSum,colSum)/totalSum
print("Expected ",expected)

# dof
dof=(observed.shape[0]-1)*(observed.shape[1]-1)
print("dof",dof)

# chi-square
chi=(((observed-expected)**2)/expected).sum()
print("Chi-Square Value",chi)

# P value 
# Small χ²
# → Observed and Expected are relatively close

# Large χ²
# → Observed and Expected are more different

# But we still need to know:

# Is 2.8 actually "large"?

# That's where p-value comes in.
pVal=stats.chi.sf(chi,df=dof)
print("P-Value",pVal)

if(pVal > 0.05):
    print("Do no reject Null Hypothesis.")
if(pVal < 0.05):
    print("Reject Null Hypothesis.")