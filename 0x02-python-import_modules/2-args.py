#!/usr/bin/python3
if __name__ == "__main__":
    import sys

	argv_count = len(sys.argv) - 1  # Subtract 1 for the script name

	# Print the number of arguments
	if argv_count == 0:
		print("{} arguments.".format(argv_count))
	elif argv_count == 1:
		print("{} argument:".format(argv_count))
		print("{}: {}".format(1, sys.argv[1]))
	else:
		print("{} arguments:".format(argv_count))

		# Use a for loop to iterate through the arguments
		for index in range(1, argv_count + 1):
			print("{}: {}".format(index, sys.argv[index]))
