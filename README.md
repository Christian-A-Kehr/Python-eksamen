Python eksamen

Project name: Bilhandler
file_name: Eksamen_car.ipynb

Short description: 

	Using web scraping collect date and write data to a csv fil.
	afterwards manages the data by creating a dataframe obj using panda
	Clean data in dataframe, the use date for clustering and classification

List of used technologies:

	- Exceptions (code)
	- Plotting (Notebook decision tree)
	- Numpy (not sure if is needed) <<<<<<
	- DateTime (used for speed test in modules/web_scraping and file writing)
	- Requests (modules/web_scraping getdata())
	- webscraping gearly (modules/web_scraping)
	- clustering (code/notebook)
	- classification (notebook)
	

Installation guide (if any libraries need to be installed):

	- all libraies inluced in teacher/Thomas notebook => clone project to notebook

User guide (how to run the program):
	
	- open Eksamen_car.ipynb in dockernotebook with jupyter
	- run kernel (will webscrab something but 3 csv file will be provided if you don't wish to webscrap: df = pd.read_csv(file_name) in cell 4 line 2 change file_name to name of the csv you want to use)
	alternativ:
	- if user wishes to see webscraping 3 variables is providing for cartype: ( 1. small_webscrap = 'alfa-romeo', 2. medium_name =  'citroen' , 3. large_webscrap = 'mercedes') 
		just set car_name in cell 2 line 5 (time needed varies).
	obs: any cartype (BMW, Audi etc) can be used but will yield very different results (do to HTML structor and bad user input on site) 
	- Restart the kennel if you wish and the notebook will import moduels to display some data and rest is excuted in cells in the notebook) 

Status (What has been done (and if anything: what was not done)):

	- webscraping (done)
	- filehandling (done)
	- clean up data (done, wished i had some other data to work with tho)
	- clustering (done) conclusion dependts on the car_typ, but eksample is provied for Citroen	
	- classification/dicision tree (not the best data for it tho)
	- mulititreating (not implemtet done)  
	

List of Challenges you have set up for your self (The things in your project you want to highlight):

	- proper webscraping (multiple obj acrossed across multiple url, solution to next pages problem) 
	- clustering and/or classification (decision Tree) (had a hard time gasping it) 