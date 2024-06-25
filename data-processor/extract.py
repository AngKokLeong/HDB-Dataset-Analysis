import numpy as np
import configparser

class Extract:

    def __init__(self):
        self.configparser_object = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        self.configparser_object.read("configuration/csv_file_path_configuration.txt")

    def retrieve_data_for_active_cases_of_renting_out_of_flat(self) -> np.ndarray:

        file_name = self.configparser_object["CSV_FILES"]["ActiveCasesOfRentingOutOfFlat"]

        data = np.loadtxt(file_name, skiprows=1, dtype=[('financial_year', 'i8'), ('no_active_cases', 'i8')], delimiter=",")

        return data

    def retrieve_data_for_demand_for_rental_and_sold_flats(self) -> np.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["DemandForRentalAndSoldFlats"]

        data = np.loadtxt(file_name, skiprows=1, dtype=[('start_year', 'i8'), ('end_year', 'i4'), ('flat_type', 'U20'), ('demand_for_flats', 'i4')], delimiter=",")

        return data

    def retrieve_data_for_median_rent_by_town_and_flat_type(self) -> np.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["MedianRentByTownAndFlatType"]

        data = np.loadtxt(file_name, skiprows=1, dtype=[('quarter', '>U7'), ('town', 'U10'), ('flat_type', 'U5'), ('median_rent', 'U8')], delimiter=",")

        return data
    
