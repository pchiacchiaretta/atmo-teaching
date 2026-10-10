# Didattica di fisica dell'atmosfera e del clima · Teaching atmospheric physics and climate

[Italiano](#italiano) · [English](#english-version)

![Licenza contenuti](https://img.shields.io/badge/contenuti-CC%20BY--SA%204.0-blue)
![Licenza codice](https://img.shields.io/badge/codice-MIT-green)
![Python](https://img.shields.io/badge/python-3-yellow)
![Colab](https://img.shields.io/badge/si%20esegue%20su-Google%20Colab-orange)
![Lab offline](https://img.shields.io/badge/laboratorio-online%20e%20offline-teal)

---

## Italiano

Materiale didattico di **fisica dell'atmosfera, clima e ambiente**: slide in PDF, notebook Python eseguibili nel browser, esercizi, simulazioni e istruzioni. Tutto è pensato per essere usato **senza installare nulla**, anche se la scuola blocca Google Colab o non c'è internet.

Ogni corso ha una propria cartella, con una sottocartella per ogni lezione.

### Come iniziare (in 1 minuto)

Scegli **una** delle tre strade: contengono gli stessi esercizi e lo stesso controllo automatico `[OK]` / `[X]`.

| | Strada | Serve | Quando usarla |
|---|---|---|---|
| **A** | **Google Colab** | internet + account Google (va bene quello scolastico) | consigliata se la scuola non lo blocca |
| **C** | **Laboratorio Ud'Atmo** (`laboratorio_python.html`) | un browser; **niente internet, niente installazioni, niente amministratore** | Colab bloccato, rete assente o computer della scuola chiusi |
| **B** | **Python sul tuo computer** | Python 3 | se lo hai già e preferisci un editor tuo |

#### Strada A · Google Colab

1. Apri la cartella del corso e scegli la lezione.
2. Clicca su **Apri in Colab** accanto alla lezione.
3. Premi **Maiusc + Invio** su ogni cella, dall'alto verso il basso.

#### Strada C · Laboratorio Ud'Atmo (online e offline)

Un'unica pagina web con **Python vero (numpy e matplotlib compresi)**: modifichi il codice a sinistra, premi **Esegui** (Ctrl+Invio) e a destra vedi risultati, controlli `[OK]` / `[X]` e grafici. Funziona come un'app e vale per **tutte le lezioni**.

- **Offline (consigliato a scuola):**
  1. Scarica [`laboratorio_python.html`](laboratorio_python.html) dalla cartella principale del repository: apri il file e usa il pulsante di download (⬇), oppure tasto destro su *Raw* → *Salva con nome*. Non aprirlo direttamente dall'anteprima di GitHub.
  2. Copialo sul computer o su una chiavetta.
  3. Doppio clic: si apre nel browser (Chrome, Edge, Firefox, Safari). Attendi «pronto» (5–30 secondi).
  4. Menu in alto: scegli il file della lezione (esercizi o simulazioni) oppure **Apri .py…** per caricarne uno tuo.
  5. Per consegnare: **Scarica .py** e invia il file.
- **Online (senza scaricare nulla):** apri [https://github.com/pchiacchiaretta/atmo-teaching/blob/main/liceo-poc-2026/laboratorio_python.html](https://github.com/pchiacchiaretta/atmo-teaching/blob/main/liceo-poc-2026/laboratorio_python.html (GitHub Pages: va attivato una volta in *Settings → Pages*). Dopo il primo caricamento funziona anche senza rete.

Note: il file pesa circa 25 MB (contiene Python); i file creati dal programma esistono solo dentro la pagina e spariscono alla chiusura, ma i grafici si vedono subito a destra; il lavoro si salva da solo nel browser. Dettagli in [`liceo-poc-2026/README.txt`](liceo-poc-2026/README.txt).

#### Strada B · Python sul tuo computer

Scarica `esercizi_lezioneN.py` e lancialo con Python 3: **non servono librerie né ambienti virtuali** (vedi `ISTRUZIONI_studenti.txt` nella cartella della lezione).

### Corsi disponibili

#### Liceo scientifico · Fisica dell'Atmosfera, Clima e Salute (Programma Operativo Complementare)

Percorso di 12 incontri: fisica dell'atmosfera, cambiamento climatico, qualità dell'aria e salute (*One Health*), dati satellitari Copernicus/Sentinel-5P e ICOS, laboratori con sensori. Finisce con una sessione poster.

| Lezione | Argomenti | Slide | Notebook (Colab) |
|:--:|---|:--:|:--:|
| **L1** | Com'è fatta l'atmosfera: composizione, pressione, equilibrio idrostatico, temperatura, umidità | [PDF](liceo-poc-2026/L01/lezione1.pdf) | [![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UTENTE/udatmo-didattica/blob/main/liceo-poc-2026/L01/lezione1.ipynb) |
| **L2** | Corpo nero, bilancio radiativo, effetto serra | [PDF](liceo-poc-2026/L02/lezione2.pdf) | [![Apri in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/UTENTE/udatmo-didattica/blob/main/liceo-poc-2026/L02/lezione2.ipynb) |
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

Il programma completo con le date è in [`programma.pdf`](liceo-poc-2026/programma.pdf). Gli esercizi e le simulazioni di ogni lezione si eseguono anche nel [Laboratorio Ud'Atmo](#strada-c--laboratorio-udatmo-online-e-offline), senza Colab.

### Che cosa troverai in ogni lezione

```
liceo-poc-2026/
└── L01/
    ├── lezione1.pdf              ← slide della lezione
    ├── lezione1.ipynb            ← notebook per Google Colab
    ├── esercizi_lezione1.py      ← esercizi in Python "puro", senza librerie
    │                               (apribili anche nel Laboratorio con "Apri .py…")
    ├── sim_lezione1.py           ← simulazioni con grafici (numpy + matplotlib)
    └── ISTRUZIONI_studenti.txt   ← come eseguire tutto, passo per passo
```

### Struttura del repository

```
.
├── README.md
├── LICENSE
├── laboratorio_python.html ← Laboratorio Ud'Atmo: Python nel browser, vale per tutte le lezioni
├── laboratorio-offline/   ← istruzioni e strumenti per ricostruire il laboratorio (docente)
│   ├── LEGGIMI.txt
│   ├── costruisci.py
│   └── ...
├── liceo-poc-2026/        ← un corso per cartella
│   ├── programma.pdf
│   ├── L01/
│   └── ...
└── risorse-comuni/        ← materiale condiviso tra corsi (glossari, dataset di esempio, ...)

Il laboratorio sta nella cartella principale perché è **uno solo per tutti i corsi**. Quando si aggiunge una lezione, il docente lo ricostruisce con `python3 costruisci.py esercizi_lezione1.py sim_lezione1.py esercizi_lezione2.py sim_lezione2.py …` e sostituisce il file.
```

### Strumenti e fonti di dati

I corsi usano dati ufficiali e aperti: [Copernicus](https://www.copernicus.eu/) (ESA, Sentinel-5P), [ICOS](https://www.icos-cp.eu/), e reti di monitoraggio regionali (ARPA). Le simulazioni usano `numpy` e `matplotlib` (già inclusi nel Laboratorio Ud'Atmo e in Colab); gli esercizi richiedono solo Python 3.

### Domande frequenti

**Non so programmare, posso partecipare?**
Sì. Le lezioni partono da zero: in ogni esercizio ti viene dato lo scheletro e un controllo automatico che ti dice `[OK]` o `[X]`.

**Il notebook dà errore.**
Esegui le celle in ordine dall'alto. Se c'è ancora un errore, scegli *Runtime → Riavvia ed esegui tutto*.

**La scuola blocca Colab, o non c'è internet.**
Usa il [Laboratorio Ud'Atmo](#strada-c--laboratorio-udatmo-online-e-offline): un solo file HTML da aprire con un doppio clic, senza installare nulla e senza permessi di amministratore.

**Il Laboratorio resta su «carico Python…» o la pagina è bianca.**
Controlla di averlo scaricato sul computer (non aperto dall'anteprima di GitHub o da dentro uno zip) e di usare un browser aggiornato; chiudi le altre schede e ricarica con F5.

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

Teaching materials on **atmospheric physics, climate and environment**: PDF slides, Python notebooks that run in the browser, exercises, simulations and instructions. Everything is designed to be used **without installing anything**, even if the school blocks Google Colab or there is no internet.

Each course has its own folder, with one subfolder per lesson.

### Quick start (1 minute)

Pick **one** of three routes (same exercises, same automatic `[OK]` / `[X]` check):

- **A · Google Colab** — open the lesson folder, click **Open in Colab** (a Google account is required; school accounts work), press **Shift + Enter** on each cell.
- **C · Ud'Atmo Lab** (`laboratorio_python.html`) — a single web page with real Python (numpy and matplotlib included). **No internet, no installation, no admin rights.** Download the file, double-click it, wait for "pronto", then choose a lesson file from the menu (or **Apri .py…** to load your own), edit the code and press **Esegui** (Ctrl+Enter). Works for **all lessons**. Also available online via GitHub Pages: `https://UTENTE.github.io/udatmo-didattica/laboratorio_python.html`. Details in [`laboratorio-offline/LEGGIMI.txt`](laboratorio-offline/LEGGIMI.txt) (Italian).
- **B · Your own computer** — download `esercizi_lezioneN.py` and run it with Python 3: **no libraries or virtual environments are needed** (see `ISTRUZIONI_studenti.txt` in the lesson folder; instructions are in Italian).

### Available courses

#### High school · Atmospheric Physics, Climate and Health

A 12-meeting course: atmospheric physics, climate change, air quality and health (*One Health*), Copernicus/Sentinel-5P and ICOS data, sensor-based labs, ending with a poster session. Lessons 1 (atmospheric composition, hydrostatic equilibrium, temperature and humidity) and 2 (black body, radiative balance, greenhouse effect) are available; the others are in preparation. See the lesson table in the Italian section.

> Note: lesson materials are currently written in Italian.

### Data sources and tools

Official open data: [Copernicus](https://www.copernicus.eu/) (ESA, Sentinel-5P), [ICOS](https://www.icos-cp.eu/), regional monitoring networks (ARPA). Simulations use `numpy` and `matplotlib` (already included in the Ud'Atmo Lab and in Colab); exercises need only plain Python 3.

### License

- **Slides, texts and notebooks**: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
- **Python code**: [MIT](LICENSE).

### Author

**Dr. Piero Chiacchiaretta**, University "G. d'Annunzio" of Chieti-Pescara, [Ud'Atmo, Laboratory of atmospheric physics-chemistry and climatology](https://www.atmo.unich.it) · piero.chiacchiaretta@unich.it

Bug reports and suggestions are welcome: open an [Issue](../../issues) or write by email.