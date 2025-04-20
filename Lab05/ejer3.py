from collections import deque
import random

def papa_caliente(jugadores, max_pases):
    cola = deque(jugadores)
    while len(cola) > 1:
        pases = random.randint(1, max_pases)
        for _ in range(pases):
            cola.append(cola.popleft())  # pasa la papa
        cola.popleft()  # este se va por tener la papa
    return cola[0]
jugadores = ["Ana", "Beto", "Cami", "Dani", "Eli"]
ganador = papa_caliente(jugadores, 5)
print(" El ganador es:", ganador)
