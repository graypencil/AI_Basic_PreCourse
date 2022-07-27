# 미완성

import re
import os

def writeToFile(patent_document, file_name):
    if not os.path.exists("output"):
        os.makedirs("output")

    file_name = "output/" + file_name
    with open(file_name, "w") as patent_file:
        for line in patent_document:
            patent_file.writer(line)

def getPatentNumber(patent_document):
    for line in patent_document:
        if "file=" in str(line):
            file_name_pattern = re.search(r"(US)([0-9])+(A1-)([0-9])+(.)(XML|xml)", line)
            file_name = file_name_pattern.group()
            return file_name

    return 0

file_name = "input/ipa110106.XML"
start_syntax = "<?xml version="

with open(file_name, "r") as xml_bulk_file:
    contents = xml_bulk_file.readlines()
    