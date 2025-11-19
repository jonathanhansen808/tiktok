#pip install -r requirements.txt

import time, requests, pickle, os, json, re, csv, pandas as pd
from openai import OpenAI
from io import StringIO
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from pathlib import Path
from github import Github
from github import Auth
from github import GithubIntegration

options = Options()
b = webdriver.Chrome(options = options)
b.get("https://ads.tiktok.com/business/creativecenter/inspiration/popular/hashtag/pc/en")
time.sleep(2)
b.maximize_window()
time.sleep(2)

if os.path.exists('new_cookies.pkl'):
    cookies = pickle.load(open("new_cookies.pkl", "rb"))
    for cookie in cookies:
        b.add_cookie(cookie)
    time.sleep(5)
    b.refresh()
pickle.dump(b.get_cookies(), open("new_cookies.pkl", "wb"))
time.sleep(1)


b.find_element(By.ID, "hashtagIndustrySelect").click()
time.sleep(1)
b.find_element(By.CSS_SELECTOR, "[data-option-id='SelectOption0']").click()
b.find_element(By.CSS_SELECTOR, "label.byted-checkbox").click()

y = 750
for timer in range(0,6):
     b.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 750  
     time.sleep(1)

hashtags = b.find_elements(By.XPATH, '//span[@class="CardPc_titleText__RYOWo"]')
hashtag_list = []
for h in range(len(hashtags)):
    hashtag_list.append(re.sub("# ", "", hashtags[h].text))
hashtags_dic = {}
hashtags_dic["Apparel"] = hashtag_list


b.execute_script("window.scrollTo(0, 0)")
b.refresh()
time.sleep(2)
b.find_element(By.ID, "hashtagIndustrySelect").click()
time.sleep(1)
b.find_element(By.CSS_SELECTOR, "[data-option-id='SelectOption2']").click()
b.find_element(By.CSS_SELECTOR, "label.byted-checkbox").click()

y = 750
for timer in range(0,6):
     b.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 750  
     time.sleep(1)

beauty_hashtags = b.find_elements(By.XPATH, '//span[@class="CardPc_titleText__RYOWo"]')
beauty_hashtag_list = []
for h in range(len(beauty_hashtags)):
    beauty_hashtag_list.append(re.sub("# ", "", beauty_hashtags[h].text))
hashtags_dic["Beauty_Personal_Care"] = beauty_hashtag_list


b.execute_script("window.scrollTo(0, 0)")
b.refresh()
time.sleep(4)
b.find_element(By.ID, "hashtagIndustrySelect").click()
time.sleep(1)
b.find_element(By.CSS_SELECTOR, "[data-option-id='SelectOption3']").click()
b.find_element(By.CSS_SELECTOR, "label.byted-checkbox").click()

y = 750
for timer in range(0,6):
     b.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 750  
     time.sleep(1)

business_hashtags = b.find_elements(By.XPATH, '//span[@class="CardPc_titleText__RYOWo"]')
business_hashtag_list = []
for h in range(len(business_hashtags)):
    business_hashtag_list.append(re.sub("# ", "", business_hashtags[h].text))
hashtags_dic["Business_Services"] = business_hashtag_list


b.execute_script("window.scrollTo(0, 0)")
b.refresh()
time.sleep(2)
b.find_element(By.ID, "hashtagIndustrySelect").click()
time.sleep(1)
b.find_element(By.CSS_SELECTOR, "[data-option-id='SelectOption5']").click()
b.find_element(By.CSS_SELECTOR, "label.byted-checkbox").click()

y = 750
for timer in range(0,6):
     b.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 750  
     time.sleep(1)

finance_hashtags = b.find_elements(By.XPATH, '//span[@class="CardPc_titleText__RYOWo"]')
finance_hashtag_list = []
for h in range(len(finance_hashtags)):
    finance_hashtag_list.append(re.sub("# ", "", finance_hashtags[h].text))
hashtags_dic["Financial_Services"] = finance_hashtag_list


b.execute_script("window.scrollTo(0, 0)")
b.refresh()
time.sleep(2)
b.find_element(By.ID, "hashtagIndustrySelect").click()
time.sleep(1)
b.find_element(By.CSS_SELECTOR, "[data-option-id='SelectOption6']").click()
b.find_element(By.CSS_SELECTOR, "label.byted-checkbox").click()

y = 750
for timer in range(0,6):
     b.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 750  
     time.sleep(1)

