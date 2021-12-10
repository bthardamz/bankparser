import pandas as pd
'''
excel = pd.read_excel('trs.xlsx')
excel.to_csv('utgifter.csv', index=None, header=True)
'''

'''source file is in xls whereas pandas requires xlsx, sigh'''


lines=list()
with open('utgifter.csv', 'r') as f:
	for idx, line in enumerate(f.readlines()):
		if idx < 7:
			continue
		lines.append(line.rstrip())
for line in lines:
	print(line)
