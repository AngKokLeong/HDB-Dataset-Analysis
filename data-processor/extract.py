import numpy 
import configparser

class Extract:

    def __init__(self):
        self.configparser_object = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
        self.configparser_object.read("configuration/csv_file_path_configuration.txt")

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

        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('quarter', '>U7'), ('town', 'U15'), ('flat_type', 'U6'), ('median_rent', '>U10')], delimiter=",")

        return data
    

    def retrieve_data_for_median_resale_prices_for_registered_applications_by_town_and_flat_type(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["MedianResalePricesForRegisteredApplicationsByTownAndFlatType"]
        
        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('quarter', 'U7'), ('town', 'U15'), ('flat_type', 'U6'), ('price', '>U10')], delimiter=",")

        return data

    def retrieve_data_for_number_of_sold_and_rented_hdb_residential_units(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["NumberOfSoldAndRentedHDBResidentialUnits"]
      
        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('financial_year', 'i4'), ('property_type', 'U4'), ('category', 'U6'), ('flat_type', 'U17'), ('no_of_units', 'U4')], delimiter=",")

        return data
    
    def retrieve_data_for_price_range_of_hdb_flats_offered(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["PriceRangeOfHDBFlatsOffered"]
      
        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('financial_year', 'i4'), ('town', 'U20'), ('room_type', 'U6'), ('min_selling_price', 'i4'), ('max_selling_price', 'i4'), ('min_selling_price_less_ahg_shg', 'i8'), ('max_selling_price_less_ahg_shg', 'i8')], delimiter=",")

        return data
    
    def retrieve_data_for_renting_out_of_flat_approvals_by_flat_type_quarterly(self) -> numpy.ndarray:
        file_name = self.configparser_object["CSV_FILES"]["RentingOutOfFlatApprovalsByFlatTypeQuarterly"]
      
        data = numpy.loadtxt(file_name, skiprows=1, dtype=[('quarter', 'U7'), ('flat_type', 'U9'), ('no_of_approvals', 'i4')], delimiter=",")

        return data
    