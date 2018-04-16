# Scrape Buzzfeed's NYPD case database
### What does this do?
This code will scrape all text and PDF data from Buzzfeed's database of NYPD disciplinary case files between 2011 and 2015.

### What data will I get?
Buzzfeed has attempted to extract raw text data from each PDF. This scraper will extract that data to individual text files in the `txt` folder for easy analysis. If you want to analyze the raw case file PDFs yourself, they will be stored in the folder `pdf`.

### How is the data identified?
The file `nypd-discipline.csv` comes from Buzzfeed and contains the names of each officer, their number, case ID,  and a URL to their case file. Each case file has it's own numerical identifier (found at the end of the URL), which I've used as the filename for the scraped text and PDF data. Please reference that CSV file if you need to match a scraped file to a specific officer.

### Where can I learn more?
Learn more about this project @ [buzzfeed.com/nypddatabase](buzzfeed.com/nypddatabase).
