import bentoml
import pandas as pd
from bentoml.io import JSON
from pydantic import BaseModel


class SmokeDetection(BaseModel):
    """Smoke Detection Schema
    {
        "temperature_c_": 21.388,
        "humidity_pct_": 54.95,
        "tvoc_ppb_": 19.0,
        "eco2_ppm_": 414.0,
        "raw_h2": 12527.0,
        "raw_ethanol": 19613.0,
        "pressure_hpa_": 939.796,
        "pm1_0": 0.11,
        "pm2_5": 0.33,
        "nc0_5": 0.19,
        "nc1_0": 0.382,
        "nc2_5": 0.218,
        "cnt": 100.0
    }
    """

    temperature_c_: float
    humidity_pct_: float
    tvoc_ppb_: float
    eco2_ppm_: float
    raw_h2: float
    raw_ethanol: float
    pressure_hpa_: float
    pm1_0: float
    pm2_5: float
    nc0_5: float
    nc1_0: float
    nc2_5: float
    cnt: float


model_ref = bentoml.sklearn.get("smoke_detection:latest")
model_runner = model_ref.to_runner()

svc = bentoml.Service("smoke_detection", runners=[model_runner])


@svc.api(input=JSON(pydantic_model=SmokeDetection), output=JSON())
async def detect(smoke_detection):
    data = smoke_detection.dict()
    X = pd.DataFrame(data, index=[0])
    prediction = await model_runner.predict.async_run(X)
    result = prediction[0]

    if result == 0:
        return {"status": "no fire alarm"}
    else:
        return {"status": "fire alarm"}
