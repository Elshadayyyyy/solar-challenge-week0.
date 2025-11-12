import pandas as pd

def load_data():
    benin = pd.read_csv('data/benin-malanville.csv')
    sierra1 = pd.read_csv('data/sierraleone_clean.csv')
    sierra2 = pd.read_csv('data/sierraleone-bumbuna.csv')
    togo = pd.read_csv('data/togo-dapaong_qc.csv')

 
    sierra = pd.concat([sierra1, sierra2], ignore_index=True)

    
    benin['Country'] = 'Benin'
    sierra['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'

    df = pd.concat([benin, sierra, togo], ignore_index=True)
    return df

def get_summary(df):
    return df.groupby('Country')[['GHI','DNI','DHI']].agg(['mean','median','std']).round(2)
