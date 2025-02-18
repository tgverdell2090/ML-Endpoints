from fasthtml.common import *
from pathlib import Path
import pickle
import pandas as pd

def load_model(version):
    assets = Path(__file__).parent / 'assets'
    model_path = assets / f'model__{version}.pkl'
    with model_path.open('rb') as file:
        model = pickle.load(file)
    
    return model

app = FastHTML()

# Define a GET route that 
# receives a model version number
# and input variables for prediction
@app.route("/model/{version}")
def get(version:str, AveRooms:int, AveBedrms:int):
    # Load model
    model = load_model(version)
    # Structure prediction data
    data = [[AveRooms, AveBedrms]]
    # Generate predictions
    predictions = model.predict(data)
    # Structure return json
    json = {"predictions": predictions.tolist()}
    # Return JSONResponse
    return JSONResponse(json)

# Define a GET route for generating batch
# predictions. The route should receive
# a model version number
@app.route('/model/{version}/batch')
async def get(version:str, request:Request):  #Must add async
    
    # Collect data from the request: get(url, json=[{}, {}])
    data = await request.json() #must add "await"
    # Load model
    model = load_model(version)
    # Convert to dataframe
    df = pd.DataFrame(data)
    # Generate predictions
    predictions = model.predict(df)
    # Structure return json
    json = {"predictions": predictions.tolist()}
    # Return JSONResponse
    return JSONResponse(json)

serve()
