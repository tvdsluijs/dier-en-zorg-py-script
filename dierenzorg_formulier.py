import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from datetime import datetime

from functions.readConfig import readConfig

class ReaalDierFormulier:
    def __init__(self):
        self.cf = readConfig()
        self.behandel_datum = ""
        self.declaratie_file = None
        self.backup_file = None
        self.browser = None

        self.get_behandel_datum()
        self.get_declaratie_file()
        if self.start_formulier():
            self.backup_declaratie_file()

    def get_behandel_datum(self):
        while True:
            try:
                behandel_datum = input("Behandel datum: [dd/mm/yyyy] (bijv: 14/05/2019) ")
                self.behandel_datum = datetime.strptime(behandel_datum, "%d/%m/%Y")
                break
            except ValueError as e:
                print("Onjuiste datum.")

    def start_formulier(self) -> bool:
        try:
            self.browser = webdriver.Chrome()
            self.browser.get("https://www.reaaldierenzorg.nl/klantenservice/online-declareren/")

            self.browser.find_element_by_id("contact_moment_policy_number").send_keys(self.cf.config['Polisnummer'])
            self.browser.find_element_by_id("contact_moment_relation_number").send_keys(self.cf.config['Relatienummer'])

            self.browser.find_element_by_id("contact_moment_date_of_birth_d").send_keys(
                                                                        self.cf.config['Uw_geboortedatum']['dag'])
            self.browser.find_element_by_id("contact_moment_date_of_birth_m").send_keys(
                                                                        self.cf.config['Uw_geboortedatum']['maand'])
            self.browser.find_element_by_id("contact_moment_date_of_birth_y").send_keys(
                                                                        self.cf.config['Uw_geboortedatum']['jaar'])

            self.browser.find_element_by_xpath('//*[@id="new_contact_moment"]/div[2]/button').click()

            # Ja, dit is mijn Iban
            self.browser.find_element_by_id("contact_moment_question_125").click()

            # dieren arts informatie
            self.browser.find_element_by_id("contact_moment_question_39").send_keys(
                                                                    self.cf.config['Dierenarts'])

            self.browser.find_element_by_id("contact_moment_question_43").send_keys(
                                                                    self.cf.config['Dierenarts_tel'])

            # behandel datum
            self.browser.find_element_by_id("question_47_d").send_keys(self.behandel_datum.day)
            self.browser.find_element_by_id("question_47_m").send_keys(self.behandel_datum.month)
            self.browser.find_element_by_id("question_47_y").send_keys(self.behandel_datum.year)

            # Buitenland Nee
            self.browser.find_element_by_id("contact_moment_question_50_nee").click()

            # toevoegen bestand
            if self.declaratie_file is not None and self.declaratie_file is not "":
                file_button = self.browser.find_element_by_id('contact_moment_documents_attributes_0_file')
                file_button.send_keys(self.declaratie_file)

            # Waarvoor bent u geweest?
            select = Select(self.browser.find_element_by_id('contact_moment_documents_attributes_0_questions_attributes_0_question_11'))
            # select.select_by_visible_text(self.cf.config['Waarvoor'])
            select.select_by_value(self.cf.config['Waarvoor'])

            # Wat is de klacht
            select = Select(self.browser.find_element_by_id('contact_moment_documents_attributes_0_questions_attributes_0_question_12'))
            # select.select_by_visible_text(self.cf.config['Klacht'])
            select.select_by_value(self.cf.config['Klacht'])

            # wat checkboxes dat je akkoord gaat met alles
            self.browser.find_element_by_id("contact_moment_question_57").click()
            self.browser.find_element_by_id("contact_moment_question_69").click()

            print("Controleer alle gegevens en klik op Verzenden")

            return True

        except Exception as e:
            print(e)
            return False

    def get_declaratie_file(self) -> bool:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        declaratie_folder = os.path.join(dir_path, "declaratie")
        backup_folder = os.path.join(dir_path, "backup_declaratie")
        for root, dirs, filenames in os.walk(declaratie_folder):
            for fileName in filenames:
                self.declaratie_file = os.path.join(declaratie_folder, fileName)
                self.backup_file = os.path.join(backup_folder, fileName)
                return True
        return False

    def backup_declaratie_file(self) -> bool:
        try:
            if self.declaratie_file is not None:
                os.rename(self.declaratie_file, self.backup_file)
            return True
        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    rdf = ReaalDierFormulier()

# 23/8/2019