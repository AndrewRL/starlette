#!/bin/bash

rm psite.db
python db/create_db.py
python db/populate_db.py