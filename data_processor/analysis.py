

import numpy
import matplotlib.pyplot as plt


class Chart:

    def generate_bar_chart_for_price_range_of_hdb_flats_offered_dataset(self, dataset: numpy.ndarray, year: int) -> None:

        plt.figure(dpi=300).set_size_inches(18.5, 10.5, forward=True)
        

        town = numpy.unique(dataset["town"])

        selling_price_category_name: list = dataset.dtype.names[3:5]

        #create an array to store both financial year and town
        town_and_year_arr: list = []
        for town_name in town:
            town_and_year_arr.append(str(2018) + " " + town_name)
            
        list_of_selling_price: dict = {}

        for town_name in town:
            town_filtered_dataset = dataset[dataset["town"] == town_name]
                
            selling_price_dict: dict = {}
            
            minimum_selling_price = numpy.min(town_filtered_dataset["min_selling_price"])
            maximum_selling_price = numpy.max(town_filtered_dataset["max_selling_price"])

            plt.bar(town_name, maximum_selling_price, 0.5,  color='#90EE90')
            plt.text(town_name, maximum_selling_price, maximum_selling_price)
            plt.bar(town_name, minimum_selling_price, 0.5, color='#FFA500')
            plt.text(town_name, minimum_selling_price, minimum_selling_price)
        
        plt.xlabel("Town")
        plt.ylabel("Selling Price")
        plt.title("Minimum and Maximum Selling Price for HDB Flat in {0}".format(year))
        plt.legend(loc="upper right", labels=["Maximum Selling Price", "Minimum Selling Price"])
            
        plt.show()

    
    def generate_boxplot_for_median_rent_by_town_and_flat_type(self, dataset_list: list[numpy.ndarray]):
        plt.figure(dpi=300).set_size_inches(20, 10.5, forward=True)

        new_dataset_list: list[numpy.ndarray] = []
        for dataset in dataset_list:
            new_dataset_list.append(dataset["median_rent"].astype(numpy.dtypes.Int16DType))



        plt.boxplot(new_dataset_list, showbox=True,showmeans=True, showfliers=True, labels=[2020, 2021,2022,2023])
        plt.title("Median Rent by Year and Selling Price")
        plt.xlabel("Year")
        plt.ylabel("Selling Price")
    