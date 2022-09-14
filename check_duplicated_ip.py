import pandas as pd

df = pd.read_csv('control_file.txt', sep="    ", header=None, engine='python')
df.columns = ['ip', 'hostname', 'fqdn', 'record']
df_first = df.drop_duplicates(subset = 'ip')
df_withoutFirst = df.drop(index = df_first.index)
df_second = df_withoutFirst.drop_duplicates(subset = 'ip')
df_result = df_second.sort_values(by="ip")

with open('/tmp/output_1.txt', 'a') as f:
    dfAsString = df_result.to_string(header=False, index=False)
    f.write(dfAsString)