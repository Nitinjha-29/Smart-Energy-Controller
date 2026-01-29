import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# 1. Load Data
data = pd.read_csv('energy_data.csv')

# 2. Features (Input) aur Target (Output) set karna
# Input: Temperature aur Time (Hour of day)
X = data[['Temperature', 'Time_Hour']]
# Output: Energy Usage
y = data['Usage_KwH']

# 3. Model Training
model = LinearRegression()
model.fit(X, y)

# 4. Save Model
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model train ho gaya aur 'model.pkl' ke naam se save ho gaya!")