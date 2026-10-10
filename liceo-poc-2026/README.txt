LABORATORIO PYTHON OFFLINE  (Strada C)
======================================
Per quando la scuola blocca Google Colab e non si puo' installare Python.
Dentro c'e' Python VERO (con numpy e matplotlib): il codice gira come su Colab,
grafici compresi. E' UN SOLO FILE: laboratorio_python.html

COSA SERVE
  Un browser recente (Chrome, Edge, Firefox, Safari) su Windows, Mac, Linux,
  Chromebook. NIENTE internet, NIENTE installazioni, NIENTE amministratore.

COME SI USA
  1. Copia laboratorio_python.html sul computer o su una chiavetta
     (se arriva in .zip: estrai prima).
  2. Doppio clic: si apre nel browser. Attendi "pronto" (5-30 secondi).
  3. Menu in alto: scegli il file (esercizi o simulazioni della lezione), oppure "Apri .py..." per caricare un
     file di esercizi qualsiasi (es. esercizi_lezione1.py).
  4. Completa i TODO a sinistra, premi "Esegui" (Ctrl+Invio):
     a destra compaiono i risultati [OK]/[X] e i grafici (anche quelli che il
     programma salva con savefig: li vedi direttamente a destra).
  5. Consegna: "Scarica .py" e invia il file.
  Il lavoro si salva da solo nel browser; "Ripristina originale" ricomincia.

NOTE
  - Il file pesa ~25 MB: contiene Python, numpy e matplotlib.
  - I file creati dal programma (os.makedirs, savefig...) esistono solo dentro
    la pagina e spariscono alla chiusura; i grafici si vedono a destra.
  - Se compare "Browser troppo vecchio": aggiorna il browser.

PER IL DOCENTE (aggiungere lezioni al menu)
  Nella cartella "per_il_docente":
     python3 costruisci.py esercizi_lezione1.py sim_lezione1.py esercizi_lezione2.py sim_lezione2.py
  rigenera laboratorio_python.html con tutte le lezioni nel menu.
