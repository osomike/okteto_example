import pandas as pd
import numpy as np
import os
import pydevd_pycharm

print('\n\n\n\nHola! We are about to execute your code inside {name} environment...\n\n\n\n'.format(
    name=os.environ.get('dev_environment', 'Local')))

print('Connecting to debugger...')
#pydevd_pycharm.settrace('localhost', port=3500, stdoutToServer=True, stderrToServer=True)
print('Debugger connected!\n')

# Create data
a = np.random.rand(2*10**4, 1*10**1)

df = pd.DataFrame(
        data=a,
        columns=['col_{i}'.format(i=_) for _ in range(a.shape[1])]
    )

# dummy data transformations
df = df.round(decimals=2)
df = df * 32 + 1

print(df)