
import threading
import time


def log_reader(file_path: str, log_queue: list, lock):
  """
    Thread function to read new lines added to the log...
  """
  print('hello 1')
  with open(file_path, mode='r') as log_file:
    try:
      log_file.seek(0, 2)

      while True:
        line = log_file.readline()
        if line:
          with lock:
            log_queue.append(line)
        else:
          time.sleep(1)
          

    except FileExistsError as e:
      print(e)

def error_monitor(log_queue: list, lock) -> None:
  print('hello 2')

  """Thread function to monitor queue for "ERROR" in log lines"""
  while True:
  
    if log_queue:
      with lock:
        line: str = log_queue.pop(0)
    else:
      line = None
    if line and "ERROR" in line:
      print(f"ERROR detected: {line}")
    else:
      time.sleep(1)

def main():
  try:  
    server_log = 'server.log'
    log_queue = []
    lock = threading.Lock()
    reader_thread = threading.Thread(target=log_reader, args=(server_log, log_queue, lock))
    error_thread = threading.Thread(target=error_monitor, args=(log_queue, lock))
    reader_thread.start()
    error_thread.start()
    reader_thread.join()
    error_thread.join()
  except KeyboardInterrupt:
    print('Exiting...')



if __name__ == '__main__':
  main()

import multiprocessing