food_hashtags = b.find_elements(By.XPATH, '//span[@class="CardPc_titleText__RYOWo"]')
food_hashtag_list = []
for h in range(len(food_hashtags)):
    food_hashtag_list.append(re.sub("# ", "", food_hashtags[h].text))
hashtags_dic["Food_Beverage"] = food_hashtag_list

b.execute_script("window.scrollTo(0, 0)")
b.refresh()
time.sleep(2)
b.find_element(By.ID, "hashtagIndustrySelect").click()
time.sleep(1)
b.find_element(By.CSS_SELECTOR, "[data-option-id='SelectOption9']").click()
b.find_element(By.CSS_SELECTOR, "label.byted-checkbox").click()

y = 750
for timer in range(0,6):
     b.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 750  
     time.sleep(1)

Home_hashtags = b.find_elements(By.XPATH, '//span[@class="CardPc_titleText__RYOWo"]')
Home_hashtag_list = []
for h in range(len(Home_hashtags)):
    Home_hashtag_list.append(re.sub("# ", "", Home_hashtags[h].text))
hashtags_dic["Home Improvement"] = Home_hashtag_list


b.execute_script("window.scrollTo(0, 0)")
b.refresh()
time.sleep(2)
b.find_element(By.ID, "hashtagIndustrySelect").click()
time.sleep(1)
b.find_element(By.CSS_SELECTOR, "[data-option-id='SelectOption15']").click()
b.find_element(By.CSS_SELECTOR, "label.byted-checkbox").click()

y = 750
for timer in range(0,6):
     b.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 750  
     time.sleep(1)

Tech_hashtags = b.find_elements(By.XPATH, '//span[@class="CardPc_titleText__RYOWo"]')
Tech_hashtag_list = []
for h in range(len(Tech_hashtags)):
    Tech_hashtag_list.append(re.sub("# ", "", Tech_hashtags[h].text))
hashtags_dic["Tech_Electronics"] = Tech_hashtag_list


b.execute_script("window.scrollTo(0, 0)")
b.refresh()
time.sleep(2)
b.find_element(By.ID, "hashtagIndustrySelect").click()
time.sleep(1)
b.find_element(By.CSS_SELECTOR, "[data-option-id='SelectOption17']").click()
b.find_element(By.CSS_SELECTOR, "label.byted-checkbox").click()

y = 750
for timer in range(0,6):
     b.execute_script("window.scrollTo(0, "+str(y)+")")
     y += 750  
     time.sleep(1)

Vehicle_hashtags = b.find_elements(By.XPATH, '//span[@class="CardPc_titleText__RYOWo"]')
Vehicle_hashtag_list = []
for h in range(len(Vehicle_hashtags)):
    Vehicle_hashtag_list.append(re.sub("# ", "", Vehicle_hashtags[h].text))
hashtags_dic["Vehicle_Transportation"] = Vehicle_hashtag_list


b.close()
print("Hashtags Captured")
print("Saving First to Github")

top = 0 
cleaned_top = 0 
empty = []

for key in hashtags_dic.keys():
    rows = len(hashtags_dic[key])
    if rows == 0:
        empty.append(key)
    elif rows > top:
        top = rows
    else:
        continue
        
for key in empty:
    del hashtags_dic[key]

for key, value in hashtags_dic.items():
    if len(value) < top:
        hashtags_dic[key] = value + [""] * (top - len(value))

auth = Auth.Token("addme")

g = Github(auth = auth)
g.get_user().login
repo = g.get_repo('jonathanhansen808/tiktok')

date = datetime.today().strftime('%Y-%m-%d')

path_local = f"{date}.csv"     # local file
path_repo  = f"CSVs/{date}.csv"     # path inside repo (same here)

with open(path_local, "r", encoding = "utf-8") as f:
    content = f.read()

try:
    existing = repo.get_contents(path_repo)
    repo.update_file(
        path_repo,
        f"Update {path_repo}",
        content,
        existing.sha
    )
    print("updated")
except:
    repo.create_file(
        path_repo,
        f"Create {path_repo}",
        content
    )
    print("saved")

print("Using OpenAI API")

all_values = []
column_map = []    

for col, vals in hashtags_dic.items():
    for i, v in enumerate(vals):
        all_values.append(v)
        column_map.append((col, i))

client = OpenAI(api_key="addme")

