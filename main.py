from config import *
from setting import *

if __name__ == '__main__':
    with open('elements.json') as fp:
        elements = json.loads(fp.read())
    profile_id = fnGetUUID()
    port = get_debug_port(profile_id)
    driver = get_webdriver(port)
    driver.get(UPWORK_URL)
    fnGetElementXpath(driver, True, elements["radio_freelancer"])
    fnGetElementXpath(driver, True, elements["btn_as_freelancer"])
    fnGetElementXpath(driver, False, elements["input_firstname"]).send_keys(FIRST_NAME)
    fnGetElementXpath(driver, False, elements["input_lastname"]).send_keys(LAST_NAME)
    fnGetElementXpath(driver, False, elements["input_email"]).send_keys(EMAIL)
    fnGetElementXpath(driver, False, elements["input_password"]).send_keys(PASSWORD)
    fnGetElementXpath(driver, True, elements["checkbox_agree"])
    fnGetElementXpath(driver, True, elements["btn_create_account"])
    while 1:
        try:
            fnGetElementXpath(driver, False, elements["btn_get_started"])
            break
        except:
            continue
    fnGetElementXpath(driver, True, elements["radio_expert"])
    fnGetElementXpath(driver, True, elements["btn_next"])
    fnGetElementXpath(driver, True, elements["radio_mainIncome"])
    fnGetElementXpath(driver, True, elements["btn_next"])
    fnGetElementXpath(driver, True, elements["radio_myself"])
    fnGetElementXpath(driver, True, elements["radio_client"])
    fnGetElementXpath(driver, True, elements["radio_recruiter"])
    fnGetElementXpath(driver, True, elements["checkbox_contract"])
    fnGetElementXpath(driver, True, elements["btn_next"])
    fnGetElementXpath(driver, True, elements["btn_fillout"])
    fnGetElementXpath(driver, False, elements["input_title"]).send_keys(TITLE)
    fnGetElementXpath(driver, True, elements["btn_next_experience"])
    fnGetElementXpath(driver, True, elements["input_nothing"])
    fnGetElementXpath(driver, True, elements["btn_next_experience"])
    fnGetElementXpath(driver, True, elements["input_nothing"])
    fnGetElementXpath(driver, True, elements["btn_next_experience"])
    fnGetElementXpath(driver, True, elements["div_language"])
    fnSelectEnglish(driver)
    fnGetElementXpath(driver, True, elements["btn_next_experience"])
    fnAddSkills(driver)
    fnGetElementXpath(driver, True, elements["btn_next_experience"])
    fnGetElementXpath(driver, False, elements["text_area_profile"]).send_keys(PROFILE)
    fnGetElementXpath(driver, True, elements["btn_next_experience"])
    fnGetElementXpath(driver, True, elements["select_service"])
    fnAddService(driver)
    fnGetElementXpath(driver, True, elements["btn_next_experience"])
    fnGetElementXpath(driver, False, elements["input_rate"]).clear()
    fnGetElementXpath(driver, False, elements["input_rate"]).send_keys(RATE)
    fnGetElementXpath(driver, True, elements["btn_next_experience"])
    fnGetElementXpath(driver, False, elements["input_street"]).send_keys(STREET)
    fnGetElementXpath(driver, False, elements["input_city"]).send_keys(CITY)
    time.sleep(2)
    fnAddCity(driver)
    fnGetElementXpath(driver, False, elements["input_zipcode"]).send_keys(ZIPCODE)
    fnGetElementXpath(driver, False, elements["input_phonenumber"]).send_keys(PHONENUMBER)
    print("Success")