#from telnetlib import EC
import time
from select import select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
#from selenium.webdriver.support.wait import WebDriverWait

date = []
home_team = []
away_team = []
score = []

driver = webdriver.Chrome()
driver.get("https://www.adamchoi.co.uk/overs/detailed")

driver.maximize_window()

driver.find_element(By.XPATH, "//label[@analytics-event = 'All matches']").click()

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("Denmark")
time.sleep(4)
tables = driver.find_elements(By.TAG_NAME, "tr")
#WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//tr')))

for table in tables:
    try:
        date_text = table.find_element(By.XPATH, './td[1]').text
        home_team_text = table.find_element(By.XPATH, './td[2]').text
        away_team_text = table.find_element(By.XPATH, './td[4]').text
        score_text = table.find_element(By.XPATH, './td[3]').text

        # Append the text to the lists
        date.append(date_text)
        home_team.append(home_team_text)
        away_team.append(away_team_text)
        score.append(score_text)
    except Exception as e:
        print(f"An error occurred: {e}")

# Print the collected data
print("Date:", date)
print("Home Team:", home_team)
print("Away Team:", away_team)
print("Score:", score)

# Quit the driver
driver.quit()

# Create a DataFrame from the lists
data = {"Date": date, "Home Team": home_team, "Away Team": away_team, "Score": score}
df = pd.DataFrame(data)
df.to_csv("matches.csv", index=False)
print(df)
