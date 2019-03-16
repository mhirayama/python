import requests
import lxml.html
import time
import pandas as pd

def main():
    session = requests.Session()
    response = session.get('http://npb.jp/bis/teams/')
    team_urls = scrape_team_page(response)
    
    df = pd.DataFrame()
    
    for team_url in team_urls:
        response = session.get(team_url)
        player_urls = scrape_player_page(response)
        
        for player_url in player_urls:
            time.sleep(1)
            response = session.get(player_url)
            record = scrape_detail_info(response)
            
            if record:
                print(record)
                series = pd.Series(record)
                df = df.append(series, ignore_index = True)
    df.to_csv('npb/player_records.csv', index = False)
    
def scrape_team_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)
    
    for a in root.cssselect('#team_list a'):
        url = a.get('href')
        yield url
    
def scrape_player_page(response):
    root = lxml.html.fromstring(response.content)
    root.make_links_absolute(response.url)

    for a in root.cssselect('td.rosterRegister a'):
        url = a.get('href')
        yield url
        
def scrape_detail_info(response):
    root = lxml.html.fromstring(response.content)
    
    try:
        keys = root.cssselect('#tablefix_p thead tr th')
        values = root.cssselect('#tablefix_p tbody tr.registerStats')[-1]
        name =  root.cssselect('#pc_v_name #pc_v_name')[0].text
        inning = root.cssselect('#tablefix_p tbody tr.registerStats table.table_inning tbody tr th')[-1]
    except:
        print('No data...')
        
    if not keys == [ ]:
        record = {keys[i].text.strip(): values[i].text.strip() for i in range(len(keys))}
        record['名前'] = name.strip()
        record['投球回'] = inning.text
        
        return record
    
if __name__ == '__main__':
    main()
