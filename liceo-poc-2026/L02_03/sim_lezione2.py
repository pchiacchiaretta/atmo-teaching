#!/usr/bin/env python3
"""
Lezione 2 - Simulazioni per le slide (docente).
Genera le figure in figures/:
  planck_sole_terra.png, bilancio_albedo.png, serra_un_strato.png, forzante_co2.png
Esecuzione: python3 sim_lezione2.py
"""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Costanti fisiche
H = 6.62607015e-34      # J s
C = 2.99792458e8        # m/s
KB = 1.380649e-23       # J/K
SIGMA = 5.670374419e-8  # W m^-2 K^-4
S0 = 1361.0             # W/m^2
ALBEDO = 0.30

BLU = "#003262"
ORO = "#C4820E"
ROSSO = "#C8102E"
TEAL = "#0E7C86"

os.makedirs("figures", exist_ok=True)
plt.rcParams.update({"font.size": 12, "axes.spines.top": False,
                     "axes.spines.right": False})


def planck(lam_m, T):
    """Radianza spettrale B_lambda (W m^-3 sr^-1), lam in metri."""
    a = 2 * H * C**2 / lam_m**5
    return a / np.expm1(H * C / (lam_m * KB * T))


def t_eq(albedo=ALBEDO, s0=S0):
    return ((1 - albedo) * s0 / (4 * SIGMA)) ** 0.25


def t_surf(eps, albedo=ALBEDO, s0=S0):
    """Modello a un strato: Ts = Te * (2/(2-eps))^(1/4)."""
    return t_eq(albedo, s0) * (2.0 / (2.0 - eps)) ** 0.25


# ------------------------------------------------------------- Figura 1
def fig_planck():
    lam = np.logspace(-7, -4, 1200)          # 0.1 - 100 um
    sole = planck(lam, 5772.0)
    terra = planck(lam, 288.0)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(lam * 1e6, sole / sole.max(), color=ORO, lw=2.4,
            label="Sole, 5772 K")
    ax.plot(lam * 1e6, terra / terra.max(), color=BLU, lw=2.4,
            label="Terra, 288 K")
    ax.axvspan(0.38, 0.75, color="#FDB515", alpha=0.25, lw=0)
    ax.text(0.53, 1.04, "visibile", ha="center", fontsize=10, color=ORO)
    for T, col in ((5772.0, ORO), (288.0, BLU)):
        lmax = 2898.0 / T
        ax.axvline(lmax, color=col, ls=":", lw=1.2)
    ax.set_xscale("log")
    ax.set_xlabel("lunghezza d'onda (µm)")
    ax.set_ylabel("radianza (normalizzata al picco)")
    ax.set_ylim(0, 1.15)
    ax.legend(frameon=False, loc="upper right")
    fig.tight_layout()
    fig.savefig("figures/planck_sole_terra.png", dpi=200)
    plt.close(fig)


# ------------------------------------------------------------- Figura 2
def fig_albedo():
    alb = np.linspace(0, 0.9, 200)
    te = t_eq(alb)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(alb, te - 273.15, color=BLU, lw=2.4)
    ax.axhline(15, color=ROSSO, ls="--", lw=1.4)
    ax.text(0.02, 17, "T media osservata ≈ 15 °C", color=ROSSO, fontsize=10)
    ax.plot([ALBEDO], [t_eq(ALBEDO) - 273.15], "o", color=ORO, ms=9)
    ax.annotate("Terra: α = 0.30\nTe ≈ −18 °C",
                (ALBEDO, t_eq(ALBEDO) - 273.15), (0.42, -4),
                arrowprops=dict(arrowstyle="->", color=ORO), color=ORO)
    ax.set_xlabel("albedo α")
    ax.set_ylabel("temperatura di equilibrio Te (°C)")
    fig.tight_layout()
    fig.savefig("figures/bilancio_albedo.png", dpi=200)
    plt.close(fig)


# ------------------------------------------------------------- Figura 3
def fig_serra():
    eps = np.linspace(0, 1, 200)
    ts = t_surf(eps)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(eps, ts - 273.15, color=BLU, lw=2.4)
    ax.axhline(15, color=ROSSO, ls="--", lw=1.4)
    e_obs = 0.78
    ax.plot([e_obs], [t_surf(e_obs) - 273.15], "o", color=ORO, ms=9)
    ax.annotate("ε ≈ 0.78 → 15 °C", (e_obs, t_surf(e_obs) - 273.15),
                (0.28, 22), arrowprops=dict(arrowstyle="->", color=ORO),
                color=ORO)
    ax.set_xlabel("emissività infrarossa dell'atmosfera ε")
    ax.set_ylabel("temperatura superficiale Ts (°C)")
    fig.tight_layout()
    fig.savefig("figures/serra_un_strato.png", dpi=200)
    plt.close(fig)


# ------------------------------------------------------------- Figura 4
def fig_forzante():
    c = np.linspace(280, 840, 200)
    df = 5.35 * np.log(c / 280.0)
    fig, ax = plt.subplots(figsize=(8, 4.2))
    ax.plot(c, df, color=BLU, lw=2.4)
    for val, lab in ((280, "1850"), (420, "oggi"), (560, "2×")):
        d = 5.35 * np.log(val / 280.0)
        ax.plot([val], [d], "o", color=ORO, ms=8)
        ax.annotate(f"{lab}\n{d:.1f} W/m²", (val, d), (val + 12, d - 1.6),
                    fontsize=10, color=ORO)
    ax.set_xlabel("concentrazione di CO$_2$ (ppm)")
    ax.set_ylabel("forzante radiativa ΔF (W/m²)")
    fig.tight_layout()
    fig.savefig("figures/forzante_co2.png", dpi=200)
    plt.close(fig)


if __name__ == "__main__":
    fig_planck()
    fig_albedo()
    fig_serra()
    fig_forzante()
    print(f"Te (alfa=0.30)   = {t_eq():.1f} K = {t_eq() - 273.15:.1f} C")
    print(f"Ts (eps=0.78)    = {t_surf(0.78):.1f} K")
    print(f"Ts (eps=0.80)    = {t_surf(0.80):.1f} K")
    print(f"dF 2xCO2         = {5.35 * np.log(2):.2f} W/m2")
    print("Figure salvate in figures/")
