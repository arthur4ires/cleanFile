import argparse
from os import remove
from os.path import isfile

def cleanFile(argumentosScript):

	arquivoClean = open(argumentosScript.input,'r')

	if isfile(argumentosScript.output):
		remove(argumentosScript.output)

	newFile =  open(argumentosScript.output,'w')

	if '|' not in argumentosScript.strings:
		print('Set | in strings args.')

	for a in arquivoClean:
		keywordNot = False
		
		for b in argumentosScript.strings.split('|'):

			if b in a:
				keywordNot = True

		if keywordNot != True:
			newFile.write(a)

	newFile.close()

def main():

	parser = argparse.ArgumentParser()
	parser.add_argument("--input", help="file input", type=str, required=True)
	parser.add_argument("--output", help="file output", type=str, required=True)
	parser.add_argument("--strings", help="syntax = palavra|palavra2", type=str, required=True)

	args = parser.parse_args()

	return cleanFile(args)

if __name__ == '__main__':
	main()


