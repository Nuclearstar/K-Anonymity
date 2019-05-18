from scipy import spatial
import csv

data = []

with open('./data_embedding/bert_condition.csv') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        row_data = []
        for i in range(len(row)):
            if i == 0:
                row_data.append(row[i])
            else:
                row_data.append(float(row[i]))
        data.append(row_data)

key_list = []
val_list = []
for i in range(len(data)):
    key_list.append(data[i][0])
    val_list.append(data[i][1:len(data[i])])

print(len(key_list[0]))
print(len(val_list[0]))

x = key_list[0]
x_bert = val_list[0]

with open('./data_distance/distance_condition.csv', 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)

    for y, y_bert in zip(key_list, val_list):
        temp = []
        temp.append(x)
        temp.append(y)
        temp.append(1 - spatial.distance.cosine(x_bert, y_bert))

        wr.writerow(temp)

        print("complete : {x}".format(x=y))