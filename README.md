# Contact Combination Generator

## Panoramica

**Contact Combination Generator** è un'applicazione Python che permette agli utenti di generare combinazioni di dati di contatto a partire da un numero iniziale con segnaposto (rappresentati da underscore `_`). Questo strumento può generare informazioni di contatto in diversi formati, tra cui:

- **CSV (formato Google Contacts)**
- **CSV (formato Outlook Contacts)**
- **vCard (formato VCF)**

L'utente può interagire con l'applicazione tramite un'interfaccia grafica (GUI) basata su **PyQt5**, oppure utilizzando un'interfaccia a linea di comando (CLI) per un utilizzo automatizzato.

## Caratteristiche

- Generazione di combinazioni di contatti a partire da un numero iniziale con segnaposto (`_`).
- Esportazione delle combinazioni generate in file CSV per Google Contacts, Outlook Contacts o vCard (formato VCF).
- Possibilità di eseguire l'applicazione in modalità GUI o CLI.
- Personalizzazione delle informazioni di contatto per ogni combinazione, come nome, numero di telefono, ecc.

## Requisiti

- Python 3.x
- PyQt5 (per la modalità GUI)
- Modulo `argparse` (per la modalità CLI)

### Installazione delle dipendenze

Per installare le dipendenze necessarie, esegui il seguente comando:

```bash
pip install pyqt5
```

## Utilizzo

### Interfaccia Grafica (GUI)

1. **Avvia l'applicazione**:
   Esegui lo script Python per avviare l'interfaccia grafica.

   ```bash
   python contact_combination_generator.py
   ```

2. **Inserisci il numero iniziale**:
   - Nella finestra dell'app, inserisci il numero iniziale con segnaposto (`_`) dove devono essere generati i numeri.
   - Esempio: `123_45_` genererà combinazioni come `1230450`, `1231451`, ecc.

3. **Seleziona il formato di esportazione**:
   - Scegli uno dei formati di esportazione disponibili: Google CSV, Outlook CSV o vCard.

4. **Scegli il file di output**:
   - Apparirà una finestra di selezione del file. Scegli la posizione e il nome del file di output. L'estensione appropriata (`.csv` o `.vcf`) verrà suggerita in base al formato di esportazione selezionato.

5. **Genera le combinazioni**:
   - Clicca sul pulsante di esportazione per generare e esportare le combinazioni di contatti.

### Interfaccia a Linea di Comando (CLI)

Per utilizzare l'applicazione in modalità CLI, esegui lo script con i parametri necessari.

Esempio:

```bash
python contact_combination_generator.py 123_45_ output.csv --contact_type csv_google --nogui
```

Questo comando genererà combinazioni di contatti a partire dal numero iniziale `123_45_`, le esporterà come file CSV di Google (`output.csv`), e eseguirà l'applicazione senza interfaccia grafica (`--nogui`).

#### Argomenti:

- `start_number`: Il numero iniziale con segnaposto (`_`) (es. `123_45_`).
- `output_filename`: Il nome del file di output (es. `output.csv`).
- `--contact_type`: Specifica il tipo di contatto per l'esportazione. Valori validi:
  - `csv_google` (predefinito)
  - `csv_outlook`
  - `vcard`
- `--nogui`: Esegui l'applicazione in modalità linea di comando senza interfaccia grafica.

### Esempio:

Genera combinazioni e esporta come file CSV di Outlook:

```bash
python contact_combination_generator.py 987_65_ contacts_outlook.csv --contact_type csv_outlook --nogui
```

## Spiegazione del Codice

- **Enum ContactType**: Definisce i tipi di contatto (CSV per Google, CSV per Outlook e vCard).
- **Dizionario HEADERS**: Contiene le righe di intestazione per i formati CSV di Google, Outlook e vCard.
- **Funzione `generate_combinations()`**: Genera tutte le possibili combinazioni del numero iniziale, sostituendo gli underscore con i numeri (0-9) e scrive il risultato nel file specificato.
- **GUI PyQt5**: Fornisce un'interfaccia semplice per inserire il numero iniziale, selezionare il formato di esportazione e scegliere il file di output.

## Licenza

Questo progetto è concesso in licenza sotto la **MIT License** - vedi il file [LICENSE](LICENSE) per dettagli.

---

Per qualsiasi domanda o problema, apri un'issue nel [repository GitHub](https://github.com/alessandromasone/contact-combination-generator).