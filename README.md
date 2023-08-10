# data_1202_final_project
This repository was created for the final project of "Data Analysis Tools Analytics"

### Dataset details.
- This datasets is of all the recent movies and series relased with their ratings, certificates, etc. and also a different dataset contains extra details about those movies like actor, plot, runtime, etc.
- The reason behind selecting this dataset is that the semester break was coming and I was wandering what movies or shows I should watch. So, to decide this I tried doing something interesting and tried to implement my learning throughout the course on a simple dataset.
- This was done for my personal use and not as any big issue solver coding. Fun learning!


### Repository content.
- This repository has 2 main folders being datasets and code.
    -  datasets: this folder before transformation and after transformation excel files of dataset.
    -  code: this contains the python code file and code_file.md file which contains pyton code which is easy to see.

### Code steps.
- Initially, I check the dataset in the excel files itself.
- First step as it should be was to import libraries which are needed for this pandas was the obvious choice. As it facilitates us with the functions which makes it easy to extract data and use it further.
- Second step will be to extract data from excel file to a pandas dataframe so we can perform transformation onto the data easily.
  - For transformation first I checked the datatypes of all the columns of both the dataframes which I created in first step.
  - Then removed the rows which had empth cells or say 'nan' values
- Latly I performed join on both the dataframes so I can get all the data about movie ratings and its details togather in one dataframe.
- Finaly, to store this newly created dataframe with all the data I exported to a new excel file which contains all the columns of both dataframes.

### Learinigs.
- Doing this simple make me understand that how good python pandas library is and how easy it makes data transformation.
- Initial step which one should always perform before starting any transformation is checking datatype of all columns.
- I have learned many small things about using python for data manipulation and will definetly research mode about this processes and improve myself. 
