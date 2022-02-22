import requests
import io
import json
import sys

def SubmitPMIDList(Inputfile,Format,Bioconcept):
	
	json = {}
	
	#
	# load pmids
	#
	with io.open(Inputfile,'r',encoding="utf-8") as file_input:
		json = {"pmids": [pmid.strip() for pmid in file_input.readlines()]}
	
	#
	# load bioconcepts
	#
	if Bioconcept != "": 
		json["concepts"]=Bioconcept.split(",")
		
	#
	# request
	#
	r = requests.post("https://www.ncbi.nlm.nih.gov/research/pubtator-api/publications/export/"+Format , json = json)
	if r.status_code != 200 :
		print ("[Error]: HTTP code "+ str(r.status_code))
	else:
		print(r.text.encode("utf-8"))

if __name__ == "__main__":

	arg_count=0
	for arg in sys.argv:
		arg_count+=1
	if arg_count<2 or (sys.argv[2]!= "pubtator" and sys.argv[2]!= "biocxml" and sys.argv[2]!= "biocjson"):
		print("\npython SubmitPMIDList.py [InputFile] [Format] [BioConcept]\n\n")
		print("\t[Inputfile]: a file with a pmid list\n")
		print("\t[Format]: pubtator (PubTator), biocxml (BioC-XML), and biocjson (JSON-XML)\n")
		print("\t[Bioconcept]: gene, disease, chemical, species, proteinmutation, dnamutation, snp, and cellline. Default includes all.\n")
		print("\t* All input are case sensitive.\n\n")
		print("Eg., python SubmitPMIDList.py examples/ex.pmid pubtator gene,disease\n\n")
	else:
		Inputfile = sys.argv[1]
		Format = sys.argv[2]
		Bioconcept=""
		if arg_count>=4:
			Bioconcept = sys.argv[3]
		
		SubmitPMIDList(Inputfile,Format,Bioconcept)