import pandas as pd
table=["RCB","CSK","SRH","MI","PK"]
played=[3,3,3,3,3]
won=[3,2,1,3,2]
points=[x*2 for x in won ]
run_rate=[1000.1,500.5,-100,600,500]
a={"team":[x for x in table],"played":[x for x in played],"won":[x for x in won],"points":[x for x in points],"run_rate":[x for x in run_rate]}
print(pd.DataFrame(a,index=[x for x in range(1,len(table)+1)]))