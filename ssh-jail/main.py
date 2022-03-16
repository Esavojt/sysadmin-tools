# Import libraries
import time
import function

sleep_minutes = 0

if __name__ == "__main__":
    try:
        while True:
            # Run main code on loop
            function.function()

            # Sleep for x minutes
            time.sleep(1)
    except KeyboardInterrupt:
        print("Bye!")
        exit()
