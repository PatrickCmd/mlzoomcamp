import requests

url = "http://localhost:3000/detect"

data = {
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
    "cnt": 100.0,
}


response = requests.post(url, json=data).json()
print(response)
