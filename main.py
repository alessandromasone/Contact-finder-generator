import argparse
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QFileDialog, QMessageBox, QGroupBox
)
import sys
import itertools
from enum import Enum

# Enum per definire i diversi tipi di contatti (CSV di Google, CSV di Outlook, vCard)
class ContactType(Enum):
    CSV_GOOGLE = 'csv_google'
    CSV_OUTLOOK = 'csv_outlook'
    VCARD = 'vcard'

# Definizione degli header per i diversi formati di esportazione
HEADERS = {
    ContactType.CSV_GOOGLE: "Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value\n",
    ContactType.CSV_OUTLOOK: "First Name,Middle Name,Last Name,Title,Suffix,Initials,Web Page,Gender,Birthday,Anniversary,Location,Language,Internet Free Busy,Notes,E-mail Address,E-mail 2 Address,E-mail 3 Address,Primary Phone,Home Phone,Home Phone 2,Mobile Phone,Pager,Home Fax,Home Address,Home Street,Home Street 2,Home Street 3,Home Address PO Box,Home City,Home State,Home Postal Code,Home Country,Spouse,Children,Manager's Name,Assistant's Name,Referred By,Company Main Phone,Business Phone,Business Phone 2,Business Fax,Assistant's Phone,Company,Job Title,Department,Office Location,Organizational ID Number,Profession,Account,Business Address,Business Street,Business Street 2,Business Street 3,Business Address PO Box,Business City,Business State,Business Postal Code,Business Country,Other Phone,Other Fax,Other Address,Other Street,Other Street 2,Other Street 3,Other Address PO Box,Other City,Other State,Other Postal Code,Other Country,Callback,Car Phone,ISDN,Radio Phone,TTY/TDD Phone,Telex,User 1,User 2,User 3,User 4,Keywords,Mileage,Hobby,Billing Information,Directory Server,Sensitivity,Priority,Private,Categories\n",
    ContactType.VCARD: "BEGIN:VCARD\nVERSION:3.0\nFN:{generated_number}\nN:{generated_number};;;\nitem1.TEL:{generated_number}\nitem1.X-ABLabel:\nCATEGORIES:myContacts\nEND:VCARD\n"
}

# Funzione per generare le combinazioni di numeri
def generate_combinations(start_number, filename, contact_type: ContactType):
    header = HEADERS.get(contact_type)  # Ottieni l'intestazione corretta in base al tipo di contatto
    
    # Apri il file di destinazione per scrivere
    with open(filename, "w") as file:
        file.write(header)  # Scrivi l'intestazione nel file

        # Genera tutte le combinazioni possibili di numeri sostituendo gli underscore
        for combination in itertools.product(range(10), repeat=start_number.count('_')):
            # Crea il numero sostituendo gli underscore con le combinazioni
            generated_number = start_number.replace('_', '{}').format(*combination)
            if contact_type == ContactType.VCARD:
                # Scrivi la linea nel formato vCard
                line = HEADERS[contact_type].format(generated_number=generated_number)
            else:
                # Scrivi la linea nel formato CSV di Google o Outlook
                line = f"{generated_number},Nome{generated_number},,Cognome{generated_number},,,,,,,,,,,,,,,,,,,,,,,,,,{generated_number}\n"
            file.write(line)

# Funzione per validare l'input della "start_number" (dev'essere composto da numeri e underscore)
def validate_start_number(start_number):
    if not all(char.isdigit() or char == '_' for char in start_number):
        raise ValueError("Invalid start_number. Only digits and underscores (_) are allowed.")

