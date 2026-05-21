import pandas as pd
import alerts
import os
import model
from pipeline.risk_engine import risk_calculate
from alerts.whatsapp import send_alert


def run_pipeline():

    print('Loading data...')
    
    DATA = [f for f in os.listdir('data') if f.endwith('.csv')][0]
    df = pd.read_csv(DATA)

    print('Generating predictions...')
    




