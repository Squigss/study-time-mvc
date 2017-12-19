import json
import pprint

TEXT_FILE_NAME = '/Users/stephanierobinson/Desktop/study-time-mvc/database.txt'

class StudyHelperModel(object):
    def __init__(self):
        self.database_info = self.read_information_from_database()

    def save_information_to_database(self, info):
        with open(TEXT_FILE_NAME, 'w') as f:
            f.truncate()
            json.dump(info, f)

    def read_information_from_database(self):
        with open(TEXT_FILE_NAME, 'r') as f:
            database_info = json.loads(f.readline())
            return database_info

    def login_or_register_user(self):
        """ If user exists - retrieve user info. If used does not exist - add user name to database """
        if self.user_name in self.database_info:
            return 'You are an existing user %s, welcome back!' % self.user_name
        else:
            self.database_info[self.user_name] = {}  # Adding new user_name to database
            self.save_information_to_database(self.database_info)
            return "Welcome %s! We are glad to have you as a new user." % self.user_name

    def get_user_summary(self):
        """ Return a list of semicolon-separated strings representing info of each subject """
        summary_raw = self.database_info[self.user_name]
        summary = []
        for subject, info_dict in summary_raw.items():
            summary.append('; '.join([ subject,
                                       str(info_dict['Number of pages to study']),
                                       str(info_dict['Average time per page(in minutes)']),
                                       str(info_dict['Time to study the subject']), ]))
        return summary

    def get_total_time_to_study(self):
        """Return a sum of times to study for all subjects"""
        all_subjects_of_a_user_from_database = self.database_info[self.user_name]
        total_hours = 0
        for subject_name, subject_info in all_subjects_of_a_user_from_database.items():
            total_hours_for_a_subject = subject_info['Time to study the subject']
            total_hours = total_hours + total_hours_for_a_subject
        return total_hours

    def add_new_subject(self, subject, pages, time):
        users_subjects = self.database_info.get(self.user_name)

        subject_info = {'Number of pages to study': pages,
                         'Average time per page(in minutes)': time,
                         'Time to study the subject': round(pages * time / 60, 1) }
        users_subjects[subject] = subject_info
        self.save_information_to_database(self.database_info)
