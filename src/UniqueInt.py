#!/usr/bin/python3

"""
entry point of the main program
"""
import time
from utils import selection_sort, readAndProcessFile, writeFile, runtime_log, BASE
import os
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        input_directory = BASE+"/data/sample_data_input"
        output_directory = BASE+"/data/sample_data_result"
        for file in os.listdir(input_directory):
            start_time = time.time()
            file_path = os.path.join(input_directory, file)
            integers = list(readAndProcessFile(file_path))
            selection_sort(integers)
            writeFile(integers, output_directory+"/"+file+"_result.txt")
            end_time = time.time()
            RunTime = end_time-start_time
            runtime_log(runtime=RunTime, file=file)
            print(f"Memory Usage and runtime for file {file}:\nmem_Usage: #TODO\nRun_Time: {RunTime*1000} milli secs\n")
        print("DONE..")
    else:
        file_path = sys.argv[1]
        if os.path.isfile(file_path):
            start_time = time.time()
            file = os.path.basename(file_path)
            integers = list(readAndProcessFile(file_path))
            selection_sort(integers)
            writeFile(integers, BASE+"/data/argument_data_result/"+file+"_result.txt")
            end_time = time.time()
            RunTime = end_time-start_time
            runtime_log(runtime=RunTime, file=file, mode="w")
        else:
            print("please provide a correct path to a file...")



