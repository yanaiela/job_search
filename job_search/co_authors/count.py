import argparse
import requests
import time
from tqdm import tqdm

from job_search.utils import read_json_file

BASE_URL = 'https://api.semanticscholar.org/graph/v1'

def get_author_papers(author_id, api_key):
    url = f"{BASE_URL}/author/{author_id}/papers"
    headers = {
        'x-api-key': api_key
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def get_paper_details(paper_id, api_key):
    url = f"{BASE_URL}/paper/{paper_id}"
    headers = {
        'x-api-key': api_key
    }
    paper_data_query_params = {'fields': 'title,year,abstract,authors.name'}
    response = requests.get(url, headers=headers, params=paper_data_query_params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

def count_co_authors(author_id, author_papers, api_key):
    co_authors = set()
    for paper in tqdm(author_papers['data']):
        paper_details = get_paper_details(paper['paperId'], api_key)
        if paper_details:
            # print(paper_details)
            for author in paper_details['authors']:
                if author['authorId'] != author_id:
                    co_authors.add(author['authorId'])
        time.sleep(2)
    return len(co_authors)

if __name__ == "__main__":
    # Replace 'AUTHOR_ID' with the Semantic Scholar ID of the author
    # author_id = '51131518' # Yanai Elazar: 232
    # author_id = '145430120' # John Hewitt: 165
    # author_id = '48872685' # Sewon Min: 269
    
    parser = argparse.ArgumentParser(description="Process a BibTeX file to simplify journal and conference titles and remove URL and pages fields.")
    parser.add_argument("--author_id", help="author id from semantic scholar")
    
    args = parser.parse_args()
    
    
    content = read_json_file('config.json')
    s2_key = content['api-keys']['s2']
    assert s2_key != 'TODO', "Please provide your Semantic Scholar API key in the config.json file."
    
    author_id = args.author_id
    author_papers = get_author_papers(author_id, s2_key)
    
    if author_papers:
        co_author_count = count_co_authors(author_id, author_papers, s2_key)
        print(f"The author with ID {author_id} has {co_author_count} co-authors.")

