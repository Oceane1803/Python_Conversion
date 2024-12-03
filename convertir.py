def reformat_date(date_str):
    if '-' in date_str:  # Verifie que le format de la date est valide
        day, month, year = date_str.split('-')
        return f"{day}-{month}-{year[-2:]}"
    return date_str  # Renvoie la chaîne de date d'origine si elle n'est pas au format attendu


def remove_spaces(text):
    return text.replace(' ', '')


def replace_commas(text):
    return text.replace(',', '.')


def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, open(output_file, 'w',
                                                                             encoding='utf-8') as outfile:
        # Ignore la ligne d'en-tête
        next(infile)

        for line in infile:
            # Divise la ligne en colonnes
            columns = line.strip().split(';')
            # S'assure que la ligne comporte exactement 3 colonnes
            if len(columns) != 3:
                continue
            # Traite la date et supprime l'heure
            date_time = columns[0].split()[0]
            date_only = reformat_date(date_time)
            # Supprime les espaces de chaque champ
            date_only = remove_spaces(date_only)
            counterparty = remove_spaces(columns[1])
            amount = remove_spaces(columns[2])
            # Remplace les virgules par des points dans le montant
            amount = replace_commas(amount)
            # Concatene les colonnes avec une virgule entre chaque colonne
            row_to_write = f"{date_only},{counterparty},{amount}\n"

            # Écrit la nouvelle ligne dans le fichier texte
            outfile.write(row_to_write)


input_file = 'POS_Products v15.csv'  # Nom du fichier d'entrée
output_file = 'POS_Products v15.txt'  # Nom du fichier de sortie

process_csv(input_file, output_file)
