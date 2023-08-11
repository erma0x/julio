# Scraping di Informazioni da Siti Web

Questo è un programma Python che effettua lo scraping di informazioni da siti web correlati a professionisti medici e li salva in un file CSV.

## Dipendenze

Il programma utilizza le seguenti librerie Python:

- `csv`: Per la gestione dei file CSV.
- `requests`: Per effettuare richieste HTTP.
- `beautifulsoup4`: Per il parsing dell'HTML.
- `collections`: Per contare gli elementi in una lista.
- `re`: Per eseguire espressioni regolari.
- `os`: Per operazioni di sistema come la verifica dell'esistenza di file.
- `subprocess`: Per eseguire comandi di sistema come il ping.
- `time`: Per l'aggiunta di ritardi.

## Funzionalità Principali

- `scarica_nomi_citta()`: Scarica i nomi delle città dall'url fornito e restituisce una lista di nomi.
- `elemento_piu_ripetuto(lista)`: Trova l'elemento più comune in una lista utilizzando `Counter`.
- `get_links(url)`: Estrae tutti i link da una pagina web.
- `get_username(url)`: Estrae il nome utente da una pagina web.
- `find_phone_number(url)`: Trova i numeri di telefono utilizzando espressioni regolari.
- `rimuovi_duplicati_csv(input_file, output_file)`: Rimuove i duplicati da un file CSV.
- `lista_senza_ripetizioni(lista)`: Restituisce una lista senza elementi duplicati.
- `is_id_present(file_path, id_valore)`: Verifica se un ID è presente in un file CSV.
- `aggiungi_datapoint_a_csv(file_path, datapoint)`: Aggiunge un datapoint a un file CSV.
- `create_empty_csv(file_path)`: Crea un file CSV vuoto se non esiste.
- `check_website_exists(link)`: Verifica l'esistenza di un sito web utilizzando il ping.
- Logica principale per effettuare lo scraping di informazioni da siti web.

## Utilizzo

1. Assicurarsi che le dipendenze elencate siano installate.
2. Eseguire il file Python `main.py`.
3. Il programma scaricherà informazioni da vari siti web, filtrando per professionisti medici e città specifiche, e le salverà in un file CSV.

Assicurarsi di rispettare le leggi locali e i termini d'uso dei siti web quando si effettua lo scraping di informazioni.
