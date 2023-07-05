## Overview:
This is a python app which allows users to explore bike share data for three US cities: New York, Washington and Chicago

I have used **several websites** to produce the code for the _Bikeshare project_ and have listed them below. 

I have also used Plotly Express to produce two charts. When I run the program from the command line these are opening in separate windows in my browser. 

## Resources

### Data Wrangling:
* https://pythonfordatascienceorg.wordpress.com/recode-data/
* https://www.tutorialsteacher.com/articles/convert-string-to-datetime-in-python?utm_content=cmp-true
* https://stackoverflow.com/questions/14538885/how-to-get-the-index-with-the-key-in-a-dictionary
* https://pythonguides.com/python-format-number-with-commas/
* https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response
* https://www.w3schools.com/python/gloss_python_string_concatenation.asp

### Summary statistics
* [NLargest](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html)
* [Percentage Value Counts](https://www.statology.org/pandas-value_counts-percentage/)

### Charts:
Reources used for producing and editing the charts are:
* Histograms [Plotly Histograms](https://plotly.com/python/histograms/)
* https://plotly.com/python/figure-labels/

## Known Issues
Data for Washington excludes some demongarphic information used in other cities. I have got around this by including a global variable which means some parts of the code don't run if Washington is selected
