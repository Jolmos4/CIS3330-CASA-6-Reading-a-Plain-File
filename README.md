## CIS3330-CASA6-Reading-a-Plain-File

In this assignment you are asked to open a file, read its content and search information to retrieve it. 

* The file you are going to read is the a comma separated values file named `'big-mac-full-index.csv'`
* To read the file, use the built-in function `open()` as shown in chapter 7.4 from Severance(2019)
  + The file to open is included in the code repository. Therefore I recommend open the file using the following filename `./big-mac-full-index.csv`
  + In this CASA assignment you are not allowed to use the CSV, Pandas or any other external modules.
* After you read the file, you are asked to traverse through all the lines in the file and print out the lines that include the word `'USA'`
  + To traverse over all the lines of the file I recommend using a for loop similar to the one showed in the first code snippet on chapter 7.4.
  + A useful way to identify a word in a text line is `if "word" in line_variable"
  + In your case you will be looking for the word **'USA'**
  + There is an example on how to search for words in a file on chapter 7.5, but that example uses a function that will help you find the word USA inside the line.
* Your code should find and print out 37 lines with information about the USA.

## Copyright disclosure

* The file `big-mac-full-index` was obtained from [https://github.com/TheEconomist/big-mac-data] (https://github.com/TheEconomist/big-mac-data). The file is protected under the MIT License [https://github.com/TheEconomist/big-mac-data/blob/master/LICENCE](https://github.com/TheEconomist/big-mac-data/blob/master/LICENCE).