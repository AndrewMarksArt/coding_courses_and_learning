"""
Logging --> captures and records events while app is running
-- useful debugging feature --> not always practical to debug in real time
-- easy to categorize events
-- provides audit trail of program execution order
-- highly customizable

import logging
.debug("debug-level msg") --> diagnostic info
.info("info-level msg") --> general info about program execution results
.warning("warning-level msg") --> something unexpected
.error("error-level msg") --> unable to perform a specific task
.critical("critical-level msg") --> serious error, program might not be able to continue
"""

import logging

extData = {
    "user": "andrew"
}


def anotherFunc():
    logging.debug("This is a debug-level message", extra=extData)


def main():
    # TODO: use basicConfig to configure logging
    fmtstr = "User:%(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
    datestr = "%m/%d/%Y %I:%M:%S %p"

    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        filemode="w",
                        format=fmtstr,
                        datefmt=datestr)

    # TODO: tryout each of the log levels
    logging.debug("This is a debug message", extra=extData)
    logging.info("This is an info message", extra=extData)
    logging.warning("This is a warning message", extra=extData)
    logging.error("This is a error message", extra=extData)
    logging.critical("This is a critical message", extra=extData)

    # TODO: output formatted strings to the log
    logging.info("here is a {} variable and an int:".format("string", 10), extra=extData)

    # TODO: custom formatting specification
    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)
    anotherFunc()


if __name__ == "__main__":
    main()
