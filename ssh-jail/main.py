# Import libraries
import time
import function
import sys
import logger
import config

if __name__ == "__main__":
    debug = "-d" in sys.argv
    try:
        while True:
            # Run main code on loop
            function.function(debug, config)

            # Sleep for x minutes
            if debug: logger.debug(f"Sleeping for {config.sleep_time}m")
            time.sleep(60 * config.sleep_time)
    except KeyboardInterrupt:
        print("Bye!")
        exit()
