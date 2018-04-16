# Scrape BuzzFeed's NYPD case database
### What does this do?
This code will scrape all text and PDF data from BuzzFeed's database of NYPD disciplinary case files between 2011 and 2015.

### What data will I get?
BuzzFeed has already attempted to extract raw text data from each PDF. This scraper will extract that text data to individual files in the `txt` folder for easy analysis. If you want to analyze the raw case file PDFs yourself, they will be stored in the folder `pdf`.

### How is the data identified?
The file `nypd-discipline.csv` comes from BuzzFeed and contains the names of each officer, their number, case ID,  and a URL to their case file. Each case file has its own numerical identifier (found at the end of the URL), which I've used as the filename for the scraped text and PDF data. Please reference that CSV file if you need to match a scraped file to a specific officer.

### How do I configure and run the scraper?
Install the requirements using `pip install -r requirements.txt`.

Since the scraper uses Selenium to extract the text data, you will need a web driver of some kind. The current configuration **assumes you have Firefox installed, as well as geckodriver downloaded and placed in a folder `/driver`.** If not, you will need to download Firefox and geckodriver, or you will need to configure the Python script to use a different web driver. See [here](https://www.seleniumhq.org/download/) for links to web drivers for different browsers.

Once you've installed requirements, Firefox, and geckodriver (or your preferred browser and driver), you can run `scrape.py` to download. The script will take some time to run, as there are over 2,000 case files to download.

### Where can I learn more?
Learn more about this project @ [buzzfeed.com/nypddatabase](buzzfeed.com/nypddatabase).
