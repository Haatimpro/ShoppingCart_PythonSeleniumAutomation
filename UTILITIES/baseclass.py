import inspect

import pytest
import logging
import  inspect

#note: base class is created to avoide using decorator: @pytest.mark.usefixtures("setup") on every testcase/class we create
#base class contains a fixture, which intern contians basic setup like launching browser, navigating to url, driver object creation
@pytest.mark.usefixtures("setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]  # Extract filename
        logger = logging.getLogger(loggerName)
        Log_File = logging.FileHandler("logfile.log")  #paste the cutomized path if required
        #To display only current test run log details use below Log_File, comment above Log_File.
        #Log_File = logging.FileHandler("logfile.log", mode='w') # Incase of multiple data set it will fail, only last dataset log details will be displayed
        formatter = logging.Formatter("%(asctime)s : %(levelname)s: %(name)s : %(message)s")
        Log_File.setFormatter(formatter)
        if (logger.hasHandlers()):  #to avoide duplicate logging of 2nd test data
            logger.handlers.clear()
        logger.addHandler(Log_File)
        logger.setLevel(logging.DEBUG)
        #log levels in orderwise
        # logger.debug("A debug statement is executed")
        # logger.info("Information statements")
        # logger.warning("Something is in warning mode")
        # logger.error("A major errror has happened")
        # logger.critical("critical issue")
        return logger