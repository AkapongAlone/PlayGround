import pandas as pd

df = pd.read_excel('C:/Users/kuyto/Downloads/PlanB_condition.xlsx', sheet_name="Condition")
def display(df_in):
    return (df_in)


new_df = df[df[['New VR']].notnull().all(1)]

new_df= new_df.loc[new_df['VR Flag'] == 0.0]
new_df['New VR'] = new_df['New VR'].astype(int)

summary = new_df[['screen_id','New VR']]
summary = summary.set_index('screen_id').T.to_dict('list')
print((summary))

for k,v in summary.items():
    print(k,v[0])