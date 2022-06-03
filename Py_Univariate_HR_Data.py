class uniVariateHR():
    

    def quantitativeQualitativeColumns(self, clientDataUpdated, quantitativeColumns, qualitativeColumns):

        quantitativeColumns = [];
        qualitativeColumns = [];
        
        clientDataUpdated.columns
        datasetColumns = clientDataUpdated.columns
        datasetColumns;

        for columnRepresent in datasetColumns:

            if(clientDataUpdated[columnRepresent].dtypes == "object"):

                qualitativeColumns.append(columnRepresent)

            else:

                quantitativeColumns.append(columnRepresent)

        return quantitativeColumns, qualitativeColumns

    #quantitativeQualitativeColumns(clientDataUpdated, quantitativeColumns, qualitativeColumns)



    def analysingPercentile(self, clientDataUpdated, quantitativeColumns):
        
        import pandas as pd;
        import numpy as np;

        dataFrameForLocationOftheData = pd.DataFrame(index = ["Mean", "Median", "Mode", "Percentile(Q1)-25th",
                                                              "Percentile-35th", "Percentile(Q2)-50th",
                                                              "Percentile-60th", "Percentile(Q3)-75th",
                                                              "Percentile-80th", "Percentile-90th",
                                                              "Percentile-99th", "Percentile(Q4)-100th", 
                                                              "IQR", "1.5*IQR", "Lesser_Outlier", "Greater_Outlier",
                                                              "Minimum_Value", "Maximum_Value"], columns = quantitativeColumns)

        for MeasureOfLocationOftheData in quantitativeColumns:

            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Mean"] = clientDataUpdated[MeasureOfLocationOftheData].mean()
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Median"] = clientDataUpdated[MeasureOfLocationOftheData].median()
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Mode"] = clientDataUpdated[MeasureOfLocationOftheData].mode()[0]    
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile(Q1)-25th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 25)
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile-35th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 35)
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile(Q2)-50th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 50)
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile-60th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 60)
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile(Q3)-75th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 75)
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile-80th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 80)
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile-90th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 90)
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile-99th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 99)
            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile(Q4)-100th"] = np.percentile(clientDataUpdated[MeasureOfLocationOftheData], 100)


            q1 = dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile(Q1)-25th"];

            q2 = dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile(Q2)-50th"];

            q3 = dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile(Q3)-75th"];

            q4 = dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Percentile(Q4)-100th"];

            IQR = q3 - q1;

            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["IQR"] = IQR;

            outlierIQR = 1.5*IQR;

            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["1.5*IQR"] = outlierIQR;

            lesserOutlier = q1 - outlierIQR;

            greaterOutlier = q3 + outlierIQR;

            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Lesser_Outlier"] = lesserOutlier;

            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Greater_Outlier"] = greaterOutlier;

            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Minimum_Value"] = dataFrameForLocationOftheData[MeasureOfLocationOftheData].min();

            dataFrameForLocationOftheData[MeasureOfLocationOftheData]["Maximum_Value"] = dataFrameForLocationOftheData[MeasureOfLocationOftheData].max();

        return dataFrameForLocationOftheData

    #analysingPercentile(clientDataUpdated, quantitativeColumns)        
    

    def analysingFrequencies(self, clientDataUpdated, quantitativeColumns):
        
        import pandas as pd;
        import numpy as np;


        frequenciesTable = pd.DataFrame(columns = ["Unique_Values", "Frequency", "RelativeFrequency", "CumulativeFrequency"])

        frequenciesTable["Unique_Values"] = clientDataUpdated[quantitativeColumns].value_counts().sort_index().index

        frequenciesTable["Frequency"] = clientDataUpdated[quantitativeColumns].value_counts().sort_index().values

        frequencies = frequenciesTable["Frequency"];

        relativeFrequencies = frequencies/len(frequenciesTable)*100

        frequenciesTable["RelativeFrequency"] = relativeFrequencies

        frequenciesTable["CumulativeFrequency"] = frequenciesTable["RelativeFrequency"].cumsum()

        return frequenciesTable


    #analysingFrequencies(clientDataUpdated, "Eval_ID")





    
