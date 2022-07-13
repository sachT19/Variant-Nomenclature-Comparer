#Sachleen Tuteja, April 2022, HGVS Nomenclature Comparison

import difflib

with open('/Users/sachleentuteja/Documents/HGVS Nomenclature Python/AnnovarColumn.txt') as file1:
    file1_annotate = file1.readlines() #read each line from the input file individually

with open('/Users/sachleentuteja/Documents/HGVS Nomenclature Python/VEPColumn.txt') as file2:
    file2_annotate = file2.readlines() #read each line from the input file individually

comparison = difflib.HtmlDiff().make_file(file1_annotate, file2_annotate, 'Annovar', 'VEP') #creating HTML file and data table that will compare the Annovar and VEP Nomenclature
comparison_results = open('/Users/sachleentuteja/Desktop/lurie/comparison.html', 'w')
comparison_results.write(comparison) #writing that HTML file with data from comparison
comparison_results.close()

 
