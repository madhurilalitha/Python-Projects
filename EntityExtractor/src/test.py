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
        len_before_highlight = len(et.raw_data)
        et.highlight_address_fields()
        et.highlight_contact_details()
        et.highlight_dates()
        et.tag_person_entities()

        et.save_document()

        # load the new document with highlighted text

        new_raw_data = docx2txt.process('Contract_Output.docx')
        len_after_highlight = len(new_raw_data)
        self.assertEqual(len_before_highlight, len_after_highlight)


if __name__ == '__main__':
    unittest.main()

