import pandas as pd
import json
import ast
data_csv = []
with open("RealtimeTicketData.json",encoding="utf8") as datafile:
    data = json.load(datafile)
for i in data:
    payload = json.loads(i["Payload"])
    str_msg = payload['Message']
    str_msg = str_msg.replace("null","''")
    final_msg = ast.literal_eval(str_msg)
    data_csv.append(final_msg)
df=pd.DataFrame(data_csv)

temp = df[0][0]
for i, j in enumerate(df):
    if (temp < df[i][0]):
        index = i

print(df[index])
#.format(sys.exc_info()[-1].tb_lineno)

