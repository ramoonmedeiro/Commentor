from bs4 import BeautifulSoup, Comment
import requests
import sys
import argparse


# PARSER STEP
parser = argparse.ArgumentParser(description="Only takes the comments in the URLs. Only this =)")


parser.add_argument('--url', type=str, required=False, help='URL TARGET\nExample: python3 main.py --url https://google.com')
parser.add_argument('--file', type=str, required=False, help='WORDLIST WITH URLs\nExample: python3 main.py --file file-with-urls.txt')

args = parser.parse_args()


# MAIN FUNCTION

if args.url:
	r = requests.get(args.url)
	soup = BeautifulSoup(r.content, 'html.parser')
	comments = soup.find_all(string = lambda text: isinstance(text, Comment))

	for linha in comments:
		print(linha)

elif args.file:
	with open(args.file) as arquivo:
		for linha in arquivo:
			linha = linha.strip()
			print()
			print(f'############################ COMMENTS IN {linha} ############################')
			r = requests.get(linha)
			soup = BeautifulSoup(r.content, 'html.parser')
			comments = soup.find_all(string = lambda text: isinstance(text, Comment))

			for line in comments:
				print(line)

print('THANKS FOR THE USE')		
