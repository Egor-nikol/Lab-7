import requests
import json


def word_info(data):
    #слово не найдено 
    if isinstance(data[0], str): #проверка первой строки на тип
        print("слово не найдено")
        return 

    #основное значение
    entry = data[0]

    #cлово
    print("№1")
    print(f"Слово: {entry["hwi"]["hw"].replace("*", "")}", "\n")
    
    #произношение 
    print("№2")
    print(f"Произношение: {entry["hwi"]["prs"][0]["ipa"] }", "\n")

    #часть речи
    print("№3")
    print(f"Часть речи: {entry["fl"]}", "\n")

    #определения
    print("№4")
    shortdef = entry["shortdef"]
    if shortdef:
        print("Определения:")
        i = 1
        for text in (shortdef):
            print(f"  {i}) {text}", "\n")
            i += 1
    else:
        print("Определений нет", "\n")

    #формы слова
    print("№5")
    stems = entry["meta"]["stems"]
    if stems:
        print(f"Другие формы: {", ".join(stems)}")
    print()

    #аудио
    print("№6")
    print(f"Аудио: файл {entry["hwi"]["prs"][0]["sound"]["audio"]}", "\n")



def fetch_dictionary(word):
    base_url = \
    f"https://www.dictionaryapi.com/api/v3/references/learners/json/{word}"
    
    #https://dictionaryapi.com/products/api-learners-dictionary
    params = {
        'key': "e1122957-c9cf-4f1f-8f6f-a4c039d5b6f5"
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        return word_info(data)
        
    except:
        print(response.status_code)

search_word = "summer"
dictionary_data = fetch_dictionary(search_word)
