import json
from paper import RESEARCHPAPER  
from similarity import magnitude,cosine_similarity

class LIBRARY:  # manages a list of RESEARCHPAPER objects
    def __init__(self, filename):
        self.filename = filename   
        self.papers = []

    def load_data(self):
        """Load papers from JSON file into self.papers."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)      # list of dicts
        except (FileNotFoundError, json.JSONDecodeError):
            # If file missing or broken, start with empty list
            self.papers = []
            return

        self.papers = []
        for item in data:
           
            paper = RESEARCHPAPER.from_dict(item)
            self.papers.append(paper)

    def save_data(self):
        """Save self.papers to JSON file as list of dicts."""
        data = []
        for paper in self.papers:
            # to write back in form of dictionary
            data.append({
                "title": paper.title,
                "author": paper.author,
                "year": paper.year,
                "abstract": paper.abstract,
                "keywords": ','.join(paper.keywords)
            })

        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    #function that add paper
    def add_paper(self):
        title=input("Enter title: ")
        author=input("Enter author: ")
        
        while True:
            try:
                year=int(input("Enter year: "))
                break
            except ValueError:
                print("Enter valid input(Only integers)")

        abstract=input("Enter abstract: ")
        keywords= input("Enter keywords seperated by comma: ")
        

        #this loop checks for duplicate title and asks user to reenter title        
        while True:
            duplicate=False
            for p in self.papers:
                if title.lower()==p.title.lower():
                        duplicate=True
                        print("Paper with title already exists")
                        choice=input("Enter 'r' to rewrite title or any key to cancel add: ").lower()
                        if choice=='r':
                            title=input("Enter title: ")
                            break

                        else:
                            return

            if duplicate==False:
                break   
        
        paper=RESEARCHPAPER(title,author,year,abstract,keywords)
        self.papers.append(paper)
        self.save_data()
        print("Paper successfully added")
        return
            
    #this funciton will display all papers
    def display_all(self):

        if not self.papers: #no paper
            print("There are no papers to display")
            return
        
        for paper in self.papers:
            print(f"TITLE: {paper.title}")
            print(f"AUTHOR: {paper.author}")
            print(f"YEAR: {paper.year}")
            print(f"ABSTRACT: {paper.abstract}")
            print(f"KEYWORDS: {','.join(paper.keywords)}")
            print("\n")

        print("_"*40)


    #this function give back how many times query word come in each paper
    def search(self,query):
        if query=='': #empty string
            print("No queries input")
            return

        token=RESEARCHPAPER.tokenize(query)   
        paper_score={}

        for paper in self.papers:
            total=0
            freq=paper.word_frequency()
            for word in token:
                total+=freq.get(word,0)

            paper_score[paper]=total

        ranked = sorted(paper_score.items(),  key=lambda x: x[1], reverse=True  ) #descending list with descending occurence of queries in papers

        if not ranked:
            print("No matches found")
            return []
        
        return ranked    
    

    #this function will find similar paper with title entered
    def find_similar(self,title):
        
        paper_found=False
        similar={}

        if not self.papers:
            print("Library is empty!")
            return []
        
        if len(self.papers)==1:
            print("There is only one paper in library")
            return self.papers[0]

        for paper in self.papers: #finding paper whose title is entered
            if paper.title.lower()==title.lower():
                paper_found=True
                main=paper
                break
        
        if paper_found==False:
            print("No paper found!")
            return []

        for paper in self.papers:
            if paper is main: #skip paper with entered title
                continue
            sim=cosine_similarity(main,paper)
            similar[paper]=sim

        #now we need to return top 3 papers who have cosine_similarity near to 1
        sort_similar=sorted(similar.items(),key=lambda x: x[1], reverse=True)

        if len(sort_similar)<3:  #if similar papers are less tahn 3 then return all papers(1,2)
            return sort_similar[:len(sort_similar)]
        else:
            return sort_similar[:3]
            



                

