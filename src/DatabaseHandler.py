import csv
import sys
import logging
import random
import pandas as pd

class DatabaseHandler():
    """
        Database handler class

        Raises -- sys.exit if the database .csv is not found
    """
    def __init__(self):
        self.red_questions = []
        self.white_questions = []
        self.blue_questions = []
        self.green_questions = []        
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.data, self.red_questions, self.white_questions, self.blue_questions, self.green_questions = self.populate_database_from_file("../database/QuestionDB.csv")

    def populate_database_from_file(self, file_path="../database/QuestionDB.csv"):
        """
        Get the data from the csv and put it in the database

        Keyword Args:
          file_path path to the csv file
        """
        data = []
        red_questions  = []
        white_questions = []
        blue_questions = []
        green_questions = []
        try:
            # open the file
            with open(file_path) as file:
                # read the file
                reader = csv.reader(file, delimiter=',')
                # parse the row
                for row in reader: 
                    try:
                        # append the array
                        data.append({ "question": row[0], "correct": row[1], "incorrect": row[2].split(','), "color": row[3] })
                        # Filter questions 
                        red_questions = [question for question in data if question ['color'] in 'red']
                        white_questions = [question for question in data if question ['color'] in 'white']
                        blue_questions = [question for question in data if question ['color'] in 'blue']
                        green_questions = [question for question in data if question ['color'] in 'green']

                    except Exception:
                        self.logger.error("Error parsing row: {0}".format(row))
        except FileNotFoundError: #pragma: no cover
            # no point in having a game with no questions
            sys.exit()
        return data, red_questions, white_questions, blue_questions, green_questions

    def select_color_question(self, color):
        """
        select a question from a particular color group

        Keyword Args:
          color - the color to select

        Return - the selected question
        """

        #Select the right subset of questions
        if color == 'red':
            filtered_questions = self.red_questions
        elif color == 'white':
            filtered_questions = self.white_questions
        elif color == 'blue':
            filtered_questions = self.blue_questions
        else:
            filtered_questions = self.green_questions

        return random.choice(filtered_questions)

    
