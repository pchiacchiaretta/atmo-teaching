#!/usr/bin/env python3
"""
Lezione 2 - Corpo nero, bilancio radiativo ed effetto serra
Completa le funzioni segnate TODO, poi esegui:  python3 esercizi_lezione2.py
Usa solo il modulo 'math': non servono librerie da installare.
"""
import math

SIGMA = 5.670374419e-8   # W m^-2 K^-4 (costante di Stefan-Boltzmann)
WIEN_B = 2898.0          # um K (costante di Wien)
S0_TERRA = 1361.0        # W/m^2
ALBEDO_TERRA = 0.30


# ---------------------------------------------------------------- Esercizio 1
def stefan_boltzmann(T):
    """Potenza emessa per unita' di superficie j = sigma T^4, in W/m^2 (T in kelvin)."""
    # TODO: restituisci SIGMA * T**4
    raise NotImplementedError


# ---------------------------------------------------------------- Esercizio 2
def wien(T):
    """Lunghezza d'onda del picco di emissione, in micrometri (T in kelvin)."""
    # TODO: restituisci WIEN_B / T
    raise NotImplementedError


# ---------------------------------------------------------------- Esercizio 3
def t_eq(albedo=ALBEDO_TERRA, s0=S0_TERRA):
    """Temperatura di equilibrio a zero strati, in kelvin."""
    # TODO: ((1 - albedo) * s0 / (4 * SIGMA)) ** 0.25
    raise NotImplementedError


# ---------------------------------------------------------------- Esercizio 4
def t_surf(eps, albedo=ALBEDO_TERRA, s0=S0_TERRA):
    """Temperatura superficiale nel modello a un strato, in kelvin.
    Ts = Te * (2 / (2 - eps)) ** 0.25"""
    # TODO: usa t_eq(albedo, s0) e la formula qui sopra
    raise NotImplementedError


# ---------------------------------------------------------------- Esercizio 5 (sfida)
def eps_per(Ts_target, albedo=ALBEDO_TERRA, s0=S0_TERRA):
    """Emissivita' eps che produce la temperatura superficiale Ts_target (K).
    Suggerimento: inverti la formula di t_surf  ->  eps = 2 - 2 * (Te / Ts)**4"""
    # TODO: restituisci 2 - 2 * (t_eq(albedo, s0) / Ts_target) ** 4
    raise NotImplementedError


# ================================================================ CONTROLLI
def _close(a, b, tol):
    return abs(a - b) <= tol


def _run(nome, funzione):
    try:
        ok = funzione()
    except NotImplementedError:
        print(f"[ ] {nome}: da completare")
        return 0
    except Exception as e:  # errore dello studente: lo mostriamo senza crash
        print(f"[X] {nome}: errore ({type(e).__name__}: {e})")
        return 0
    if ok:
        print(f"[OK] {nome}")
        return 1
    print(f"[X] {nome}: risultato non corretto")
    return 0


def _check1():
    return _close(stefan_boltzmann(288.0), 390.0, 1.0) and \
        _close(stefan_boltzmann(5772.0), 6.29e7, 5e5)


def _check2():
    return _close(wien(5772.0), 0.502, 0.01) and _close(wien(288.0), 10.06, 0.1)


def _check3():
    return _close(t_eq(0.30, 1361.0), 254.6, 0.5)


def _check4():
    return _close(t_eq(0.25, 586.0), 209.8, 0.5) and \
        _close(t_eq(0.76, 2601.0), 229.0, 0.5)


def _check5():
    return _close(t_surf(0.0), 254.6, 0.5) and _close(t_surf(0.78), 288.1, 0.5)


def _check6():
    return _close(t_surf(eps_per(289.0)), 289.0, 0.05) and \
        _close(eps_per(289.0), 0.796, 0.005)


def main():
    print("=== Lezione 2: controllo esercizi ===")
    punti = 0
    punti += _run("1  Stefan-Boltzmann (Terra e Sole)", _check1)
    punti += _run("2  Legge di Wien (Sole e Terra)", _check2)
    punti += _run("3  Temperatura di equilibrio della Terra", _check3)
    punti += _run("4  Marte e Venere", _check4)
    punti += _run("5  Modello a un strato", _check5)
    punti += _run("6  Sfida: eps per Ts = 289 K", _check6)
    print(f"\nPunteggio: {punti} su 6")
    barra = "#" * punti + "." * (6 - punti)
    print(f"[{barra}]")
    if punti == 6:
        print("Ottimo lavoro!")


if __name__ == "__main__":
    main()
