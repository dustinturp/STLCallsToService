# Description

[STLPD](http://www.slmpd.org/Crimereports.shtml) monthly reports combined into single year reports.

The included python script can be used to merge all data into a single csv file.


CRS info: EPSG:102696, NAD_1983_StatePlane_Missouri_East_FIPS_2401_Feet
encoding: utf-8

# Summary of calls to service

|Year|January|February|March|April|May|June|July|August|September|October|November|December|total|
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|2008|5,516|4,468|5,427|5,899|5,935|5,948|6,348|6,416|6,612|5,962|5,260|4,820|68,410|
|2009|4,718|4,443|5,127|4,961|5,373|5,380|5,816|5,930|5,633|5,591|5,367|4,677|63,046|
|2010|4,179|3,448|4,777|5,096|4,927|4,869|5,488|5,460|5,245|5,341|4,689|4,310|57,830|
|2011|4,163|3,510|4,581|4,945|5,191|5,311|5,211|5,005|4,468|4,684|4,259|3,919|55,247|
|2012|3,671|3,354|4,367|4,905|4,975|4,853|5,139|5,038|4,437|4,571|4,096|3,981|53,887|
|2013|4,421|3,408|4,010|4,344|4,891|4,752|4,977|4,804|4,771|4,117|3,850|3,625|51,970|
|2014|3,280|2,932|3,697|3,997|4,196|4,235|4,383|4,337|4,481|4,242|3,976|4,120|47,876|
|2015|3,983|3,188|4,447|4,776|4,456|4,434|4,826|4,709|4,509|4,380|3,853|3,674|51,235|
|2016|3,900|3,408|4,011|3,999|4,430|3,339|4,554|4,982|4,387|4,586|3,952|3,879|50,426|
|2017|3,936|3,548|3,981|3,969|4,548|4,210|4,463|4,503|3,756|4,462|3,847|3,763|48,986|
|2018|3,826|3,185|3,629|3,735|4,013|4,282|4,257|4,402|4,096|4,087|3,559|3,672|46,742|
|2019|3,527|3,198|3,605|4,064|4,133|4,549|4,701|4,624|4,679|4,283|3,803|3,735|48,901|
|2020|3,943|3,493|3,417|6,028|3,309|4,371|4,101|4,193|4,024|3,693|3,843|3,319|47,734|

---
### MISC Notes

* Additional columns are present in 2017May.

---

## Using the Python Script to join the CSV files.

### Requirements
    - Python 3
    - Pandas library (pip install pandas)

## Instructions

1. Clone the repo
`git clone https://github.com/dustinturp/STLCallsToService.git`

2. Use the script. (command may look different depending on how you installed Python)
Navigate to the folder containing the csv files via terminal.

`python3 pandas_join_files.py` 

3. Enter a name for the combined file.

## Future Improvements

* Charts
* CLI prompts
* Error handling 


## Source
[Monthly reports](https://www.slmpd.org/Crimereports.shtml)
For more information about the St. Louis PD Crime stats check their [FAQ](http://www.slmpd.org/Crime/CrimeDataFrequentlyAskedQuestions.pdf).


