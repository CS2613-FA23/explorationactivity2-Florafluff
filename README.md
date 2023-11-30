### 1. Which package/library does the sample program demonstrate?
- The sample program demonstrates the python library [matplotlib](https://matplotlib.org/stable/index.html) alongside [pandas](https://pandas.pydata.org/docs/).

### 2. How does someone run your program?
- To run the program first type ``pip install pandas``, ``pip install matplotlib``, and ``pip install jupyterlab`` into the terminal (jupyterlab might take awhile).
- Next type ``jupyter lab`` into the terminal, this should open a tab in your web browser that looks like this: 
![this](https://cdn.discordapp.com/attachments/319987558509576201/1179604286049620000/image.png?ex=657a6319&is=6567ee19&hm=81532ab6df9b07f1d2bdfd73a72338089e81aed8b381989e193970e7dafde8fd&)
- You need to click on the Python 3 button under Console right here:

    ![this](https://cdn.discordapp.com/attachments/319987558509576201/1179604679785726063/image.png?ex=657a6377&is=6567ee77&hm=ae2163c3cc94ffd6085cfca5c12a494f4e777efe1d184e8efafd9400aee23c25&)
- Now you need to type ``run SpreadSheetEditor`` in the input bar at the bottom of the console, then hit **SHIFT and ENTER at the same time** to run the program
- From here just follow what the program tells you to do
- if you get an ``ModuleNotFoundError: No module named 'openpyxl'`` error when exporting to Excel then run the command ``pip install openpyx1``

### 3. What purpose does your program serve?
- The program allows you to edit a ``.csv`` spreadsheet.
- You can add and remove columns and rows, changing the data inside them as you do.
- The program allows you to output your spreadsheet as a ``.csv`` (command seperated values) or a ``.xlsx`` (Excel document).
- It also allows you to plot your spreadsheet onto different types of graphs

### 4. What would be some sample input/output?
- The program takes in a ``.csv`` file with at least 2 rows and 2 columns in it with the first row being the column names and the first column being the row names.
- **The first cell (0,0) needs to be named** ``rowName``. The file should also only contain numerical data aside from the first row and first column (those being the names).
- the file ``ExampleSpreadsheet.csv`` is an example of a valid input.
- Some other valid inputs would be:

    ![ex](https://cdn.discordapp.com/attachments/319987558509576201/1179609565671727145/image.png?ex=657a6804&is=6567f304&hm=7716e5596b3838e7dbc4987b11a6aa651ff3593077f29f6de481692369826adf&)

    ![ex](https://cdn.discordapp.com/attachments/319987558509576201/1179609716305965167/image.png?ex=657a6828&is=6567f328&hm=8e5e9e028b820e21adce2508dc56c6155479ca34666783a44548f83b58025758&)

- Example of a bar graph output:

    ![ex](https://cdn.discordapp.com/attachments/319987558509576201/1179610210957017088/image.png?ex=657a689e&is=6567f39e&hm=90a0eb81e2a296739c4cc1c6255f2d1e2f49d742c6681b0420b3b59ca0b69d79&)

- Example of spreadsheet exported to Excel:

    ![ex](https://cdn.discordapp.com/attachments/319987558509576201/1179611026015133754/image.png?ex=657a6960&is=6567f460&hm=37d02d80997821891181af1c4fe7234248a0c4debd715772b6061e8eb9c8c4b0&)