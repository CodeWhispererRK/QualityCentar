# backend/database.py
# читање на sample CSV датотеки за QualityCentar
import csv
import os
DATA_DIR = os.path.join(os.path.dirname(__file__),'../data')
def read_csv(filename):
  filepath = os.path.join(DATA_DIR, filename) with open(filepath, newline='',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    return (row for row in reader)
# пример за користење 
    if __name__ == "__main__": companies = 
    read_csv('sample_companies.csv')
    print("Companies loaded:", companies)
