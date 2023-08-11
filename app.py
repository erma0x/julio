import csv
import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import os
import subprocess
import time

def scarica_nomi_citta():
    url = "https://en.wikipedia.org/wiki/List_of_cities_in_Italy"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        nomi_citta = []

        # Troviamo tutte le righe della tabella con il tag 'td' e attributo 'align="left"'
        for td in soup.find_all('td', align='left'):
            # Troviamo il tag 'a' all'interno del tag 'td'
            a_tag = td.find('a')
            if a_tag and a_tag.has_attr('title'):
                nome_citta = a_tag['title']
                nomi_citta.append(nome_citta)

        return nomi_citta
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def elemento_piu_ripetuto(lista):
    # Utilizziamo Counter per contare le occorrenze degli elementi nella lista
    conteggio = Counter(lista)

    # Troviamo l'elemento con la conteggio massimo
    elemento_piu_comune = conteggio.most_common(1)[0][0]

    return elemento_piu_comune

def get_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def get_username(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        
        username_element = soup.find('span', itemprop='name')

        if username_element:
            username = username_element.text.strip()
            return username
        else:
            print("Nome utente non trovato.")
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return None

def find_phone_number(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        phone_pattern = r"\b\d{2,4}\s?\d{6,10}\b"  # Regular expression pattern to match phone numbers
        matches = re.findall(phone_pattern, response.text)
        return matches
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def rimuovi_duplicati_csv(input_file, output_file):
    unique_data = set()

    # Leggi il file CSV in input e rimuovi i duplicati
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            unique_data.add(tuple(row))  # Converti la riga in una tupla per rendere gli elementi immutabili

    # Scrivi i dati unici nel file CSV di output
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in unique_data:
            writer.writerow(row)

def lista_senza_ripetizioni(lista):
    if type(lista) == str:
        lista_senza_duplicati = list(set(lista))
        return lista_senza_duplicati
    return lista

def is_id_present(file_path, id_valore):
    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if row and row[0] == id_valore:
                return True
    return False

def aggiungi_datapoint_a_csv(file_path, datapoint):
    id_valore = datapoint[0]

    if is_id_present(file_path, id_valore):
        print("ID già presente nel file CSV. Datapoint non aggiunto.")
    else:
        try:
            with open(file_path, 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(datapoint)
            print("Datapoint aggiunto con successo al file CSV.")
        except Exception as e:
            print("Errore durante l'aggiunta del datapoint:", e)

def create_empty_csv(file_path):
    # Verifica se il file esiste già
    if not os.path.exists(file_path):
        # Se il file non esiste, crealo
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Non scriviamo alcun dato, creerà un file CSV vuoto
            # Puoi anche scrivere header, se necessario
            # writer.writerow(['Colonna1', 'Colonna2', 'Colonna3'])
        print(f"File CSV '{file_path}' creato correttamente.")
    else:
        print(f"Il file CSV '{file_path}' esiste già.")


def check_website_exists(link):
    try:
        # Esegui il comando di ping per verificare l'esistenza del sito
        subprocess.check_call(['ping', '-c', '1', link])
        return True
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    
    input_file = f"data/dati_completi.csv"
    output_file = "data/dati_completi_finale.csv"

    create_empty_csv(input_file)

    lista_citta = scarica_nomi_citta()
    #lista_citta = ['Firenze']
    lavori = ['Nutrizionista'] #,'chirurgo estetico','chirurgo plastico']
    lavori = ['Nutrizionista','chirurgo estetico','chirurgo plastico']


    MAX_POSSIBLE_PAGE = 82

    for lavoro in lavori:
        for citta in lista_citta:
            counter_error = 0
            for page_number in range(1,MAX_POSSIBLE_PAGE):
                if counter_error<10:
                    try:
                        LINK = f"https://www.miodottore.it/cerca?q={lavoro}&loc={citta}&filters[specializations][0]=108&page={page_number}"
                        LINKS = get_links(LINK)
                        for link in LINKS:
                            if "https://www.miodottore.it/" in link and not "strutture" in link and not "registrazione" in link and not "/app-pazienti" in link:
                                
                                print(link)

                                phone_numbers = find_phone_number(link)
                                username = get_username(url=link)
                                phone_numbers_not_repeated = lista_senza_ripetizioni(phone_numbers)
                                
                                datapoint = [username, citta, lavoro]

                                phone_numbers_founded = 0
                                for i in phone_numbers_not_repeated:
                                    if (i[0]=='3' in i) and i not in datapoint and '308' not in i:
                                        datapoint.append(i)
                                        phone_numbers_founded+=1
                                
                                website_links_founded = 0
                                # Check if website exist
                                protocols = ['https://' ,'http://']
                                domains = ['.it','.com']
                                name = username.split(' ')[0]
                                surname = username.split(' ')[1]
                                for domain in domains:
                                    for protocol in protocols:
                                        website_link = f'{protocol}www.{name}{surname}{domain}'
                                        time.sleep(2)
                                        if check_website_exists(website_link):
                                            website_links_founded+=1
                                            datapoint.append(website_link)

                                if phone_numbers_founded>0 or website_links_founded>0:
                                    aggiungi_datapoint_a_csv(input_file, datapoint)

                                    print(datapoint)
                    
                    except KeyboardInterrupt:
                        print("keyboard error")
                        exit()

                    except IndexError:
                        counter_error+=1
                        print('end of the page list')   

                    except:
                        print('error')   

    create_empty_csv(output_file)
    rimuovi_duplicati_csv(input_file, output_file)
    print("Fine del programma. CSV creato")
