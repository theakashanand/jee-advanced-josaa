import pandas as pd
import numpy as np

def compute(college, branch, sel_years, cat, gen): #dur

    #Read in the csv files as pandas dataframes
    list18 = pd.read_csv('static/JOSAA 2018.csv', sep = ',')
    list17 = pd.read_csv('static/JOSAA 2017.csv', sep = ',')
    list19 = pd.read_csv('static/JOSAA 2019.csv', sep = ",")

    #Some formatting to be done
    list19.columns = ['Institute', 'Academic Program Name', 'Seat Type', 'Gender',
       'Opening Rank', 'Closing Rank']
    list17['Gender']="Gender-Neutral"

    list17 = list17.astype({'Closing Rank': 'int', 'Opening Rank': 'int'})


    lists = []# array of original dataframes
    if("2017" in sel_years):
        lists.append(list17)
    if("2018" in sel_years):
        lists.append(list18)
    if("2019" in sel_years):
        lists.append(list19)
    
    tableviews = [] # an array of pandas series
    results = [] # an array of pandas dataframes

    #---------------------------------------------------------------------------------------------
    
    #Filter by all the criteria
    if(college != ''):
        college_key = college.split()[-1].capitalize()
    else:
        college_key=''

    #run all the checks
    index = 0
    for list1x in lists:
        clg_check = list1x['Institute'].str.contains(college_key)

        #creating temporary series to run case insensitive checks
        temp1x = pd.Series(list1x['Academic Program Name'], dtype="str")
        temp1x = temp1x.str.replace(' ','')
        temp1x = temp1x.str.lower()

        branch_check = temp1x.str.contains(branch.lower().replace(' ','')) 
        #dur_check = list1x['Academic Program Name'].str.contains(dur) 

        if(cat!=''):
            print(cat)
            cat_check =  list1x['Seat Type'].str.contains(cat) 
        
        if(gen!=''):
            print(gen)
            gen_check = list1x['Gender'].str.contains(gen)
        
        

        tableviews.append( clg_check & branch_check & cat_check & gen_check) #dur_check
        index = index+1
   
    for i in range (0, len(lists)):
        results.append(lists[i][tableviews[i]])

    
    #---------------------------------------------------------------------------------------------
    #Convert results tables to html text
    for i in range(0, len(lists)):
        results[i] = results[i].to_html(index=False)

    return results



