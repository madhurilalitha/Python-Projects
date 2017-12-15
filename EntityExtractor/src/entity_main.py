#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by Lalitha Madhuri Putchala on Dec 10 2017
"""

import spacy
import docx2txt
import re
from docx import Document
from utils import get_sentence_tokens, tag_text, highlight_text


class Entity:
    def __init__(self):
        self.raw_data = docx2txt.process('Contract_Input.docx')
        self.doc = Document('Contract_Input.docx')

    def highlight_address_fields(self):

        # extract street address/zipcodes/ proper format address and improper format address using python regex
        street_address_exp = re.compile(
            u'\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\D|$)',
            re.IGNORECASE)
        street_addresses = re.findall(street_address_exp, self.raw_data)

        zip_code_exp = re.compile(r'\b\d{5}(?:[-\s]\d{4})?\b')
        zip_codes = re.findall(zip_code_exp, self.raw_data)

        proper_address_exp = "[0-9]{1,5} .+, .+, [A-Z]{2} [0-9]{5}"
        proper_addresses = re.findall(proper_address_exp, self.raw_data)
        # logic to handle the improper format address instead of using regex functions
        sentence_tokens = get_sentence_tokens(self.raw_data)
        for i in range(len(sentence_tokens)):
            if sentence_tokens[i][0] == 'Address:':
                improper_format = sentence_tokens[i + 1][0]

        address_details = list()
        address_details.extend(street_addresses)
        address_details.extend(zip_codes)
        address_details.extend(proper_addresses)
        address_details.append(improper_format)

        # highlight address fields
        for each in address_details:
            highlight_text(self.doc, each.strip())

    def highlight_contact_details(self):

        contact_details = list()
        # Get emails and phone numbers
        emails = re.findall(r'[\w\.-]+@[\w\.-]+', self.raw_data)
        phonenumbers = re.findall(
            r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}', self.raw_data)
        contact_details.extend(emails)
        contact_details.extend(emails)
        for contact in contact_details:
            highlight_text(self.doc, contact)

    def highlight_dates(self):

        # Get dates
        match = re.search(r'(\d+/\d+/\d+)', self.raw_data)
        highlight_text(self.doc, match.group(1))

    def tag_person_entities(self):

        # use pre-trained spacy models to get the 'PERSON' entities
        model = spacy.load('en_core_web_sm')
        mydata = model(self.raw_data)
        person_labels = list()
        for each in mydata.ents:
            if each.label_ == 'PERSON':
            	person_labels.append(each.text)
        unique_person_labels = set(person_labels)
        for label in unique_person_labels:
        	tag_text(self.doc, label)

    def save_document(self):
        self.doc.save('Contract_Output.docx')
