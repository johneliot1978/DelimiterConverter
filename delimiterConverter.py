# Description: python command line script to convert a delimited file to another delimited format
import pandas as pd
import sys
import os

def convert_delimited_file(input_file, input_delimiter, output_delimiter):
    # Check if the input file exists
    if not os.path.isfile(input_file):
        print(f"File {input_file} does not exist.")
        return
    
    # Load the delimited file with the specified delimiter and ensure all fields are treated as strings
    try:
        df = pd.read_csv(input_file, dtype=str, encoding='utf-8', sep=input_delimiter)
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return
    
    # Construct the output file name by replacing the input delimiter with the output delimiter
    base, _ = os.path.splitext(input_file)
    output_file = f"{base}_converted.txt"
    
    # Export the DataFrame to a TSV file with the specified output delimiter and UTF-8 encoding
    try:
        df.to_csv(output_file, sep=output_delimiter, index=False, encoding='utf-8')
        print(f"File successfully converted to {output_file}")
    except Exception as e:
        print(f"Error writing to {output_file}: {e}")

if __name__ == "__main__":
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python convert_to_tsv.py <input_file>")
    else:
        input_file = sys.argv[1]
        
        # Prompt the user for input delimiter and output delimiter
        input_delimiter = input("Enter the delimiter used in the input file (e.g., ',' for comma): ")
        output_delimiter = input("Enter the delimiter you want for the output file (e.g.  | or tab or something else): ")
        
        convert_delimited_file(input_file, input_delimiter, output_delimiter)
