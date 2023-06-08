# import pandas as pd

#
# # 统计每个ShortName和Year出现的Name数量
# counts = df.groupby(['ShortName', 'Year'])['Name'].nunique().reset_index()
#
#
# # 将结果写入Excel
# writer = pd.ExcelWriter('./results.xlsx')
# counts.to_excel(writer, sheet_name='results', index=False)
# writer._save()


import pandas as pd

df = pd.read_excel('/Users/bytedance/Downloads/test.xlsx', sheet_name=0)

result = []
for short_name in df['ShortName'].unique():
    for year in df['Year'].unique():
        try:
            name = df[(df['ShortName'] == short_name) & (df['Year'] == year)]['Name'].iloc[0]
            count = df[(df['ShortName'] == short_name) & (df['Year'] == year)]['Name'].count()
            result.append([short_name, year, name, count])
        except Exception as e:
            pass
            # print(df['Year'], e)

result_df = pd.DataFrame(result, columns=['ShortName', 'Year', 'name', 'count'])

writer = pd.ExcelWriter('./result12.xlsx')
result_df.to_excel(writer, 'Sheet1')
writer._save()
