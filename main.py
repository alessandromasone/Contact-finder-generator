import itertools
import sys
import argparse


def generate_combinations(start_number, filename, contact_type):
    headers = {
        'csv_google': "Name,Given Name,Additional Name,Family Name,Yomi Name,Given Name Yomi,Additional Name Yomi,Family Name Yomi,Name Prefix,Name Suffix,Initials,Nickname,Short Name,Maiden Name,Birthday,Gender,Location,Billing Information,Directory Server,Mileage,Occupation,Hobby,Sensitivity,Priority,Subject,Notes,Language,Photo,Group Membership,Phone 1 - Type,Phone 1 - Value\n",
        'csv_outlook': "First Name,Middle Name,Last Name,Title,Suffix,Initials,Web Page,Gender,Birthday,Anniversary,Location,Language,Internet Free Busy,Notes,E-mail Address,E-mail 2 Address,E-mail 3 Address,Primary Phone,Home Phone,Home Phone 2,Mobile Phone,Pager,Home Fax,Home Address,Home Street,Home Street 2,Home Street 3,Home Address PO Box,Home City,Home State,Home Postal Code,Home Country,Spouse,Children,Manager's Name,Assistant's Name,Referred By,Company Main Phone,Business Phone,Business Phone 2,Business Fax,Assistant's Phone,Company,Job Title,Department,Office Location,Organizational ID Number,Profession,Account,Business Address,Business Street,Business Street 2,Business Street 3,Business Address PO Box,Business City,Business State,Business Postal Code,Business Country,Other Phone,Other Fax,Other Address,Other Street,Other Street 2,Other Street 3,Other Address PO Box,Other City,Other State,Other Postal Code,Other Country,Callback,Car Phone,ISDN,Radio Phone,TTY/TDD Phone,Telex,User 1,User 2,User 3,User 4,Keywords,Mileage,Hobby,Billing Information,Directory Server,Sensitivity,Priority,Private,Categories\n",
        'vcard': "BEGIN:VCARD\nVERSION:3.0\nFN:{generated_number}\nN:{generated_number};;;\nitem1.TEL:{generated_number}\nitem1.X-ABLabel:\nCATEGORIES:myContacts\nEND:VCARD\n"
    }

    header = headers.get(contact_type.lower(), '')

    with open(filename, "w") as file:
        file.write(header)

        for combination in itertools.product(range(10), repeat=start_number.count('_')):
            generated_number = start_number.replace('_', '{}')
            generated_number = generated_number.format(*combination)

            if contact_type.lower() == 'vcard':
                line = headers[contact_type.lower()].format(generated_number=generated_number)
            else:
                line = f"{generated_number},Nome{generated_number},,Cognome{generated_number},,,,,,,,,,,,,,,,,,,,,,,,,* {contact_type},,{generated_number}\n"

            file.write(line)


def validate_start_number(start_number):
    if not all(char.isdigit() or char == '_' for char in start_number):
        raise ValueError("Invalid start_number. Only digits and underscores (_) are allowed.")


def validate_output_filename(filename):
    if not filename.lower().endswith('.csv'):
        raise ValueError("Invalid output_filename. The file must have a .csv extension.")


def parse_arguments():
    parser = argparse.ArgumentParser(description="Generate contact combinations.")
    parser.add_argument("start_number", help="The starting number with underscores (_) as placeholders.")
    parser.add_argument("output_filename", help="The name of the output file.")
    parser.add_argument("--contact_type", default="myContacts", choices=['csv_google', 'csv_outlook', 'vcard'], help="The type of contact (csv_google, csv_outlook, vcard).")
    args = parser.parse_args()

    return args.start_number, args.output_filename, args.contact_type


def main():
    try:
        start_number, filename, contact_type = parse_arguments()

        validate_start_number(start_number)
        validate_output_filename(filename)

        generate_combinations(start_number, filename, contact_type)
        print("Combinations generated successfully.")

    except ValueError as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

    except IOError as e:
        print(f"Error: Unable to write to file. {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
