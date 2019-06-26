import numpy as np
import os

from tika import parser
import PyPDF2

def getPageCount(pdf_file):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pages = pdfReader.numPages
	return pages

def extractData(pdf_file, page):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(page)
	data = pageObj.extractText()
	return data

def x():
    papers = []
    titles = []
    word_counts = []
    directory = os.fsencode('data/papers_pdf')
    csv = 'data/papers.csv'
    
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".pdf"):
            pdfFile = open('data/papers_pdf/'+filename, 'rb')
            
    	# get the word count in the pdf file
    	totalWords = 0
    	numPages = getPageageCount(pdfFile)
    	for i in range(numPages):
    		text = extractData(pdfFile, i)
    		totalWords+=getWordCount(text)
        
        titles.append()
        
            
	print (totalWords)
        
    return papers

x()