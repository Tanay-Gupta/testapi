import requests
from bs4 import BeautifulSoup

def get_contest_info(soup):
    contest_info = {}
    # contest_info["name"] = soup.find("h2", class_="event-name").text
    contest_info["url"] = soup.find("a", class_="mega-dropdown__list-item").get("href")
    # contest_info["start_time"] = soup.find("time", class_="start-time").text
    # contest_info["duration"] = soup.find("time", class_="duration").text.split(":")[0]
    # contest_info["end_time"] = soup.find("time", class_="end-time").text
    return contest_info

def main():
    url = "https://practice.geeksforgeeks.org/events/upcoming"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    contests = []
    print(soup.find_all(class_="mega-dropdown__list-item"))
    for div in soup.find_all( class_="mega-dropdown__list-item"):
        contest_info = get_contest_info(div)
        contests.append(contest_info)
    print(contests)

if __name__ == "__main__":
    main()
