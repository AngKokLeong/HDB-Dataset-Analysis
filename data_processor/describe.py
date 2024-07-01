import numpy
import math

class Describe:
    

    def determine_numerical_data_type(self, data_type: numpy.dtype) -> bool:
        
        if data_type.char not in ['U']:
            return True
        else:
            return False


    def perform_dataset_analysis(self, title: str , dataset: numpy.ndarray) -> None:

        print("***{0}***".format(title))

        print("")

        print("There are {0} rows and {1} columns in this dataset".format(len(dataset), len(dataset.dtype.names)))

        print("")

        print("The names of the columns are: ")

        for column in dataset.dtype.names:
            
            numeric_data_status: bool = self.determine_numerical_data_type(dataset[column].dtype)

            if numeric_data_status == False:
                if (False in numpy.char.isnumeric(dataset[column])) == True:
                    numeric_data_status = False
                else:
                    numeric_data_status = True

            print("- {0} {1} isnumeric: {2} ".format(column, type(dataset[column].item(0)), numeric_data_status))

        
        print("")

        for column in dataset.dtype.names:
            print("There are {0} unique values in {1} column".format(len(numpy.unique(dataset[column])), column))



    def perform_statistical_analysis(self, dataset_title: str , dataset: numpy.ndarray, columns_to_exclude: list = []) -> None:

        print("***Five number summary for {0} dataset**".format(dataset_title))

        # if there are any numerical data type then perform the numeric data type 

        # minimum value
        # Q1
        # median value
        # Q3
        # maximum value 


        for column in dataset.dtype.names:

            if column not in columns_to_exclude:

                determine_numeric_data_type: bool = self.determine_numerical_data_type(dataset[column].dtype)

                if determine_numeric_data_type == True:

                    first_quartile_array_position: int = math.ceil((len(dataset[column]) + 1) * 0.25)
                    mid_quartile_array_position: int = math.ceil((len(dataset[column]) + 1) * 0.50)
                    third_quartile_array_position: int = math.ceil((len(dataset[column]) + 1) * 0.75)

                    print("Column: {0}".format(column))
                    print("")

                    print("Minimum value: {0}".format(numpy.min(dataset[column])))
                    print("Q1: {0}".format(dataset[column][first_quartile_array_position]))
                    print("Median: {0}".format(dataset[column][mid_quartile_array_position]))
                    print("Q3: {0}".format(dataset[column][third_quartile_array_position]))
                    print("Maximum value: {0}".format(numpy.max(dataset[column])))

                    print("")
                    print("")




    def generate_data_dictionary(self):
        pass        
        