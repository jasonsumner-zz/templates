#!/usr/bin/python

''' Python template for quick reference written by Jason Sumner
Example output:
./python.py 

'''

# Import Modules
import argparse, logging, os.path

# Define Variable
filename="python.py"
filenameBackup=filename + '.bak'
logFilename=filename + '.log'
logLevel=logging.DEBUG #Log Levels: logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL, logging.DEBUG
screenLevel="debug" #Print to Screen Levels: info, warning, error, critical, debug

# Configure logging module
logging.basicConfig(filename=logFilename, level=logLevel, format="%(asctime)s, %(levelname)s, %(message)s")

# Argument Parsing and Help Component
parser = argparse.ArgumentParser(description='A quick python template for reference when writing new scripts.')
parser.add_argument('-s', '--string', action="store", dest="stringValue", type=str, required=True,
	help="The string that you want written to the files.")
parser.add_argument('-l', '--loop', action="store", dest="loopNumber", type=int, required=True,
	help="The number of times you want this script to write to file.")
args = parser.parse_args()

# Function
def outputHandler(outputType,outputMessage):
	if outputType == "info":
		logging.info(outputMessage)
		if screenLevel == "info" or screenLevel == "warning" or screenLevel == "error" or screenLevel == "critical" or screenLevel == "debug":
			print outputMessage
	elif outputType == "warning":
		logging.warning(outputMessage)
		if screenLevel == "warning" or screenLevel == "error" or screenLevel == "critical" or screenLevel == "debug":
			print "WARNING: " + outputMessage
	elif outputType == "error":
		logging.error(outputMessage)
		if screenLevel == "error" or screenLevel == "critical" or screenLevel == "debug":
			print "ERROR: " + outputMessage
	elif outputType == "critical":
		logging.critical(outputMessage)
		if screenLevel == "critical" or screenLevel == "debug":
			print "CRITICAL: " + outputMessage
	elif outputType == "debug":
		logging.debug(outputMessage)
		if screenLevel == "debug":
			print "DEBUG: " + outputMessage
	else:
		print "Please specify one of the following log entry types: INFO, WARNING, ERROR, CRITICAL, or DEBUG,"

def main():
	outputHandler("debug","Execution of main() has started.")

	# Verify if a backup of this file exists
	if os.path.exists(filenameBackup):
		outputHandler("info","A backup of the file '" + filenameBackup + "'exists.")
	else:
		outputHandler("warning","A backup of the file '" + filenameBackup + "' doest not exist.")



	#print args.stringValue
	#print args.loopNumber

# Start code execution if script is not executed and not imported as a
if __name__ == "__main__":
    main()