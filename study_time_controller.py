import tkinter
import study_time_model
import study_time_view

class Controller(object):
    def __init__(self):
        self.model = study_time_model.StudyHelperModel()
        self.view = study_time_view.StudyHelperView(None)

        self.view.login_button.bind("<Button-1>", self.login_button_function)
        self.view.save_button.bind("<Button-1>", self.save_button_function)

    def login_button_function(self, event):
        user_name = self.view.user_name_variable.get()
        self.model.user_name = user_name
        comment = self.model.login_or_register_user()

        #update user comment
        self.view.user_comment_variable.set(comment)
        self.update_summary_and_total_time()

    def save_button_function(self, event):
        subject = self.view.subject_name_variable.get()
        pages = self.view.pages_to_read_variable.get()
        time = self.view.time_per_page_variable.get()
        self.model.add_new_subject(subject, pages, time)
        self.update_summary_and_total_time()



    def update_summary_and_total_time(self):
        #delete everything from listbox and add a new header
        self.view.listbox.delete(0, tkinter.END)
        self.view.listbox.insert(0, "Subject; Pages; Time per page; Total time")

        #summary
        summary = self.model.get_user_summary()
        for i, message in enumerate(summary, 2):
            self.view.listbox.insert(i, message)

        #total time to study
        total_time = self.model.get_total_time_to_study()
        self.view.time_to_study_comment_variable.set('Time needed to complete your studies: {} hours'.format(str(total_time)))

    def run(self):
        self.view.title('my application')
        self.view.mainloop()


if __name__ == "__main__":
    c = Controller()
    c.run()
