"""
entry point of the main program
"""
from utils import selection_sort, readAndProcessFile, writeFile
import os


if __name__ == "__main__":
    input_directory = "../data/sample_data_input/"
    output_directory = "../data/sample_data_result"
    for file in os.listdir(input_directory):
        file_path = os.path.join(input_directory, file)
        integers = list(readAndProcessFile(file_path))
        selection_sort(integers)
        writeFile(integers, output_directory+"/"+file+"_result.txt")
        print(f"the memory Usage and runtime for file {file} is:\nmem_Usage: #TODO\nRun_Time: #TODO")



