# HuaweiPythonTest

Hello! Recently I was selected, through a job interview, to be developing a few simple webscraping aplications in pyhton and I realised there is not much content on the internet to help us out on this market, so I had to bang my head on the wall for two days straight to get around some little and inofensive (that's what I thought) syntax error. Now there's no reason for me to keep this knowloge for my self. I Hope you'll enjoy it :)

This project is separated in three main archives: ex01.py, ex02.py and ex03.py. Each one made to answare one of the three tasks passed over for me.

Those were the questions:

The following questions that require coding should be answered in Python.

  1. Schematize an OO application that receives user authentication information (username and password), access a webpage using the information given, retrieve data from the webpage (HTML table), and export the extracted data (excel file). The schematic should consider class variables and methods, including parameters and outputs.

  2. Develop a script that can access a given URL and return all email addresses found in the page. These pages can be used as examples:
   
     i. https://www.golfclubsatthetribute.com/Default.aspx?p=DynamicModule&pageid=149&ssid=204&vnf=1;

     ii. https://www.thegolfclubatfossilcreek.com/club-contacts;

     iii. https://www.mg-cc.org/club-information/club-contacts;

  3. Develop a script that can list all the content inside a directory and returns a dataframe with the following information:

      a. Name;
    
      b. Extension;
    
      c. Location;
    
      d. Size;
    
      e. Last modification date.
      
# Install

I'm gessing you already have installed git, python and the VS Code extensions or pycharm to run this code. If this is the case, you are only a few steps away from letting it do its magic. If not, first go to the Python in VS Code or Pycharm webpage https://code.visualstudio.com/docs/languages/python // https://www.jetbrains.com/pycharm/ (respectivly), there you'll find instructions on how to prepare your computer to run any python project.

  Now you need (as always) to clone this repository:

    git clone https://github.com/tigulima/HuaweiPythonTest.git
    
  (You might need Git for that: https://git-scm.com/downloads)
    
To complete the tasks, I used the following libs:
  - Selenium

        pip install selenium
    
  - BeatufulSoup4

        pip install BeautifulSoup4
  
  - Requests

        pip install requests
        
  - Pandas

        pip install pandas
  
  - Chrome drivers 
 
        https://sites.google.com/chromium.org/driver/downloads
        

  For Chrome Drivers to work, you need to place the unzipped "chromedrivers.exe" file on the following path: 
            
    C:\Program Files (x86)\ChromeDrivers

# Run

Now, to run the code, open cmd on the directory you cloned this project and type:
  
  For question 1:
  
    python ex01.py

  For question 2:

    python ex02.py
    
  For question 3:
    
    python ex03.py
    
  And Voilah!
  
  If you have any, and I mean ANY question or tips I DARE you to e-mail me at tigulima@gmail.com. I'm waiting for your response, and happy coding!
    
