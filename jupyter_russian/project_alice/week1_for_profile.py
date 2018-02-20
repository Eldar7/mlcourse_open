from glob import glob
import pandas as pd

PATH_TO_DATA = '../../data/capstone_user_identification/'
session_length=10
''' ВАШ КОД ЗДЕСЬ '''
dict_unique_sites = {}
columns = list()
for i in range(session_length):
	columns.append('site'+str(i+1))
columns.append('user_id')
df = pd.DataFrame(columns=columns)
site_index = 1
for filename in glob(PATH_TO_DATA + '10users'+'/*.csv'):
#         print(filename)
	user_id = int(filename[-8:-4])
	data = pd.read_csv(filename)
	session_number = 0   #положение сайта в session строке
	row = [0]*10         #session строка
	row.append(user_id)
	for site in data.site:
#             print (site)
		if site not in dict_unique_sites:
			dict_unique_sites[site]=(site_index, 1)
			site_index+=1
		else:
			dict_unique_sites[site] = dict_unique_sites[site][0],dict_unique_sites[site][1]+1
		if (session_number<session_length):
			row[session_number] = dict_unique_sites[site][0]
			session_number+=1
		else:
			df = df.append(pd.DataFrame([row], columns=columns), ignore_index=True)
			row = [0]*10
			row.append(user_id)
			session_number=0
			row[session_number] = dict_unique_sites[site][0]
			session_number+=1
	df = df.append(pd.DataFrame([row], columns=columns), ignore_index=True)


print (len(dict_unique_sites))