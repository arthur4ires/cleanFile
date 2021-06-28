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
		exit()

	duplicateUrls = []

	for a in arquivoClean:

		if argumentosScript.extensions != None:

			if '|' not in argumentosScript.extensions:
				print('Set | in extensions args.')
				exit()

			if '.' in a:

				stopExtension = False

				for _ in argumentosScript.extensions.split('|'):
					if _ in a.split('.')[-1].replace('\n',''):
							stopExtension = True
							break

				if stopExtension == True:
					continue

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
	parser.add_argument("--extensions", help="extensions = palavra|palavra2", type=str)

	args = parser.parse_args()

	return cleanFile(args)

if __name__ == '__main__':
	main()


