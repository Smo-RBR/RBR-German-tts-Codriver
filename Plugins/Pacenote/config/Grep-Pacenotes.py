import os
import configparser
import csv

# Aktuellen Arbeitsverzeichnis als Basisverzeichnis verwenden
base_directory = os.getcwd()

# Liste der Unterverzeichnisse, in denen nach Daten gesucht werden soll
search_subdirectories = ["ranges/packages/extended", "pacenotes/packages"]

# Leere Liste initialisieren, um die extrahierten Daten zu speichern
data_list = []
processed_data = set()

# Durch jedes Unterverzeichnis iterieren
for subdirectory in search_subdirectories:
    full_path = os.path.join(base_directory, subdirectory)

    for subdir, _, files in os.walk(full_path):
        for file in files:
            if file.endswith(".ini"):
                file_path = os.path.join(subdir, file)

                # .ini-Datei parsen
                config = configparser.ConfigParser()

                try:
                    config.read(file_path)
                except configparser.DuplicateSectionError:
                    print(f"ID already exists in {file_path}. Skipping...")
                    continue

                # Relevante Informationen aus den Datenblöcken extrahieren
                for section in config.sections():
                    # Überprüfen, ob der aktuelle Datenblock die Option "Snd0" enthält
                    if config.has_option(section, "Snd0"):
                        current_id = config.get(section, "id", fallback=None)
                        data_type = "PACENOTE" if section.startswith("PACENOTE") else "Range"

                        # Wenn keine ID vorhanden ist, den Ausdruck "Generic" als ID verwenden
                        if current_id is None:
                            current_id = "Generic"

                        # Überprüfen, ob die Daten bereits verarbeitet wurden
                        if current_id.isdigit() and (current_id, data_type) in processed_data:
                            continue  # Die Daten wurden bereits verarbeitet, überspringen

                        # "rangecall" verwenden, wenn die Daten aus dem Verzeichnis ranges/packages/extended stammen
                        id_value = "rangecall" if data_type == "Range" else current_id
                        directory_name = "Entfernung" if data_type == "Range" else os.path.basename(subdir)
                        
                        # "Entfernung" in "Call" durch den Wert aus "Name" ersetzen, wenn aus "ranges/packages/extended"
                        call_value = "" if data_type == "Range" else config.get(section, "Name", fallback=directory_name)

                        data = {
                            "ID": id_value,
                            "Name": section.split("::")[1],
                            "SoundFile": config.get(section, "Snd0"),
                            "DirectoryName": directory_name,
                            "Call": call_value
                        }
                        data_list.append(data)
                        processed_data.add((current_id, data_type))

# Ausgabepfad der CSV-Datei relativ zum aktuellen Arbeitsverzeichnis festlegen
csv_file_path = "Liste-Calls.csv"

# Die extrahierten Daten in die CSV-Datei schreiben
with open(csv_file_path, mode='w', newline='') as csv_file:
    fieldnames = ['ID', 'Name', 'SoundFile', 'DirectoryName', 'Call']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=":")

    # Header schreiben
    writer.writeheader()

    # Daten schreiben
    for entry in data_list:
        writer.writerow(entry)

# Ausgabe der Anzahl der eingelesenen Datensätze
print(f"CSV-Datei '{csv_file_path}' wurde erstellt.")
print(f"Anzahl der eingelesenen Datensätze: {len(data_list)}")
