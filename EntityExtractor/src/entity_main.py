#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created by Lalitha Madhuri Putchala on Dec 10 2017
"""

import unittest
from entity_main import Entity
from docx import Document
import docx2txt


class TestEntity(unittest.TestCase):

    '''The below function verifies the basic sanity functionality of the program 
       by validating the word count in the document before and after the highlighting
       of the text'''

    def test_sanity(self):

        et = Entity()
        et.highlight_address_fields()
        et.highlight_contact_details()
        et.highlight_dates()
        person_count = et.tag_person_entities()

        et.save_document()

        # load the new document with highlighted text

        new_raw_data = docx2txt.process('Contract_Output.docx')
        new_cnt = 0
        word_tokens = new_raw_data.split(' ')
        for each_token in word_tokens:
        	if '[PERSON]' in each_token:
        		new_cnt +=1
        self.assertEqual(person_count, new_cnt)


if __name__ == '__main__':
    unittest.main()

