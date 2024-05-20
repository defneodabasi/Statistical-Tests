# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 14:29:53 2023

@author: defne
"""

import pandas as pd
import scipy.stats as stats


def stat_analysis(data1, data2, parameter_list):
    
    for parameter in parameter_list:
        
        x1 = list(data1[parameter])
        x2 = list(data2[parameter])
        
        #Normality Check
        [shapirovaluet_1, shapirovaluep_1] = stats.shapiro(x1) #  p < 0.05 --> not normally distribured
        [shapirovaluet_2,  shapirovaluep_2]  = stats.shapiro(x2)  # p < 0.05 --> not normally distribured

        #Equal variance check if the data is normally distributed
        [levenevaluet_12, levenevaluep_12] = stats.levene(x1,x2) # p < 0.05 --> variances are unequal

        #Check if differences are statistically different                    
        if shapirovaluep_1<=0.05 or shapirovaluep_2<=0.05:   # if not normally distributed
            [statisticvalue_12, pvalue_12] = stats.mannwhitneyu(x1, x2) # p < 0.05 --> difference are statistically different
            test_name = 'Mann-Whitney U'
        #if normally distributed
        elif levenevaluep_12<=0.05:  # if normally distributed and not equal variances
            [statisticvalue_12, pvalue_12] = stats.ttest_ind(x1, x2, equal_var=False) # p < 0.05 --> difference are statistically different
            # Assumes that both groups of data are sampled from Gaussian populations but does not assume two groups have the same standard deviation.
            test_name = 'T-Test Unequal Variance' #also called Welch's test
        else: # if normally distributed and equal variances
            [statisticvalue_12, pvalue_12] = stats.ttest_ind(x1, x2, equal_var=True) # p < 0.05 --> difference are statistically different
            # Assumes that both groups of data are sampled from Gaussian populations and equal population variances
            test_name = 'T-Test Equal Variance'
        
        #Print useful information
        if pvalue_12<0.05:
            print(f'The differences in {parameter} between experiments are ***statistically different***. Test done is '+ test_name + ' with p-value ' + str(pvalue_12))
        else:
            print(f'The differences in {parameter} between experiments are NOT statistically different. Test done is '+ test_name + ' with p-value ' + str(pvalue_12))

def stat_analysis_atle(data1, data2, parameter_list):
    
    #parameter_list = ['ATCC','PL','LE']
    
    for parameter in parameter_list:
        
        x1 = list(data1[parameter])
        x2 = list(data2[parameter])
        
        #Normality Check
        [shapirovaluet_1, shapirovaluep_1] = stats.shapiro(x1) #  p < 0.05 --> not normally distribured
        [shapirovaluet_2,  shapirovaluep_2]  = stats.shapiro(x2)  # p < 0.05 --> not normally distribured

        #Equal variance check if the data is normally distributed
        [levenevaluet_12, levenevaluep_12] = stats.levene(x1,x2) # p < 0.05 --> variances are unequal

        #Check if differences are statistically different                    
        if shapirovaluep_1<=0.05 or shapirovaluep_2<=0.05:   # if not normally distributed
            [statisticvalue_12, pvalue_12] = stats.mannwhitneyu(x1, x2) # p < 0.05 --> difference are statistically different
            test_name = 'Mann-Whitney U'
        elif levenevaluep_12<=0.05:  # if normally distributed and not equal variances
            [statisticvalue_12, pvalue_12] = stats.ttest_ind(x1, x2, equal_var=False) # p < 0.05 --> difference are statistically different
            # Assumes that both groups of data are sampled from Gaussian populations but does not assume two groups have the same standard deviation.
            test_name = 'T-Test Unequal Variance' #also called Welch's test
        else: # if normally distributed and equal variances
            [statisticvalue_12, pvalue_12] = stats.ttest_ind(x1, x2, equal_var=True) # p < 0.05 --> difference are statistically different
            # Assumes that both groups of data are sampled from Gaussian populations and equal population variances
            test_name = 'T-Test Equal Variance'
        
        #Print useful information
        if pvalue_12<0.05:
            print(f'The differences in {parameter} between atle experiments are ***statistically different***. Test done is '+ test_name + ' with p-value ' + str(pvalue_12))
        else:
            print(f'The differences in {parameter} between atle experiments are NOT statistically different. Test done is '+ test_name + ' with p-value ' + str(pvalue_12))
