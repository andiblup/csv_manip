# csv_manip
### Installation 
> "Into many Columns"
1. Download or clone this repository
  * If downloaded unzip the package.
2. Open the In mehrere Spalten folder, here is where you will drop your .csv file
3. IMPORTANT: The default file name has to be data.csv and the product will be called endProduct.csv
  * You could change theese names in the lines 8 and p of the converter.py file, but it wont change anything in the .exe programm. You would have to run everything with the python command in the terminal instead of doubleklick the .exe programm.
* If you use the .exe and the default names
  1. Copie the file you want to transform into the "dist" folder
  2. Doubleclick the converter.exe
* If you dont use the exe
  1. Make sure you have installed at least Python 3.8 and added it to the path variables
  2. Copie the file you want to transform into the SAME folder with the converter.py
  3. Open this folder with the terminal
  4. Then use the command: `python converter.py` or `python3 converter.py`

> "Into a single column" <br>
Same procedure as with the column separator




### Description
A script I wrote for a friend for CSV manipulation. It splits the data received from the server, initially separated by commas within a single column, into separate columns for easier editing in Excel. Additionally, there is a script to reformat these divided data back into a single column.
