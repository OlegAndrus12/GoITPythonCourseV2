"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exist

In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)


Character	Meaning
'r'	open for reading (default)
'w'	open for writing, truncating the file first
'x'	create a new file and open it for writing
'a'	open for writing, appending to the end of the file if it exists
'b'	binary mode
't'	text mode (default)
'+'	open a disk file for updating (reading and writing)


encoding: Windows, ASCII, UTF-16
UTF-8 is the dominant encoding for the World Wide Web (and internet technologies), 
accounting for 98.2% of all web pages, 99.0% of the top 10,000 pages, and up to 100% for many languages, 
as of 2024.[9] Virtually all countries and languages have 95% or more use of UTF-8 encodings on the web.

"""


file = open("test.txt", "w", encoding="utf-8")
file.write("Hello world!\n")
file.write("Hello Ukraine!\n")
file.writelines(["Hi Bob!", "Hi Dima!", "Test", "ups"])
file.close()

file = open("test.txt", "r", encoding="utf-8")
# !!!!! size parameter
# result = file.read()
# result = file.readline()
result = file.readlines()
print(result)
file.close()
