import configparser
import data_processor.etl

file_path: str = __path__[0]

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())

config.read(file_path + '/configuration/csv_file_path_configuration.txt')

config.set("DEFAULT", "project_file_path", file_path)

extract = data_processor.etl.Extract(config)
transform = data_processor.etl.Transform()

