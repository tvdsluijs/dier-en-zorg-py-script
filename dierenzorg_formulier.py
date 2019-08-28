import os
import pathlib
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from time import sleep

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
            self.browser.get("https://formulieren.proteqcrm.nl/declaraties/dier_en_zorg")

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
            self.browser.find_element_by_css_selector(f"select#contact_moment_documents_attributes_0_questions_attributes_0_question_11 > option[value='{self.cf.config['Waarvoor']}']").click()

            sleep(2)  # ff wachten tot volgende selectbox gevuld is.
            try:
                # Klacht, dit zit in een try, want soms gaat dit helaas fout.
                self.browser.find_element_by_css_selector(f"select#contact_moment_documents_attributes_0_questions_attributes_0_question_12 > option[value='{self.cf.config['Klacht']}']").click()
            except Exception as e:
                pass

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
        self.check_create_folders(declaratie_folder)

        backup_folder = os.path.join(dir_path, "backup_declaratie")
        self.check_create_folders(declaratie_folder)

        for root, dirs, filenames in os.walk(declaratie_folder):
            for fileName in filenames:
                self.declaratie_file = os.path.join(declaratie_folder, fileName)
                self.backup_file = os.path.join(backup_folder, fileName)
                return True
        return False

    def check_create_folders(self, folder: str = None) -> bool:
        if folder is None:
            return False
        try:
            p = pathlib.Path(folder)
            p.mkdir(exist_ok=True)
            return True
        except Exception as e:
            print(e)
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

"""
Alles zelf nalopen en dan zelf op Verzenden klikken.
Als het goed is krijg je daarna te zien
====================================================
Uw declaratie is ontvangen
We nemen zo spoedig mogelijk contact met u op
"""