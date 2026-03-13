class RESEARCHPAPER: #this class only handles a single document/paper

    #this function initialises everything
    def __init__(self,title,author,year,abstract,keywords):
        self.title=title
        self.author=author
        self.year=int(year)
        self.abstract=abstract
        self.keywords=[]
        keyword=keywords.split(",")
        for k in keyword:
            k=k.strip()
            if k:
                self.keywords.append(k)

    #this function converts plain text to a dictionary
    def to_dict(self):
        doc={
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'abstract': self.abstract,
            'keywords': self.keywords
        }

        return doc
    
    '''this function takes data; data is dictionary that contins all details of each document
    it converts data in an object
    {
    "title": "AI",
    "author": "Alice",
    "year": 2026,
    "abstract": "About AI",
    "keywords": ["ai", "ml"]
    }
    into:
    ResearchPaper(
        title="AI",
        author="Alice",
        year=2026,
        abstract="About AI",
        keywords=["ai", "ml"]
    )
    so when we load a document from files to ResearchPaper(title, author, year, abstract, keywords)
    that will call __init__'''

    @staticmethod # @staticmethod means this method belongs to the class but
    # does not use self; it can be called as RESEARCHPAPER.from_dict(data)
    # without creating an object first. so it doesnot depend on existing document
    def from_dict(data):
        #we used data.get bcs if any field in missing in dict then program wont crash it will take ampty string
        title=data.get('title','')
        author=data.get('author','')
        year=data.get('year',0)
        abstract=data.get('abstract','')
        keywords=data.get('keywords',[]) 

        return RESEARCHPAPER(title,author,year,abstract,','.join(keywords))
    
    #this function will lower case all letters, remove punctuations and will split them into list of words
    #text refers to abstract 
    @staticmethod
    def tokenize(text):
        words=[]
        clean_chars=[]
        text=text.lower()
        for chr in text:
            if chr.isalnum() or chr.isspace():
                clean_chars.append(chr) #list that contain all words and whitespace
        
        words=''.join(clean_chars) #converting it in string

        return words.split() #returning list with words not characters
    
    #this function will give back word frequency
    def word_frequency(self):
        words=self.tokenize(self.abstract)
        count={}

        for word in words:
            if word not in count:
                count[word]=0
            count[word]+=1
        
        return count
    
    






        
