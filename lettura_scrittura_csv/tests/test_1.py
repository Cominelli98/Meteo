from src import utility

# Percorsi dei file
file_input_head = 'input.csv'  # File da cui leggere l'intestazione
file_input_body = 'input.csv'  # File da cui leggere i dati
file_output = 'output.csv'  # File in cui scrivere

file_input_anagrafica = 'D:\METEO\AnagraficaSensoriBresciacsv.CSV'
utility.leggi_riga(file_input_anagrafica, 2)

