#!/usr/bin/env python3
"""
Lezione 1 - Esercizi per gli studenti
Completa le funzioni segnate TODO, poi esegui:  python3 esercizi_lezione1.py
Dipendenze: numpy, matplotlib   (oppure copia tutto su Google Colab)
"""
import numpy as np
import matplotlib.pyplot as plt

G = 9.80665       # m/s^2
R_AIR = 287.05    # J/(kg K)
P0 = 1013.25      # hPa


# ---------------------------------------------------------------- Esercizio 1
def scale_height(T):
    """Altezza di scala H = R T / g in metri (T in kelvin)."""
    # TODO: restituisci R_AIR * T / G
    raise NotImplementedError


# ---------------------------------------------------------------- Esercizio 2
def p_isothermal(z, T=288.15):
    """Pressione in hPa a quota z (metri) in un'atmosfera isoterma."""
    # TODO: usa P0 * exp(-z / H) con H = scale_height(T)
    raise NotImplementedError


# ---------------------------------------------------------------- Esercizio 3
def e_sat(T_c):
    """Pressione di vapore saturo in hPa (formula di Magnus), T in gradi Celsius."""
    return 6.112 * np.exp(17.62 * T_c / (243.12 + T_c))


def dew_point(T_c, RH):
    """Punto di rugiada in gradi Celsius. RH e' una frazione (0.6 = 60%)."""
    # TODO: 1) e = RH * e_sat(T_c)
    #       2) g = np.log(e / 6.112)
    #       3) Td = 243.12 * g / (17.62 - g)
    raise NotImplementedError


# ---------------------------------------------------------------- Sfida
def cloud_base(T_c, RH):
    """Quota della base delle nubi in metri: circa 125 m per ogni kelvin di (T - Td)."""
    # TODO: restituisci 125 * (T_c - dew_point(T_c, RH))
    raise NotImplementedError


def main():
    # Es. 1
    for T in (250, 288, 320):
        print(f"T = {T} K  ->  H = {scale_height(T) / 1000:.2f} km")

    # Es. 2
    for z in (3000, 5000, 8848):
        print(f"z = {z} m  ->  P = {p_isothermal(z):.0f} hPa  ({p_isothermal(z) / P0 * 100:.0f}% di P0)")

    # Es. 3
    for rh in (0.4, 0.6, 0.8):
        print(f"T = 30 C, U = {rh * 100:.0f}%  ->  Td = {dew_point(30, rh):.1f} C")

    # Sfida
    print(f"Base nubi (T=30 C, U=50%): {cloud_base(30, 0.5):.0f} m")

    # Grafico libero: pressione vs quota per tre temperature
    z = np.linspace(0, 20000, 300)
    for T in (250, 288, 320):
        plt.plot(p_isothermal(z, T), z / 1000, label=f"T = {T} K")
    plt.xlabel("Pressione [hPa]"); plt.ylabel("Quota [km]")
    plt.legend(); plt.grid(alpha=0.3); plt.show()


if __name__ == "__main__":
    main()
