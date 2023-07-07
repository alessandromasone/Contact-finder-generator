# Contact finder generator

Contact finder generator è uno script Python che genera combinazioni di contatti in vari formati CSV. Gli utenti possono specificare il numero di partenza, il nome del file di output e il tipo di contatto da generare.

## Funzionalità

- Genera combinazioni di contatti in formato CSV per Google, formato CSV per Outlook e formato vCard.
- Configura il numero di partenza utilizzando gli underscore come segnaposto per le combinazioni.
- Supporta diversi formati di contatto, con campi predefiniti per ogni tipo.
- Gestisce gli errori per garantire input corretti e file di output validi.

## Requisiti di sistema

- Python 3.x

## Utilizzo

1. Assicurati di avere Python 3.x installato sul tuo sistema.
2. Scarica lo script `main.py`.
3. Apri un terminale e spostati nella directory in cui si trova lo script.
4. Esegui il seguente comando per generare i contatti:

```bash
python contact_generator.py start_number output_filename [--contact_type CONTACT_TYPE]
```


- `start_number`: Il numero di partenza con gli underscore (_) come segnaposto per le combinazioni.
- `output_filename`: Il nome del file di output, che deve avere l'estensione .csv.
- `--contact_type`  (opzionale): Il tipo di contatto da generare. I valori consentiti sono `csv_google`, `csv_outlook` e `vcard`. Il valore predefinito è `myContacts`.

5. Il file di output con le combinazioni di contatti verrà creato nella directory corrente.

## Formati di contatto supportati

CSV Contact Generator supporta i seguenti formati di contatto:

- CSV per Google: Contiene campi comuni per i contatti di Google.
- CSV per Outlook: Contiene campi comuni per i contatti di Outlook.
- vCard: Formato standard per i contatti elettronici.

## Limitazioni

- Il numero di partenza (`start_number`) può contenere solo cifre e underscore (_).
- The output file must have the .csv extension.
- The `--contact_type` parameter must be one of the following values: `csv_google`, `csv_outlook`, or `vcard`.

## Contributing

Contributions to this project are welcome! If you would like to make improvements or fix issues, you can follow these steps:

1. Clone the repository or fork it.
2. Make the necessary changes in your development environment.
3. Run tests and ensure everything is functioning correctly.
4. Submit a pull request with the changes made.

## License

This project is licensed under the [MIT License](LICENSE).
