import logging
import sys

class LogGen:

    @staticmethod
    def loggen():
        # Create a new logger object
        logger = logging.getLogger(__name__) #creates a new logger object that is specific to this current module or script.
        logger.setLevel(logging.INFO)

        # Create a stream handler to capture print statements to console
        
        sh = logging.StreamHandler(sys.stdout) #sys.stdout
        sh.setLevel(logging.INFO)
        sh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        sh.setFormatter(sh_formatter)

        # Create a file handler to write log messages to file
        fh = logging.FileHandler(".\\Logs\\automation.log")
        fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        fh.setFormatter(fh_formatter)

        # Add handlers to logger object
        logger.addHandler(sh)
        logger.addHandler(fh)

        return logger


# import logging
# import sys

# class LogGen:

#     @staticmethod
#     def loggen():
        # Create a new logger object
        # logger = logging.getLogger(__name__)
        # logger.setLevel(logging.INFO)

        # # Create a stream handler to capture print statements to console
        # sh = logging.StreamHandler(sys.stdout)
        # sh.setLevel(logging.INFO)
        # sh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        # sh.setFormatter(sh_formatter)

        # # Create a file handler to write log messages to file
        # fh = logging.FileHandler(".\\Logs\\automation.log")
        # fh_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
        # fh.setFormatter(fh_formatter)

        # # Add handlers to logger object
        # logger.addHandler(sh)
        # logger.addHandler(fh)

        # # Set up the logger to log to the report object's extra_logs attribute
        # handler = ReportHandler()
        # handler.setLevel(logging.INFO)
        # handler.setFormatter(fh_formatter)
        # logger.addHandler(handler)

        # return logger

# report_ctx = None
# class ReportHandler(logging.Handler):
#     def emit(self, record):
#         report = getattr(report_ctx, 'item', None)
#         if report:
#             extra_logs = getattr(report, 'extra_logs', '')
#             extra_logs += self.format(record) + '\n'
#             setattr(report, 'extra_logs', extra_logs)
