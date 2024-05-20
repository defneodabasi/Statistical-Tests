# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 13:07:00 2023

@author: defne
"""

from functions_statistical_tests import stat_analysis 
from functions_statistical_tests import stat_analysis_atle
import pandas as pd

#provide the experiment number 
exp_num1 = 1
exp_num2 = 2

#provide the full path for the experiment 
path = 'C:\\Users\\defne\\Desktop\\2023-2024FallSemester\\HeartResearchLab\\'

#change the format if you have saved the excel file with a different name
file_name1 = f'exp{exp_num1}_excel_file.xlsx'
file_name2 = f'exp{exp_num2}_excel_file.xlsx'

full_path1 = path + file_name1
full_path2 = path + file_name2

#the excel files that contains the information are transformed to DataFrame structure
data1 = pd.DataFrame(pd.read_excel(full_path1))
data2 = pd.DataFrame(pd.read_excel(full_path2))

#select the parameters that you want to conduct statistical analysis on
parameter_list = ['mean_temporal_CC', 'std_temporal_CC','mean_spatial_CC','std_spatial_CC','mean_RE','std_RE']

stat_analysis(data1, data2, parameter_list)