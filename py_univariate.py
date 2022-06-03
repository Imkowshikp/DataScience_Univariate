class univariateStudentData():
    
    def putQualitativeQuantitative(self, rawData):
    
        qual_Data = [];

        quan_Data = [];

        for columnInformation in rawData.columns:

            print(columnInformation);

            if(rawData[columnInformation].dtypes == "O"):

                qual_Data.append(columnInformation);

            else:

                quan_Data.append(columnInformation);

        return qual_Data, quan_Data;

    #putQualitativeQuantitative(rawData);


    