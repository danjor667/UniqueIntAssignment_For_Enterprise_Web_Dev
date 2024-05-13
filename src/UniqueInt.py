"""
program
"""
from utils import generator_sort, read_file
import sys


if __name__ == "__main__":
    if len(sys.argv) < 2:
        input_file = "sample_01.txt"
        input_file_path = f"../data/sample_data_input/{input_file}"
        output_file_path = f"../data/sample_data_result/{input_file}_result.txt"
        with open(output_file_path, "w") as f:
            for ele in generator_sort(read_file(input_file_path)):
                f.write(str(ele)+'\n')




