## CIS3330-CASA6-Reading-a-Plain-File

In this assignment you are asked to open a file, read its content and search information to retrieve it. 

* The file you are going to read is the a comma separated values file named `'big-mac-full-index.csv'`
* To read the file you, use the built-in function `open()` as shown in chapter 7.4 from Severance(2019)
  + The file to open is included in the code repository. Therefore your filename should be `./big-mac-full-index.csv`
  + In this CASA assignment you are not allowed to use the CSV, Pandas or any other external modules.
* After you read the file, you are asked to traverse through all the lines of the file and print out lines that include the word `''`
  + A useful way to identify a word in a text line is `if "word" in line_variable"