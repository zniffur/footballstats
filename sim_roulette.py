import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

NUM_RUN = 1000
INITIAL_BANKROLL = 100
BET = 1
# RATIO_SIX_LINE = 5
# RATIO_EVENODD = 1


df = pd.DataFrame(columns=['num', 'win', 'roll'])
df['num'] = np.random.randint(0, 36, NUM_RUN)
df.loc[0, 'win'] = 0
df.loc[0, 'roll'] = INITIAL_BANKROLL


for i in range(1, df.shape[0]):
    outcome = df.loc[i, 'num']

    if df.loc[i-1, 'win'] >= 0:  # vinto la run prima, continuo con six-line
        if outcome > 0 and outcome <= 30:  # win
            df.loc[i, 'win'] = BET
            df.loc[i, 'roll'] = df.loc[i-1, 'roll'] + df.loc[i, 'win']
        else:  # loss
            df.loc[i, 'win'] = BET * -5
            df.loc[i, 'roll'] = df.loc[i-1, 'roll'] + df.loc[i, 'win']
    else:  # perso la volta prima, passo a even/odd
        last_outcome = df.loc[i-1, 'num']
        if (outcome % 2 == 0 and last_outcome % 2 == 0) or (outcome % 2 == 1 and last_outcome % 2 == 1):  # loss
            df.loc[i, 'win'] = BET * -5
            df.loc[i, 'roll'] = df.loc[i-1, 'roll'] + df.loc[i, 'win']
            continue
        if (outcome % 2 == 0 and last_outcome % 2 == 1) or (outcome % 2 == 1 and last_outcome % 2 == 0):  # win
            df.loc[i, 'win'] = BET * 5
            df.loc[i, 'roll'] = df.loc[i-1, 'roll'] + df.loc[i, 'win']
            continue


print(df.head(10))
print('------------')
print(df.tail(10)

df.roll.plot()
plt.show()
