import win32evtlog
import pandas as pd

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# System Logs
def system():
	h = win32evtlog.OpenEventLog(None, 'System')

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print('\n Number of records : ',len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = 'Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name'
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ';' + records[i].SourceName + ';' + records[i].TimeWritten.Format() + ';' + str(records[i].EventID) + ';' + str(records[i].RecordNumber) + ';' + str(records[i].EventType) + ';' + str(records[i].EventCategory) + ';' + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
	print(df)
	df.to_csv('system_log.csv', header=False, index=False)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# Security Logs
def security():
	h = win32evtlog.OpenEventLog(None, 'Security')

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print('\n Number of records : ',len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = 'Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name'
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ';' + records[i].SourceName + ';' + records[i].TimeWritten.Format() + ';' + str(records[i].EventID) + ';' + str(records[i].RecordNumber) + ';' + str(records[i].EventType) + ';' + str(records[i].EventCategory) + ';' + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
	print(df)
	df.to_csv('security_log.csv', header=False, index=False)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# Application Logs
def application():
	h = win32evtlog.OpenEventLog(None, 'Application')

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print('\n Number of records : ',len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = 'Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name'
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ';' + records[i].SourceName + ';' + records[i].TimeWritten.Format() + ';' + str(records[i].EventID) + ';' + str(records[i].RecordNumber) + ';' + str(records[i].EventType) + ';' + str(records[i].EventCategory) + ';' + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
	print(df)
	df.to_csv('application_log.csv', header=False, index=False)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
'''
# General Logs
def general():
	h = win32evtlog.OpenEventLog(None, 'General Logging')

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print('\n Number of records : ',len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = 'Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name'
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ';' + records[i].SourceName + ';' + records[i].TimeWritten.Format() + ';' + str(records[i].EventID) + ';' + str(records[i].RecordNumber) + ';' + str(records[i].EventType) + ';' + str(records[i].EventCategory) + ';' + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
	print(df)
	df.to_csv('general_log.csv', header=False, index=False)
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# Setup Logs
def setup():
	h = win32evtlog.OpenEventLog(None, 'Setup')

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print('\n Number of records : ',len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = 'Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name'
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ';' + records[i].SourceName + ';' + records[i].TimeWritten.Format() + ';' + str(records[i].EventID) + ';' + str(records[i].RecordNumber) + ';' + str(records[i].EventType) + ';' + str(records[i].EventCategory) + ';' + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
	print(df)
	df.to_csv('setup_log.csv', header=False, index=False)
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

# Hardware Events Logs
def hardware_events():
	h = win32evtlog.OpenEventLog(None, 'HardwareEvents')

	flags = win32evtlog.EVENTLOG_BACKWARDS_READ|win32evtlog.EVENTLOG_SEQUENTIAL_READ
	records = win32evtlog.ReadEventLog(h, flags, 0)
	print('\n Number of records : ',len(records))

	row, header = [None]*len(records), [None]*len(records)
	fi = []

	header[0] = 'Index;Source Name;Time Written;Event ID;Record Number;Event Type;Event Category;Computer Name'
	fi.append(header[0].split(';'))
	
	for i in range(len(records)):
		a = i + 1
		row[i] = str(a) + ';' + records[i].SourceName + ';' + records[i].TimeWritten.Format() + ';' + str(records[i].EventID) + ';' + str(records[i].RecordNumber) + ';' + str(records[i].EventType) + ';' + str(records[i].EventCategory) + ';' + records[i].ComputerName
		fi.append(row[i].split(';'))
		df = pd.DataFrame(fi)
	print(df)
	df.to_csv('hardware_events_log.csv', header=False, index=False)
'''
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

print('\n\n Security Logs \n')
security()
print('-'* 100)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

print('\n\n System Logs \n')
system()
print('-'* 100)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

print('\n Application Logs \n')
application()

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
'''
print('\n General Logs \n')
general()
print('-'* 100)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

print('\n Setup Logs \n')
setup()
print('-'* 100)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

print('\n Hardware Events Logs \n')
hardware_events()
print('-'* 100)
'''