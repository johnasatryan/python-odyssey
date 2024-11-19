# Multiprocessing Task – Large-Scale Data Aggregation
# You are working with a large dataset stored in multiple CSV files. 
# Each file contains transaction data from different regions. 
# Your task is to process these files concurrently and aggregate the data into a summary report 
# that includes the total number of transactions and the sum of transaction amounts for each file.
# Use the multiprocessing library to create separate processes for each CSV file.
# Each process should read its assigned file, sum the transaction amounts, and count the number of transactions.
# Aggregate the results from all processes and print the final summary.


import csv
import multiprocessing
import time

def process_file(file_path, result_queue):
  try:
    total_transactions = 0
    total_amount = 0.0

    with open(file_path, mode='r') as file:
      reader = csv.DictReader(file)

      for item in reader:
        total_transactions += 1
        total_amount += float(item['Amount'])
      result_queue.put((file_path, total_transactions, total_amount))
  except Exception:
    print(f"Error in processing: {file}")

def aggregate_results(result_queue, num_files):
  final_summary = {}
  for _ in range(num_files):
    file_path, total_transactions, total_amount = result_queue.get()
    final_summary[file_path] = {'total_transactions' : total_transactions, 'total_amount': total_amount}
  return final_summary
  
def main():
  csv_files = ['transaction_region1.csv', 'transaction_region2.csv', 'transaction_region3.csv']

  result_queue = multiprocessing.Queue()

  processes = []

  for csv_file in csv_files:
    process = multiprocessing.Process(target=process_file, args=(csv_file, result_queue))
    processes.append(process)
    process.start()
  
  for process in processes:
    process.join()

  final_result = aggregate_results(result_queue, len(csv_files))
  print("Summary result:")
  for file, data in final_result.items():
    print(f"File: {file}")
    print(f"Total: {data}")


if __name__ == '__main__':
  main()

