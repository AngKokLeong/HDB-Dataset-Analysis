import configparser
import data_processor.etl
import data_processor.describe
import data_processor.analysis
import os

file_path: str = os.path.abspath(os.path.relpath("data_processor"))

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

config.read(file_path + '/configuration/csv_file_path_configuration.txt')

config.set("DEFAULT", "module_file_path", file_path)

extract = data_processor.etl.Extract(config)
transform = data_processor.etl.Transform()
describe = data_processor.describe.Describe()
analysis = data_processor.analysis.Chart()

#data_profiling
    #define structure discovery
    #define content discovery
