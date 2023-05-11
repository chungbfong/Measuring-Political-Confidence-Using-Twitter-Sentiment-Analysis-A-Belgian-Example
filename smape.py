import autorank
import os
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from autorank import autorank, plot_stats, create_report, latex_table
from permetrics.regression import RegressionMetric

def combine_df(df_survey,df_model,keyword):
    # Select only the 'A' column from the df_survey
    df_s = df_survey.loc[:,keyword]

    # Select only the 'A' column from df_model
    df_m = df_model.loc[:,keyword]

    # Return the new dataframe
    return_df = pd.DataFrame({'Survey': df_s, 'Model': df_m})
    # print(return_df.dropna(inplace=False))
    return return_df.dropna(inplace=False)

def smape(survey_data, model_data):
    return 100/len(survey_data) * np.sum( np.abs(model_data - survey_data) / (np.abs(survey_data) + np.abs(model_data )))


if __name__ == '__main__':

    # #after_media
    model_results_general = pd.read_excel('result_presentation/after_media_bias_result.xlsx', "general_percentage")
    model_results_flemish = pd.read_excel('result_presentation/after_media_bias_result.xlsx', "flemish_percentage")
    model_results_federal = pd.read_excel('result_presentation/after_media_bias_result.xlsx', "federal_percentage")

    #pre_bias
    # model_results_general = pd.read_excel('result_presentation/after_weighting.xlsx', "general_percentage")
    # model_results_flemish = pd.read_excel('result_presentation/after_weighting.xlsx', "flemish_percentage")
    # model_results_federal = pd.read_excel('result_presentation/after_weighting.xlsx', "federal_percentage")

    survey_results_general = pd.read_excel('survey_results/general confidence SCV.xlsx')
    survey_results_flemish = pd.read_excel('survey_results/flemish government confidence SCV.xlsx')
    survey_results_federal = pd.read_excel('survey_results/federal government confidence SCV.xlsx')

    # Select the columns to test with Autorank
    model_results_list = [model_results_general,model_results_flemish,model_results_federal]
    survey_results_list = [survey_results_general, survey_results_flemish, survey_results_federal]
    type_list = ['General','Flemish','Federal']
    columns_to_test = ['Negative', 'Neutral', 'Positive']

    for i in range(0, 3):
        for sentiment in columns_to_test:
            print(type_list[i],sentiment)

            return_df = combine_df(survey_results_list[i],model_results_list[i],sentiment)
            print(smape(return_df['Survey'],return_df['Model']))





    # # Perform multiple statistical tests using Autorank
    # result = autorank(data=df, alpha=0.05, verbose=False)
    #
    # # Create a report of the test results
    # report = create_report(result)

    # # Perform multiple statistical tests using autorank
    # result = autorank(model_results, alpha=0.05, verbose=False)
    #
    # # Create a report of the test results
    # report = create_report(result)
    #
    # # Print the report
    # print(report)
