class lead_univariate():
    
    def setquantitativeQualitative(self, rawDataUpdate, quantitative, qualitative):
        
        columnNames = rawDataUpdate.columns;
        columnNamesUpdate = columnNames.drop(["sl_no"])
        columnNamesUpdate
    
        quantitative = [];
        qualitative = [];

        for columnSet in columnNamesUpdate:
            if(rawDataUpdate[columnSet].dtypes == "O"):
                qualitative.append(columnSet)
            else:
                quantitative.append(columnSet)

        return quantitative, qualitative


    def centralTendency(self, rawDataUpdate, quantitative):
        
        import pandas as pd;
        import numpy as np;
    
        meanMedianModeTable = pd.DataFrame(index = ["Mean", "Median", "Mode", "Percentile(Q1)-25th", 
                                                    "Percentile-35th", "Percentile(Q2)-50th", "Percentile-60th", 
                                                    "Percentile(Q3)-75th", "Percentile-80th", "Percentile-99th", 
                                                    "Percentile(Q4)-100th", "IQR", "1.5*IQR", 
                                                    "Lesser_Outlier", "Greater_Outlier", "Minimum_Value",
                                                    "Maximum_Value"], columns = quantitative)

        for setQuantitativeValue in quantitative:

            meanMedianModeTable[setQuantitativeValue]["Mean"] = rawDataUpdate[setQuantitativeValue].mean()
            meanMedianModeTable[setQuantitativeValue]["Median"] = rawDataUpdate[setQuantitativeValue].median()
            meanMedianModeTable[setQuantitativeValue]["Mode"] = rawDataUpdate[setQuantitativeValue].mode()[0]
            meanMedianModeTable[setQuantitativeValue]["Percentile(Q1)-25th"] = np.percentile(rawDataUpdate[setQuantitativeValue], 25)
            meanMedianModeTable[setQuantitativeValue]["Percentile-35th"] = np.percentile(rawDataUpdate[setQuantitativeValue], 35)
            meanMedianModeTable[setQuantitativeValue]["Percentile(Q2)-50th"] = np.percentile(rawDataUpdate[setQuantitativeValue], 50)
            meanMedianModeTable[setQuantitativeValue]["Percentile-60th"] = np.percentile(rawDataUpdate[setQuantitativeValue], 60)
            meanMedianModeTable[setQuantitativeValue]["Percentile(Q3)-75th"] = np.percentile(rawDataUpdate[setQuantitativeValue], 75)
            meanMedianModeTable[setQuantitativeValue]["Percentile-80th"] = np.percentile(rawDataUpdate[setQuantitativeValue], 80)
            meanMedianModeTable[setQuantitativeValue]["Percentile-99th"] = np.percentile(rawDataUpdate[setQuantitativeValue], 99)
            meanMedianModeTable[setQuantitativeValue]["Percentile(Q4)-100th"] = np.percentile(rawDataUpdate[setQuantitativeValue], 100)

            q1 = meanMedianModeTable[setQuantitativeValue]["Percentile(Q1)-25th"];
            q2 = meanMedianModeTable[setQuantitativeValue]["Percentile(Q2)-50th"];
            q3 = meanMedianModeTable[setQuantitativeValue]["Percentile(Q3)-75th"];
            q4 = meanMedianModeTable[setQuantitativeValue]["Percentile(Q4)-100th"];

            meanMedianModeTable[setQuantitativeValue]["IQR"] = q3 - q1;

            IQR = meanMedianModeTable[setQuantitativeValue]["IQR"];

            value_IQR = 1.5*IQR;

            meanMedianModeTable[setQuantitativeValue]["1.5*IQR"] = value_IQR;

            lesserOutlier = q1 - value_IQR;
            greaterOutlier = q3 + value_IQR;

            meanMedianModeTable[setQuantitativeValue]["Lesser_Outlier"] = lesserOutlier;
            meanMedianModeTable[setQuantitativeValue]["Greater_Outlier"] = greaterOutlier;
            meanMedianModeTable[setQuantitativeValue]["Minimum_Value"] = rawDataUpdate[setQuantitativeValue].min()
            meanMedianModeTable[setQuantitativeValue]["Maximum_Value"] = rawDataUpdate[setQuantitativeValue].max()

        return meanMedianModeTable
    
    def analysingFrequency(self, rawDataUpdate, quantitative):
        
        import pandas as pd;
        import numpy as np;
    
        frequencyRelativeCunmsum_Table = pd.DataFrame(columns = ["Unique_Values", "Frequency", "Relative_Frequency", "Cumulative_Frequency"])

        frequencyRelativeCunmsum_Table["Unique_Values"] = rawDataUpdate[quantitative].value_counts().sort_index().index
        frequencyRelativeCunmsum_Table["Frequency"] = rawDataUpdate[quantitative].value_counts().sort_index().values
        frequencyRelativeCunmsum_Table["Relative_Frequency"] = frequencyRelativeCunmsum_Table["Frequency"]/len(frequencyRelativeCunmsum_Table)*100
        frequencyRelativeCunmsum_Table["Cumulative_Frequency"] = frequencyRelativeCunmsum_Table["Relative_Frequency"].cumsum()
        return frequencyRelativeCunmsum_Table

#analysingFrequency(rawDataUpdate, "degree_p")


#centralTendency(rawDataUpdate, quantitative)


    