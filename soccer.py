import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/E0-2019.csv')
# df.head()
# df.to_excel('datasets/E0-2019.xlsx')

df = df[['Div', 'Date', 'HomeTeam', 'AwayTeam', \
    'FTHG', 'FTAG', 'FTR', 'HTHG', \
        'HTAG', 'HTR','B365H', 'B365D', 'B365A', \
            'BbAv>2.5', 'BbAv<2.5']]

# home goals - poisson
df[df.FTHG == 0].shape[0] / 380
df[df.FTHG == 1].shape[0] / 380
df[df.FTHG == 2].shape[0] / 380
df[df.FTHG == 3].shape[0] / 380
df[df.FTHG == 4].shape[0] / 380
df[df.FTHG == 5].shape[0] / 380

# away goals - poisson
df[df.FTAG == 0].shape[0] / 380
df[df.FTAG == 1].shape[0] / 380
df[df.FTAG == 2].shape[0] / 380
df[df.FTAG == 3].shape[0] / 380
df[df.FTAG == 4].shape[0] / 380
df[df.FTAG == 5].shape[0] / 380

# come ci becca il bookmaker su esito finale
h = df[(df.FTR == 'H')].shape[0] # H
d = df[(df.FTR == 'D')].shape[0] # D
a = df[(df.FTR == 'A')].shape[0] # A

df[(df.FTR == 'H')]

tot = h+d+a
print('Tot: {}'.format(tot))
print('H: {}/{}({:.2f}%), D: {}/{}({:.2f}%), A: {}/{}({:.2f}%)'.format(h,tot,h/tot*100,d,tot,d/tot*100,a,tot,a/tot*100))

rh = df[(df.FTR == 'H') & (df.B365H < df.B365D) & (df.B365H < df.B365A)].shape[0] 
rd = df[(df.FTR == 'D') & (df.B365D < df.B365H) & (df.B365D < df.B365A)].shape[0] 
ra = df[(df.FTR == 'A') & (df.B365A < df.B365H) & (df.B365A < df.B365D)].shape[0] 

print('RH: {}/{}({:.2f}%), RD: {}/{}({:.2f}%), RA: {}/{}({:.2f}%)'.format(rh,tot,rh/tot*100,rd,tot,rd/tot*100,ra,tot,ra/tot*100))

wh = df[(df.FTR != 'H') & (df.B365H < df.B365D) & (df.B365H < df.B365A)].shape[0] 
wd = df[(df.FTR != 'D') & (df.B365D < df.B365H) & (df.B365D < df.B365A)].shape[0] 
wa = df[(df.FTR != 'A') & (df.B365A < df.B365H) & (df.B365A < df.B365D)].shape[0] 

print('WH: {}/{}({:.2f}%), WD: {}/{}({:.2f}%), WA: {}/{}({:.2f}%)'.format(wh,tot,wh/tot*100,wd,tot,wd/tot*100,wa,tot,wa/tot*100))

# come ci becca il bookmaker su o/u
df['TG'] = df.FTHG + df.FTAG

ro = df[(df.TG > 2) & (df['BbAv>2.5'] < 2)].shape[0]
ru = df[(df.TG <= 2) & (df['BbAv<2.5'] < 2)].shape[0]

print('RO: {}/{}({:.2f}%), RU: {}/{}({:.2f}%)'.format(ro,tot,ro/tot*100,ru,tot,ru/tot*100))

wo = df[(df.TG > 2) & (df['BbAv>2.5'] >= 2)].shape[0]
wu = df[(df.TG <= 2) & (df['BbAv<2.5'] >= 2)].shape[0]
print('WO: {}/{}({:.2f}%), WU: {}/{}({:.2f}%)'.format(wo,tot,wo/tot*100,wu,tot,wu/tot*100))


# statistiche delle favorite
# df[(df.B365H < 2) & (df.FTR == 'H')].shape[0]
df[(df.B365H < 2) & (df.FTR != 'H')].shape[0]
# df[(df.B365A < 2) & (df.FTR == 'A')].shape[0]
df[(df.B365A < 2) & (df.FTR != 'A')].shape[0]

# df[(df.B365A < 2) & (df.FTR != 'A')][['FTR', 'B365A']]


# analisi sulle quote e pct risultati

df2 = df[(df.B365A >= 1.5) & (df.B365A < 6.5)]
df2[df2.FTR == 'H'].shape[0]/df2.shape[0]
df2[df2.FTR == 'D'].shape[0]/df2.shape[0]
df2[df2.FTR == 'A'].shape[0]/df2.shape[0]

df2.describe()