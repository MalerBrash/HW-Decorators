import csv
import datetime


def logger(path_logfile):
    def _logger(function):
        def log_function(*args, **kwargs):
            start_time = datetime.datetime.now()
            name_func = function.__name__
            result = function(*args, **kwargs)
            print(args)
            print(kwargs)
            with open(path_logfile, 'a', newline='') as f:
                writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                writer.writerow([start_time, name_func, args, kwargs, result])
            return result
        return log_function
    return _logger