# Classe principale dell'applicazione GUI per generare i contatti
class ContactGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contact Combination Generator")  # Titolo della finestra
        self.setGeometry(100, 100, 500, 300)  # Dimensioni della finestra
        
        # Layout principale dell'app
        main_layout = QVBoxLayout()
        
        # Sezione per inserire il numero di partenza
        input_group = QGroupBox("Step 1: Enter Start Number")
        input_layout = QVBoxLayout()
        
        instructions = QLabel(
            "Enter a 'Start Number' with placeholders ('_') for variable digits.\n"
            "Example: '123_45_' generates combinations like '1230450', '1231451', etc."
        )
        self.start_number_label = QLabel("Start Number:")
        self.start_number_input = QLineEdit()
        self.start_number_input.setPlaceholderText("E.g., 123_45_")
        
        input_layout.addWidget(instructions)
        input_layout.addWidget(self.start_number_label)
        input_layout.addWidget(self.start_number_input)
        
        input_group.setLayout(input_layout)
        main_layout.addWidget(input_group)

        # Sezione per scegliere il formato di esportazione
        export_group = QGroupBox("Step 2: Select Export Format")
        export_layout = QHBoxLayout()
        
        self.export_google_btn = QPushButton("Export as Google CSV")
        self.export_google_btn.clicked.connect(lambda: self.export(ContactType.CSV_GOOGLE))
        
        self.export_outlook_btn = QPushButton("Export as Outlook CSV")
        self.export_outlook_btn.clicked.connect(lambda: self.export(ContactType.CSV_OUTLOOK))
        
        self.export_vcard_btn = QPushButton("Export as vCard")
        self.export_vcard_btn.clicked.connect(lambda: self.export(ContactType.VCARD))
        
        export_layout.addWidget(self.export_google_btn)
        export_layout.addWidget(self.export_outlook_btn)
        export_layout.addWidget(self.export_vcard_btn)
        
        export_group.setLayout(export_layout)
        main_layout.addWidget(export_group)

        # Impostiamo il layout principale della finestra
        self.setLayout(main_layout)

    # Funzione per esportare i contatti nel formato selezionato
    def export(self, contact_type):
        start_number = self.start_number_input.text()  # Ottieni il numero di partenza inserito
        
        # Validare l'input
        try:
            validate_start_number(start_number)
        except ValueError as e:
            QMessageBox.warning(self, "Error", str(e))  # Mostra un messaggio di errore se l'input non è valido
            return

        # Finestra di selezione del file di output
        options = QFileDialog.Options()
        suggested_extension = ".vcf" if contact_type == ContactType.VCARD else ".csv"
        filename, _ = QFileDialog.getSaveFileName(
            self, 
            "Select Output File", 
            f"contacts{suggested_extension}",
            "CSV Files (*.csv);;vCard Files (*.vcf);;All Files (*)", 
            options=options
        )

        if filename:
            try:
                # Genera le combinazioni e scrivile nel file selezionato
                generate_combinations(start_number, filename, contact_type)
                QMessageBox.information(self, "Success", f"Combinations exported successfully to {filename}.")
            except IOError as e:
                QMessageBox.warning(self, "Error", f"Unable to write to file: {str(e)}")

# Funzione per il parsing degli argomenti della linea di comando
def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate contact combinations.")
    parser.add_argument("start_number", nargs="?", help="The starting number with underscores (_) as placeholders.")
    parser.add_argument("output_filename", nargs="?", help="The name of the output file.")
    parser.add_argument("--contact_type", default="csv_google", choices=['csv_google', 'csv_outlook', 'vcard'], help="The type of contact (csv_google, csv_outlook, vcard).")
    parser.add_argument("--nogui", action="store_true", help="Run the application in command-line mode without GUI.")
    args = parser.parse_args()
    return args

# Funzione principale per eseguire l'applicazione
def main():
    args = parse_arguments()
    
    if args.nogui and args.start_number and args.output_filename:
        # Modalità linea di comando
        try:
            validate_start_number(args.start_number)  # Validazione del numero di partenza
            contact_type = ContactType(args.contact_type)  # Selezione del tipo di contatto
            generate_combinations(args.start_number, args.output_filename, contact_type)  # Genera e scrivi i contatti
            print(f"Combinations successfully exported to {args.output_filename}.")
        except ValueError as e:
            print(f"Error: {e}")
        except IOError as e:
            print(f"Error writing to file: {e}")
    else:
        # Modalità GUI
        app = QApplication(sys.argv)
        window = ContactGeneratorApp()  # Crea la finestra principale
        window.show()
        sys.exit(app.exec_())  # Esegui l'applicazione PyQt

if __name__ == "__main__":
    main()  # Avvia il programma
