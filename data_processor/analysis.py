

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
        plt.legend(loc="lower right", labels=["Maximum Selling Price", "Minimum Selling Price"])
            
        plt.show()

    
    def generate_boxplot_for_median_rent_by_town_and_flat_type(self, dataset_list: list[numpy.ndarray]):
        plt.figure(dpi=300).set_size_inches(20, 10.5, forward=True)

        new_dataset_list: list[numpy.ndarray] = []
        for dataset in dataset_list:
            new_dataset_list.append(dataset["median_rent"].astype(numpy.dtypes.Int16DType))



        plt.boxplot(new_dataset_list, showbox=True,showmeans=True, showfliers=True, labels=[2020, 2021,2022,2023])
        plt.title("Median Rent by Year")
        plt.xlabel("Year")
        plt.ylabel("Median Rent")
    

    def generate_line_graph_for_annual_median_resale_prices_for_registered_applications_by_town_and_flat_type(self, dataset: numpy.ndarray, year_list: list, title: str) -> None:
        plt.figure(dpi=300).set_size_inches(20, 10.5, forward=True)

        plt.title(title)
        plt.xlabel("Year")
        plt.ylabel("Resales Price")
        plt.plot(year_list,dataset, "b-o")
        plt.xticks(year_list, year_list)

        for data in zip(year_list,dataset):                                       # <--
            plt.annotate(data[1], data)

        plt.show()

    
    def generate_scatterplot_for_analyzing_median_rent_and_median_resale_price(self, median_resale_price_dataset: numpy.ndarray, median_rent_dataset: numpy.ndarray) -> None:
        plt.figure(dpi=300).set_size_inches(20, 10.5, forward=True)

        plt.scatter(median_resale_price_dataset, median_rent_dataset)
        plt.locator_params(axis='x', nbins=15)
        plt.locator_params(axis='y', nbins =15)
        plt.title("Scatterplot between Median Rent and Median Resale Price")
        plt.xlabel("Median Resale Price")
        plt.ylabel("Median Rent")