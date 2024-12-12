import pandas as pd
import matplotlib.pyplot as plt

hpi_data = pd.read_csv(r"C:\Users\behna\Desktop\CSUSHPISA.csv")
interest_data = pd.read_csv(r"C:\Users\behna\Desktop\DFF.csv")

hpi_data.rename(columns={'DATE': 'date', 'CSUSHPISA': 'value_hpi'}, inplace=True)
interest_data.rename(columns={'DATE': 'date', 'DFF': 'value_interest'}, inplace=True)

hpi_data['date'] = pd.to_datetime(hpi_data['date'])
interest_data['date'] = pd.to_datetime(interest_data['date'])

combined_data = pd.merge(hpi_data, interest_data, on='date', how='outer')

combined_data.dropna(subset=['value_hpi'], inplace=True)

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(combined_data['date'], combined_data['value_hpi'], label='House Price Index', color='blue')
plt.title('House Price Index (HPI)')
plt.xlabel('Date')
plt.ylabel('HPI')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(combined_data['date'], combined_data['value_interest'], label='Interest Rate', color='orange')
plt.title('Bank Interest Rate')
plt.xlabel('Date')
plt.ylabel('Interest Rate')
plt.legend()

plt.tight_layout()
plt.show()