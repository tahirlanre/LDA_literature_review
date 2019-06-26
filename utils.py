import numpy as np
import os

import PyPDF2


def getPageCount(pdf_file):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    pages = pdfReader.numPages
    return pages


def extractData(pdf_file, page):
    pdfFileObj = open(pdf_file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
    pageObj = pdfReader.getPage(page)
    data = pageObj.extractText()
    return data


def x():
    titles = []
    word_counts = []
    directory = os.fsencode('data/papers_pdf')
    csv = 'data/papers.csv'

    import pdb; pdb.set_trace()
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".pdf"):
            pdfFile = open('data/papers_pdf/' + filename, 'rb')
            inputPdf = PyPDF2.PdfFileReader(pdfFile)
            # get the word count in the pdf file
            totalWords = 0
            numPages = getPageCount('data/papers_pdf/' + filename)
            for i in range(numPages):
                text = extractData('data/papers_pdf/' + filename, i)
                totalWords += len(text.split())

            titles.append(inputPdf.getDocumentInfo().title)
            word_counts.append(totalWords)
            print(totalWords)
            print(inputPdf.getDocumentInfo().title)
        else:
            continue

    papers_info = {'title': titles, 'word_count': word_counts}

    print(papers_info)


x()
