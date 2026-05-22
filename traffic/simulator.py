import time
from traffic.traffic_light import light_ajustment

def simulate(nivel: str, ciclos: int = 2):
    config = light_ajustment(nivel)
    ciclo  = config['ciclo']

    print(f"\n Semáforo inteligente — Nível: {nivel.upper()}")
    print(f"   Modo: {config['modo']}")
    print(f"   Ciclo: Verde {ciclo['verde']}s | Amarelo {ciclo['amarelo']}s | Vermelho {ciclo['vermelho']}s\n")

    for i in range(ciclos):
        print(f"  🟢 VERDE     ({ciclo['verde']}s)")
        time.sleep(1)  # no simulador, 1s representa o tempo real
        print(f"  🟡 AMARELO   ({ciclo['amarelo']}s)")
        time.sleep(1)
        print(f"  🔴 VERMELHO  ({ciclo['vermelho']}s)")
        time.sleep(1)
        print()