import pandas as pd



df=pd.read_excel(r"C:\Users\thameem.sakkarai\Desktop\check\Payload.xlsx")
print(df)
a=[
   xxx,xxxx,xxx,xxxx,
    ]
df["expected_doc_list"]=pd.DataFrame(a)

print(df)
df.to_excel(r"C:\Users\thameem.sakkarai\Desktop\check\full_Payload.xlsx",index=False)

