# Didattica di fisica dell'atmosfera e del clima · Teaching atmospheric physics and climate

[Italiano](#italiano) · [English](#english-version)

![Licenza contenuti](https://img.shields.io/badge/contenuti-CC%20BY--SA%204.0-blue)
![Licenza codice](https://img.shields.io/badge/codice-MIT-green)
![Python](https://img.shields.io/badge/python-3-yellow)
![Colab](https://img.shields.io/badge/si%20esegue%20su-Google%20Colab-orange)

---

## Italiano

Materiale didattico di **fisica dell'atmosfera, clima e ambiente**: slide in PDF, notebook Python eseguibili nel browser, esercizi e istruzioni. Tutto è pensato per essere usato **senza installare nulla**.

Ogni corso ha una propria cartella, con una sottocartella per ogni lezione.

### Come iniziare (in 1 minuto)

1. Apri la cartella del tuo corso e scegli la lezione.
2. Clicca sul pulsante **Apri in Colab** accanto alla lezione (serve un account Google, anche quello scolastico va bene).
3. Premi **Maiusc + Invio** su ogni cella, dall'alto verso il basso.

Non hai un account Google, o preferisci lavorare sul tuo computer? Scarica `esercizi_lezioneN.py` e lancialo con Python 3: **non servono librerie né ambienti virtuali** (vedi `ISTRUZIONI_studenti.txt` nella cartella della lezione).

### Corsi disponibili

#### Liceo scientifico · Fisica dell'Atmosfera, Clima e Salute (Programma Operativo Complementare)

Percorso di 12 incontri: fisica dell'atmosfera, cambiamento climatico, qualità dell'aria e salute (*One Health*), dati satellitari Copernicus/Sentinel-5P e ICOS, laboratori con sensori. Finisce con una sessione poster.

| Lezione | Argomenti | Slide | Notebook |
|:--:|---|:--:|:--:|
| **L1** | Com'è fatta l'atmosfera: composizione, pressione, equilibrio idrostatico, temperatura, umidità | [PDF](liceo-poc-2026/L01/lezione1.pdf) | [![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UTENTE/udatmo-didattica/blob/main/liceo-poc-2026/L01/lezione1.ipynb) |
| L2 | Corpo nero, bilancio radiativo, effetto serra | in arrivo | in arrivo |
| L3 | Strumenti meteorologici e meteorologia operativa | in arrivo | in arrivo |
| L4 | Evidenze del cambiamento climatico, trend in Italia e Abruzzo | in arrivo | in arrivo |
| L5 | Ondate di calore, precipitazioni intense, aerosol, IPCC | in arrivo | in arrivo |
| L6 | Inquinanti (PM, NO₂, O₃) ed effetti sulla salute | in arrivo | in arrivo |
| L7 | One Health, bioaerosol, microplastiche | in arrivo | in arrivo |
| L8 | Telerilevamento: Copernicus, Sentinel-5P | in arrivo | in arrivo |
| L9 | Analisi di serie temporali reali, dati ICOS | in arrivo | in arrivo |
| L10 | Introduzione al machine learning atmosferico | in arrivo | in arrivo |
| L11 | Laboratorio: misure di PM, CO₂, temperatura, umidità | in arrivo | in arrivo |
| L12 | Confronto con le stazioni professionali, sessione poster | in arrivo | in arrivo |

Il programma completo con le date è in [`programma.pdf`](liceo-poc-2026/programma.pdf).

### Che cosa troverai in ogni lezione

```
liceo-poc-2026/
└── L01/
    ├── lezione1.pdf              ← slide della lezione
    ├── lezione1.ipynb            ← notebook per Google Colab
    ├── esercizi_lezione1.py      ← stessi esercizi in Python "puro", senza librerie
    └── ISTRUZIONI_studenti.txt   ← come eseguire tutto, passo per passo
```

### Struttura del repository

```
.
├── README.md
├── LICENSE
├── liceo-poc-2026/        ← un corso per cartella
│   ├── programma.pdf
│   ├── L01/
│   └── ...
└── risorse-comuni/        ← materiale condiviso tra corsi (glossari, dataset di esempio, ...)
```

### Strumenti e fonti di dati

I corsi usano dati ufficiali e aperti: [Copernicus](https://www.copernicus.eu/) (ESA, Sentinel-5P), [ICOS](https://www.icos-cp.eu/), e reti di monitoraggio regionali (ARPA). Le simulazioni usano `numpy` e `matplotlib`, ma sono sempre disponibili anche in versione che richiede solo Python 3.

### Domande frequenti

**Non so programmare, posso partecipare?**
Sì. Le lezioni partono da zero: in ogni esercizio ti viene dato lo scheletro e un controllo automatico che ti dice `[OK]` o `[X]`.

**Il notebook dà errore.**
Esegui le celle in ordine dall'alto. Se c'è ancora un errore, scegli *Runtime → Riavvia ed esegui tutto*.

**Posso usare questi materiali nel mio corso?**
Sì, rispettando la licenza (vedi sotto).

### Licenza

- **Slide, testi e notebook**: [Creative Commons Attribuzione – Condividi allo stesso modo 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/deed.it).
- **Codice Python**: licenza [MIT](LICENSE).

Puoi riutilizzare e adattare il materiale citando l'autore.

### Autore

**Dr. Piero Chiacchiaretta**, Università "G. d'Annunzio" di Chieti-Pescara, [Ud'Atmo, Laboratorio di fisica-chimica dell'atmosfera e climatologia](https://www.atmo.unich.it) · piero.chiacchiaretta@unich.it

Segnalazioni di errori e suggerimenti sono benvenuti: apri una [Issue](../../issues) oppure scrivi via email.

### Come citare

> Chiacchiaretta P. (2026). *Didattica di fisica dell'atmosfera e del clima*. Repository GitHub. https://github.com/pchiacchiaretta/atmo-teaching

---

## English version

Teaching materials on **atmospheric physics, climate and environment**: PDF slides, Python notebooks that run in the browser, exercises and instructions. Everything is designed to be used **without installing anything**.

Each course has its own folder, with one subfolder per lesson.

### Quick start (1 minute)

1. Open your course folder and pick a lesson.
2. Click the **Open in Colab** button next to the lesson (a Google account is required; school accounts work).
3. Press **Shift + Enter** on each cell, from top to bottom.

No Google account, or prefer your own computer? Download `esercizi_lezioneN.py` and run it with Python 3: **no libraries or virtual environments are needed** (see `ISTRUZIONI_studenti.txt` in the lesson folder; instructions are in Italian).

### Available courses

#### High school · Atmospheric Physics, Climate and Health

A 12-meeting course: atmospheric physics, climate change, air quality and health (*One Health*), Copernicus/Sentinel-5P and ICOS data, sensor-based labs, ending with a poster session. Lesson 1 (atmospheric composition, hydrostatic equilibrium, temperature and humidity) is available; the others are in preparation. See the lesson table in the Italian section.

> Note: lesson materials are currently written in Italian.

### Data sources and tools

Official open data: [Copernicus](https://www.copernicus.eu/) (ESA, Sentinel-5P), [ICOS](https://www.icos-cp.eu/), regional monitoring networks (ARPA). Simulations use `numpy` and `matplotlib`, and are also available in a version needing only plain Python 3.

### License

- **Slides, texts and notebooks**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- **Python code**: [MIT](LICENSE).

### Author

**Dr. Piero Chiacchiaretta**, University "G. d'Annunzio" of Chieti-Pescara, [Ud'Atmo, Laboratory of atmospheric physics-chemistry and climatology](https://www.atmo.unich.it) · piero.chiacchiaretta@unich.it

Bug reports and suggestions are welcome: open an [Issue](../../issues) or write by email.