import os
try:
    os.system("uvicorn btcstealer_api:app")
except:
    os.system("python -m uvicorn btcstealer_api:app")