prompt = f"""
You will receive a list of strings. 
For each string, return its normalized, segmented version.
Here are the caveats for the words appearing in the list - 
If a word appears in another language, such as abuelitos, leave it as is.
Recognize celebrity names and acronyms when applicable. 
Any words ending in the three letters tok should be left alone.
If you are unsure on a word, it is best to leave it only.

Return ONLY a JSON array of cleaned strings, in the same order as the input.
Finally, Wrap your final answer in the following structure: 
{{"normalized_strings": [cleaned_string1, cleaned_string2, ...]}}

Do not include the originals. Do not include keys. Do not wrap in an object.
Output must be a valid JSON array.

Input list:
{all_values}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    response_format={"type": "json_object"}
)

cleaned_list = json.loads(response.choices[0].message.content)
cleaned_list = cleaned_list["normalized_strings"]

cleaned_dic = {k: vals.copy() for k, vals in hashtags_dic.items()}

for cleaned_value, (col, idx) in zip(cleaned_list, column_map):
    cleaned_dic[col][idx] = cleaned_value

for key, value in cleaned_dic.items():
    if len(value) < top:
        cleaned_dic[key] = value + [""] * (top - len(value))

path_local_cleaned = f"{date}-cleaned.csv"    
path_repo_cleaned  = f"CSVs/{date}-cleaned.csv"     

with open(path_local_cleaned, "r", encoding = "utf-8") as f:
    content = f.read()

try:
    existing = repo.get_contents(path_repo_cleaned)
    repo.update_file(
        path_repo_cleaned,
        f"Update {path_repo_cleaned}",
        content,
        existing.sha
    )
    print("updated")

except:
    repo.create_file(
        path_repo_cleaned,
        f"Create {path_repo_cleaned}",
        content
    )
    print("updated")

time.sleep(5)

repo = g.get_repo("Jonathanhansen808/tiktok")
contents = repo.get_contents("CSVs")  

def extract_date_from_filename(name: str):
    try:
        return datetime.strptime(name[:10], "%Y-%m-%d")
    except:
        return None
    
csv_files = []

for item in contents:
    if not item.path.lower().endswith(".csv"):
        continue
    if "cleaned" in item.path.lower():
        continue

    date = extract_date_from_filename(item.name)
    if date:
        csv_files.append((item, date))

csv_files.sort(key=lambda x: abs((x[1] - datetime.today()).days))
(item1, d1), (item2, d2) = csv_files[:2]

if d1 >= d2:
    base_item, base_date = item1, d1
    other_item, other_date = item2, d2
else:
    base_item, base_date = item2, d2
    other_item, other_date = item1, d1

print(f"Base CSV:   {base_item.name}")
print(f"Compare to: {other_item.name}")

def load_csv_from_github(item):
    content_bytes = item.decoded_content
    content_str = content_bytes.decode("utf-8")
    f = StringIO(content_str)
    reader = csv.reader(f)
    rows = list(reader)

    headers = rows[0]
    cols = {h: [] for h in headers}

    for row in rows[1:]:
        for i, h in enumerate(headers):
            val = row[i].strip() if i < len(row) else ""
            if val:
                cols[h].append(val)

    return cols

base_dic = load_csv_from_github(base_item)
other_dic = load_csv_from_github(other_item)

new_entries = {}

for col in base_dic.keys():
    base_vals = set(v for v in base_dic[col] if v.strip())
    other_vals = set(v for v in other_dic.get(col, []) if v.strip())
    unique_vals = sorted(base_vals - other_vals)
    new_entries[col] = unique_vals

max_rows = max(len(v) for v in new_entries.values()) if new_entries else 0
for col, vals in new_entries.items():
    if len(vals) < max_rows:
        new_entries[col] = vals + [""] * (max_rows - len(vals))

output_name = f"New {base_date.strftime('%Y-%m-%d')} vs {other_date.strftime('%Y-%m-%d')}.csv"
remote_path = f"Comparisons/{output_name}"

buffer = StringIO()
writer = csv.writer(buffer)
writer.writerow(new_entries.keys())
writer.writerows(zip(*new_entries.values()))
comparison_content = buffer.getvalue()

try:
    existing = repo.get_contents(remote_path)
    repo.update_file(
        remote_path,
        f"Update {remote_path}",
        comparison_content,
        existing.sha
    )
    print(f"Updated existing file on GitHub: {remote_path}")

except Exception:
    repo.create_file(
        remote_path,
        f"Create comparison output {remote_path}",
        comparison_content
    )
    print(f"Created new file on GitHub: {remote_path}")