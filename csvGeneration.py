import pandas as pd
import numpy as np

samples = 1000

#random x numbers between 0 and 100
x = np.random.uniform(0, 100, samples)

#random noise and linear relation with x-> clip values between 0 and 100
noise = np.random.normal(0, 10, samples)
y = 0.9 * x + noise
y = np.clip(y, 0, 100)

df = pd.DataFrame({'x': x, 'y': y})

print(df)
df.to_csv('dataset.csv', index=False)

print("dataset creado y guardado")