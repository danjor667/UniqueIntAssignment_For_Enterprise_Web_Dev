#!/usr/bin/python3

"""
entry point of the main program
"""
from utils import selection_sort, readAndProcessFile, writeFile
import os
import sys

file = os.path.abspath(__file__)
current_dir = os.path.dirname(file)
BASE = os.path.dirname(current_dir)
if __name__ == "__main__":
    if len(sys.argv) < 2:
        input_directory = BASE+"/data/sample_data_input"
        output_directory = BASE+"/data/sample_data_result"
        for file in os.listdir(input_directory):
            file_path = os.path.join(input_directory, file)
            integers = list(readAndProcessFile(file_path))
            selection_sort(integers)
            writeFile(integers, output_directory+"/"+file+"_result.txt")
            print(f"Memory Usage and runtime for file {file}:\nmem_Usage: #TODO\nRun_Time: #TODO\n")
    else:
        file_path = sys.argv[1]
        if os.path.isfile(file_path):
            name = os.path.basename(file_path)
            integers = list(readAndProcessFile(file_path))
            selection_sort(integers)
            writeFile(integers, BASE+"/data/argument_data_result/"+name+"_result.txt")
        else:
            print("please provide a correct path to a file...")



