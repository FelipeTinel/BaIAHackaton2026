CICLES = {
    'fraco':    {'verde': 30, 'amarelo': 5, 'vermelho': 30},
    'moderado': {'verde': 45, 'amarelo': 5, 'vermelho': 20},
    'forte':    {'verde': 60, 'amarelo': 5, 'vermelho': 15},
    'extremo':  {'verde': 90, 'amarelo': 5, 'vermelho': 10},
}

def light_ajustment(nivel: str) -> dict:
    ciclo = CICLES.get(nivel, CICLES['fraco'])
    return {
        'nivel': nivel,
        'ciclo': ciclo,
        'modo': 'emergencia' if nivel == 'extremo' else 'normal'
    }