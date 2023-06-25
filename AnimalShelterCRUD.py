#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 21:11:06 2023

@author: dantelee_snhu
"""

from pymongo import MongoClient

class AnimalShelter(object):
    
    def __init__(self, username, password):
    
        # MongoDB Values
        USER = username
        PASS = password
        HOST = "nv-desktop-services.apporto.com"
        PORT = 30846
        DB = "AAC"
        COL = "animals"
    
        self.client = MongoClient(f"mongodb://{USER}:{PASS}@{HOST}:{PORT}")
        self.db = self.client[DB]
        self.collection = self.db[COL]

    # Insert a document
    def create(self, document):
        try:
            result = self.collection.insert_one(document)
            return result.acknowledged
        except Exception as e:
            print(f"Error occurred during document insertion: {e}")
            return False
    
    # Query for documents
    def read(self, query):
        try:
            result = self.collection.find(query)
            return list(result)
        except Exception as e:
            print(f"Error occurred during document querying: {e}")
            return []
            
    def update(self, query, update_data):
        try:
            result = self.collection.update_many(query, {"$set": update_data})
            return result.modified_count
        except Exception as e:
            print(f"Error occurred during document updating: {e}")
            return False
        
    def delete(self, query):
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error occurred during document deletion: {e}")
            return False

    def filter_animals(self, filter_option):
        if filter_option == 'Water Rescue':
            # Apply filter criteria for Water Rescue
            breeds_filter = ['Labrador Retriever Mix', 'Chesapeake Bay Retriever', 'Newfoundland']
            sex_filter = 'Intact Female'
            age_filter = (26, 156)

            query = {
                'breed': {'$in': breeds_filter},
                'sex_upon_outcome': sex_filter,
                'age_upon_outcome_in_weeks': {'$gte': age_filter[0], '$lte': age_filter[1]}
            }

        elif filter_option == 'Mountain or Wilderness Rescue':
            # Apply filter criteria for Mountain or Wilderness Rescue
            breeds_filter = ['German Shepherd', 'Alaskan Malamute', 'Old English Sheepdog', 'Siberian Husky', 'Rottweiler']
            sex_filter = 'Intact Male'
            age_filter = (26, 156)

            query = {
                'breed': {'$in': breeds_filter},
                'sex_upon_outcome': sex_filter,
                'age_upon_outcome_in_weeks': {'$gte': age_filter[0], '$lte': age_filter[1]}
            }

        elif filter_option == 'Disaster or Individual Tracking':
            # Apply filter criteria for Disaster or Individual Tracking
            breeds_filter = ['Doberman Pinscher', 'German Shepherd', 'Golden Retriever', 'Bloodhound', 'Rottweiler']
            sex_filter = 'Intact Male'
            age_filter = (20, 300)

            query = {
                'breed': {'$in': breeds_filter},
                'sex_upon_outcome': sex_filter,
                'age_upon_outcome_in_weeks': {'$gte': age_filter[0], '$lte': age_filter[1]}
            }

        else:
            # No filter, return all documents
            query = {}

        return self.read(query)