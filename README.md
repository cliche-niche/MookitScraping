## Working
To scrape the page saved in [page.html](./page.html), run this in the terminal:
```bash
python3 scrape.py --number 4
```
The default number of lectures to scrape is 4 but it can be changed by replacing the `4` in above snippet by the desired number.


## Description of Files
+ [scrape.py](./scrape.py): Contains the code to scrape the page saved in [page.html](page.html).
+ [data.csv](./data.csv): The CSV file provided has 6 of the latest lectures in my ESC201A course, and [this file](lecsUploaded.PNG) has a screenshot of the latest lecs in the same course for verification.
+ [login.py](./login.py): This file and [chromedriver.exe](./chromedriver.exe) are not required for scraping, but I had to write them to log-in to [HelloIITK](https://hello.iitk.ac.in/index.php/user/login) and get the page myself using selenium.
I used [login.py](./login.py) to save the content of the course page to [page.html](page.html).


## References
+ https://realpython.com/python-web-scraping-practical-introduction/ (Introduced me to scraping)
+ https://kazuar.github.io/scraping-tutorial/ (For log-in)
+ Official documentations of [CSV](https://docs.python.org/3/library/csv.html) and [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
+ Stackoverflow, which helped me realise that Selenium is more convenient for pages that are rendered using javascript, among a lot of other things.