# COVID API data dashboard

This is a flask app that visualizes data from the COVID Tracking Project [covidtracking.com].  Data is limited to seven day moving averages new positive tests, hospitalizations, and deaths for the southern United States.

## Installations
To install the flask app, you need to install python 3.8.5 and the python packages in the requirements.txt file.  Install those packages with 'pip install -r requirements.txt'

## Project Motivation
This was put together for the 'Deploy a Data Dashboard' portfolio exercies as part of the Data Science nanodegree program.  I honestly didn't know that I would be interested in building a web site, but I enjoyed the portion of the Software Engineering lesson that I decided to give it a try.  

I chose the COVID Tracking Project just because of the relevancy at the time that I was taking the program and the data was readily available.

I really enjoyed putting this together.  I will definitely try some more projects like this.

## File Descriptions
The files contained in the project include:
- covidweb .py - imports the flask app and runs the program on the localhost
- data .py - contains the logic to download the data from the COVID tracking API [covidtracking.com/data/api]
- routes .py - contains the logic to direct the web page to load the data based on the state selected
- index .html - contains the presentation logic 

## Interaction
The program is launched from a terminal by running 'python covidweb.py'

## Licensing, Authors, Ackwledgements, etc.
As mentioned earlier, data was pulled from the [covidtracking.com] web site.  I also would like to acknowledge the Udacity Data Science nanodegree [program]([https://www.udacity.com/course/data-scientist-nanodegree--nd025) for the inspration and tools provided to create this project.

MIT License is included.
