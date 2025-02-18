import pickle
import pandas as pd
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing

assets = Path(__file__).parent / 'assets'
data_path = assets / 'training_data.csv'
model_path = assets / 'model__v1.pkl'

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df.to_csv(data_path, index=False)

features = [
    'AveRooms',
    'AveBedrms'
]

model = LinearRegression()
model.fit(df[features], df.target)

with model_path.open('wb') as file:

    pickle.dump(model, file)

