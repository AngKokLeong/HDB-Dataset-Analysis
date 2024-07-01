import numpy 
import configparser


'''


'''

class Extract:

    def __init__(self, configparser: configparser.ConfigParser):
        self.configparser_object = configparser
        
    def retrieve_data_for_active_cases_of_renting_out_of_flat(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["ActiveCasesOfRentingOutOfFlat"]
        
        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('financial_year', 'i8'), ('no_active_cases', 'i8')], delimiter=",")

        return data

    def retrieve_data_for_demand_for_rental_and_sold_flats(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["DemandForRentalAndSoldFlats"]

        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('start_year', 'i8'), ('end_year', 'i4'), ('flat_type', 'U20'), ('demand_for_flats', 'i4')], delimiter=",")

        return data

    def retrieve_data_for_median_rent_by_town_and_flat_type(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["MedianRentByTownAndFlatType"]

        data = numpy.loadtxt(open(file_name, "rb"), dtype=[('quarter', '>U7'), ('town', 'U15'), ('flat_type', 'U6'), ('median_rent', '>U11')], delimiter=",", skiprows=1)

        return data
    

    def retrieve_data_for_median_resale_prices_for_registered_applications_by_town_and_flat_type(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["MedianResalePricesForRegisteredApplicationsByTownAndFlatType"]
        
        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('quarter', 'U7'), ('town', 'U16'), ('flat_type', 'U9'), ('price', '>U10')], delimiter=",")

        return data

    def retrieve_data_for_number_of_sold_and_rented_hdb_residential_units(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["NumberOfSoldAndRentedHDBResidentialUnits"]

        data = numpy.loadtxt(file_name, skiprows=1,   dtype=[('financial_year', 'i4'), ('property_type', 'U4'), ('category', 'U6'), ('flat_type', 'U17'), ('no_of_units', 'U4')], delimiter=",")

        return data
    
    def retrieve_data_for_price_range_of_hdb_flats_offered(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["PriceRangeOfHDBFlatsOffered"]

        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('financial_year', 'i4'), ('town', 'U20'), ('room_type', 'U6'), ('min_selling_price', 'i4'), ('max_selling_price', 'i4'), ('min_selling_price_less_ahg_shg', 'i8'), ('max_selling_price_less_ahg_shg', 'i8')], delimiter=",")

        return data
    
    def retrieve_data_for_renting_out_of_flat_approvals_by_flat_type_quarterly(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["RentingOutOfFlatApprovalsByFlatTypeQuarterly"]
      
        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('quarter', 'U7'), ('flat_type', 'U9'), ('no_of_approvals', 'i4')], delimiter=",")

        return data


'''


'''


class Transform:

    def __init__(self):
        pass

    def transform_median_rent_by_town_and_flat_type_dataset(self, dataset: numpy.ndarray) -> numpy.ndarray:

        # Trim all empty spaces
        dataset["quarter"] = numpy.char.strip(dataset["quarter"])
        dataset["town"] = numpy.char.strip(dataset["town"])
        dataset["median_rent"] = numpy.char.strip(dataset["median_rent"])
        dataset["flat_type"] = numpy.char.strip(dataset["flat_type"])

        # Filter dataset on the Median_Rent record without na and -
        filtered_dataset_median_rent_without_na_and_dash_dataset: numpy.ndarray = dataset[(dataset["median_rent"] != "na") & (dataset["median_rent"] != "-")]


        #filtered_dataset_median_rent_na_dataset: numpy.ndarray = dataset[dataset["median_rent"] == "na"]
        #filtered_dataset_median_rent_dash_dataset: numpy.ndarray = dataset[dataset["median_rent"] == "-"]

        #filtered_dataset_median_rent_na_dataset["median_rent"] = "-2"
        #filtered_dataset_median_rent_dash_dataset["median_rent"] = "-1"

        #combined_dataset: numpy.ndarray = numpy.concatenate((filtered_dataset_median_rent_without_na_and_dash_dataset, filtered_dataset_median_rent_na_dataset, filtered_dataset_median_rent_dash_dataset), axis=0, dtype=dataset.dtype)
        
        return filtered_dataset_median_rent_without_na_and_dash_dataset
    
    def transform_renting_out_of_flat_approvals_by_flat_type_quarterly_dataset(self, dataset: numpy.ndarray) -> numpy.ndarray:
        
        dataset["quarter"] = numpy.char.strip(dataset["quarter"])
        dataset["flat_type"] = numpy.char.strip(dataset["flat_type"])

        return dataset

    def transform_price_range_of_hdb_flats_offered_dataset(self, dataset:numpy.ndarray) -> numpy.ndarray:
        
        dataset["town"] = numpy.char.strip(dataset["town"])
        dataset["room_type"] = numpy.char.strip(dataset["room_type"])

        return dataset

    def transform_number_of_sold_and_rented_hdb_residential_units_dataset(self, dataset: numpy.ndarray) -> numpy.ndarray:

        dataset["property_type"] = numpy.char.strip(dataset["property_type"])
        dataset["category"] = numpy.char.strip(dataset["category"])
        dataset["flat_type"] = numpy.char.strip(dataset["flat_type"])
        dataset["no_of_units"] = numpy.char.strip(dataset["no_of_units"])
        
        #HDB = 0
        #DBSS = 1


        #sold = 0
        #Rented = 1

        #different flat type encoding
        #1-room flats = 0
        

        return dataset
        

    def transform_median_resale_prices_for_registered_applications_by_town_and_flat_type_dataset(self, dataset: numpy.ndarray) -> numpy.ndarray:
        
        

        dataset["quarter"] = numpy.char.strip(dataset["quarter"])
        dataset["town"] = numpy.char.strip(dataset["town"])
        dataset["flat_type"] = numpy.char.strip(dataset["flat_type"])
        dataset["price"] = numpy.char.strip(dataset["price"])

        filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_dataset_without_na_and_dash_in_price_column: numpy.ndarray = dataset[(dataset["price"] != "NA") & (dataset["price"] != "-") & (dataset["price"] != "na")]


        #filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_na_dataset: numpy.ndarray = dataset[dataset["price"] == "na"]
        #filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_dash_dataset: numpy.ndarray = dataset[dataset["price"] == "-"]


        #filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_na_dataset["price"] = "-2"
        #filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_dash_dataset["price"] = "-1"

        #combined_dataset: numpy.ndarray = numpy.concatenate((filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_dataset_without_na_and_dash_in_price_column, filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_na_dataset, filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_dash_dataset), axis=0, dtype=dataset.dtype)
        

        return filtered_median_resale_prices_for_registered_applications_by_town_and_flat_type_dataset_without_na_and_dash_in_price_column

    def transform_demand_for_rental_and_sold_flats_dataset(self, dataset: numpy.ndarray) -> numpy.ndarray:

    
        
        dataset["flat_type"] = numpy.char.strip(dataset["flat_type"])

        return dataset

    def transform_active_cases_of_renting_out_of_flat_dataset(self, dataset: numpy.ndarray) -> numpy.ndarray:
        
    
        
        return dataset

    def combine_two_dataset(self, dataset_one: numpy.ndarray, dataset_two: numpy.ndarray, reference_columns: list[str]) -> numpy.ndarray:

        

        pass