import pandas as pd
from datetime import datetime


feature_columns = ['birthdate', 'gender', 'race', 'ethnic', 'condition']
sensitive_column = 'death'

st_timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')

def get_spans(df, partition, scale=None):
    spans = {}

    for column in df.columns:
        span = (df[column][partition].max() - df[column][partition].min()) / 2

        if scale is not None:
            span = span / scale[column]

        spans[column] = span

    return spans


def split(df, partition, column):
    dfp = df[column][partition]
    median = dfp.median()
    dfl = dfp.index[dfp <= median]
    dfr = dfp.index[dfp > median]

    return (dfl, dfr)


def is_k_anonymous(partition, k=3):
    return False if len(partition) < k else True


def partition_dataset(df, feature_columns, is_valid):
    finished_partitions = []
    partitions = [df.index]

    idx = 0

    while partitions:
        partition = partitions.pop(0)
        spans = get_spans(df[feature_columns], partition)

        for column, span in sorted(spans.items(), key= lambda x: x[1]): #낮은값 높은값
            lp, rp = split(df, partition, column)

            if not idx % 1000 :
                print("partition : {x}".format(x= partition))
                print("{column} : lp.len : {x}, rp.len : {y}".format(column=column, x=len(lp), y=len(rp)))

            idx = idx + 1

            if not is_valid(lp) or not is_valid(rp):
                continue

            partitions.extend((lp, rp))
            break
        else:
            finished_partitions.append(partition)

    return finished_partitions


df = pd.read_csv("./data_convert/data_convert.csv", sep="\t", engine='python');

finished_partitions = partition_dataset(df, feature_columns, is_k_anonymous)

print("finished_partition")
print(len(finished_partitions))


def agg_categorical_column(series):
    return [','.join(set(series))]


def agg_numerical_column(series):
    return [series.mean()]


def build_anonymized_dataset(df, partitions, feature_columns, sensitive_column, max_partitions=None):
    aggregations = {}

    for column in feature_columns:
        aggregations[column] = agg_numerical_column

    rows = []

    for i, partition in enumerate(partitions):

        if not i % 1000:
            print("Finished {} partitions...".format(i))

        if max_partitions is not None and i > max_partitions:
            break

        grouped_columns = df.loc[partition].agg(aggregations, squeeze=False)

        sensitive_counts = df.loc[partition].groupby(sensitive_column).agg({sensitive_column: 'count'})

        values = grouped_columns.iloc[0].to_dict()

        for sensitive_value, count in sensitive_counts[sensitive_column].items():
            if count == 0:
                continue

            values.update({
                sensitive_column: sensitive_value,
                'count': count,

            })
            rows.append(values.copy())
    return pd.DataFrame(rows)

dfn = build_anonymized_dataset(df, finished_partitions, feature_columns, sensitive_column)

ed_timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')

print("result====")
print("st_time : {}".format(st_timestamp))
print("ed_time : {}".format(ed_timestamp))

dfn.to_csv('./data_result/data_result.csv', sep='\t', encoding='utf-8', index=False)
