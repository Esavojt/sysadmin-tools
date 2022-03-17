# Import libraries
import time
import function
import sys
import logger

sleep_minutes = 1

if __name__ == "__main__":
    debug = "-d" in sys.argv
    try:
        while True:
            # Run main code on loop
            function.function(debug)

            # Sleep for x minutes
            if debug: logger.debug(f"Sleeping for {sleep_minutes}m")
            time.sleep(60 * sleep_minutes)
    except KeyboardInterrupt:
        print("Bye!")
        exit()
