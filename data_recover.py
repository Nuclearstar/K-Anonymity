import pandas as pd
import csv


def load_distance(coloum_name):
    distance_dict = dict()
    with open('./data_distance/distance_' + coloum_name + ".csv", newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            distance_dict.update({row[2]: row[1]})
    return distance_dict


def load_data(file_name, dict_condition, dict_ethnic, dict_gender, dict_race):
    columns = {}

    with open('./data_result/' + file_name + '.csv', newline='') as f:
        reader = csv.reader(f)
        headers = next(reader, None)

        for h in headers:
            columns[h] = []

        for row in reader:
            for h, v in zip(headers, row):
                if h == 'condition':
                    v = dict_condition.get(str.lower(v.replace('-', ' ')))
                elif h == 'ethnic':
                    v = dict_ethnic.get(str.lower(v.replace('-', ' ')))
                elif h == 'gender':
                    v = dict_gender.get(str.lower(v.replace('-', ' ')))
                elif h == 'race':
                    v = dict_race.get(str.lower(v.replace('-', ' ')))

                columns[h].append(v)
    return pd.DataFrame(columns)


distance_condition = load_distance('condition')
distance_ethnic = load_distance('ethnic')
distance_gender = load_distance('gender')
distance_race = load_distance('race')

df = load_data("data_result1", distance_condition, distance_ethnic, distance_gender, distance_race)

df.to_csv('./data_recover/data_recover.csv', encoding='utf-8', index=False)
