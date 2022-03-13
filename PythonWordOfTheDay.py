# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI TO GET WORD OF THE DAY FROM MERRIAM-WEBSTER'S RSS FEED

# In this script, a request is sent to the RSS Feed http://www.merriam-webster.com/wotd/feed/rss2 from which
# RSS output is fetched and parsed

# Importing necessary packages
import feedparser
import tkinter as tk
import tkinter.scrolledtext as sb_text
from tkinter import *
from bs4 import BeautifulSoup

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    quoteLabel = Label(root, text="Word Of The Day : ", bg="tomato4", font=('Comic Sans MS',15,'bold'))
    quoteLabel.grid(row=0, column=0, padx=10, pady=5)

    root.wordText = sb_text.ScrolledText(root, width=30, height=15, bg='azure3')
    root.wordText.grid(row=1, column=0, rowspan=5, columnspan=3, padx=10, pady=5)
    # Making Text Widget uneditable by setting state parameter of config() to DISABLED
    root.wordText.config(state=DISABLED, font = "Calibri 15", wrap="word")

    fetchButton = Button(root, text="GET WORD OF THE DAY", command=getWordOfTheDay)
    fetchButton.grid(row=7, column=0, padx=10, pady=5, columnspan=3)

# Defining the getQuote() to get the quote of the day
def getWordOfTheDay():
    # Parsing the feed from the RSS Feed URL using the parse() method of feedparser URL
    word_output = feedparser.parse('http://www.merriam-webster.com/wotd/feed/rss2')
    # Fetching the details regarding the word of the day from the correct keys.
    # The resulting output which is in HTML Format is converted to text by passing the
    # output to BeautifulSoup() method which is an HTML Parser
    word_output = BeautifulSoup(word_output['entries'][0]['summary'], features="lxml")
    word_of_the_day = word_output.get_text().strip("\n")
    # Enabling the Text Widget by setting state parameter of config() to NORMAL
    root.wordText.config(state=NORMAL)
    # Clearing the entries from the Text Widget using the delete() method
    root.wordText.delete('1.0', END)
    # Displaying the word of the day in the wordText Widget
    root.wordText.insert("end", word_of_the_day)
    # Making Widget uneditable again after the displaying the word of the day
    root.wordText.config(state=DISABLED)

# Creating object of tk class
root = tk.Tk()
# Setting the title, background color, windowsize
# & disabling the resizing property
root.title("PythonWordOfTheDay")
root.geometry("345x370")
root.config(background="tomato4")
root.resizable(False, False)
# Creating the tkinter variables
song = StringVar()
artist = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
