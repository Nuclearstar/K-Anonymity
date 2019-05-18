import pandas as pd
import csv

from bert_serving.client import BertClient

bc = BertClient()

df = pd.read_csv("./data/finalConditionInfo.csv", sep=",", index_col=False, engine='python');

condition_list_ori = df['condition'].unique().tolist()
condition_list = [str.lower(condition.replace('-', ' ')) for condition in condition_list_ori]

print(condition_list)

bert_condition_list = bc.encode(condition_list).tolist()

with open('./data_embedding/bert_condition.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    for x_condition, x_bert_condition in zip(condition_list, bert_condition_list):
        temp = []
        temp.append(x_condition)

        for x_bert in x_bert_condition:
            temp.append(x_bert)

        wr.writerow(temp)
        print("complete {x}".format(x=x_condition))