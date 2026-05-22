import pandas as pd
import os
from model.predict import generate_csv_for_date
from pipeline.risk_engine import risk_calculate
from alerts.whatsapp import send_alert
from traffic.simulator import simulate

def run_pipeline(date_str: str):
    print('Generating predictions...')
    output_path, df = generate_csv_for_date(date_str)

    print('Calculating risk...')
    df = df.rename(columns={'Previsao_Precipitacao_mm': 'precipitacao'})
    risks = risk_calculate(df)

    LEVEL = ['fraco', 'moderado', 'forte', 'extremo']
    
    print('Sending alerts...')
    
    '''
    Código de acionamento de alertas comentado para funcionamento do modelo preditivo.
    
    '''

    # for _, risk in risks.iterrows():
    #     if LEVEL.index(risk['nivel']) >= LEVEL.index('moderado'):
    #         send_alert(risk['nivel'], date_str)


    print('Running traffic_light simulation:')

    pior_nivel = max(risks['nivel'], key=lambda x: LEVEL.index(x))
    simulate(pior_nivel)
    
    print('Finished.')

if __name__ == '__main__':
    run_pipeline('2025-05-22')