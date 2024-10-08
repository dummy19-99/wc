from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
search_term = "python"

response = get(f"{base_url}{search_term}")
if response.status_code != 200:
  print("Can't request website.")
else:
  results = []
  soup = BeautifulSoup(response.text, "html.parser")
  jobs = soup.find_all('section', class_="jobs")
  for job_section in jobs:
    job_posts = job_section.find_all('li')
    job_posts.pop(-1)
    for post in job_posts:
      anchors = post.find_all('a')
      anchors = anchors[1]
      link = anchors['href']
      company, kind, region = anchors.find_all('span', class_ = "company")
      title = anchors.find('span', class_ = 'title')
      job_data = {
        'link': f"https://weworkremotely.com/{link}",
        'company': company.string, 
        'region': region.sting,
        'position': title.string
      }
      results.append(job_data)
      for result in results:
        print(result)
        print("/////")