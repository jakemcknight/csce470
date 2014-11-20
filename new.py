import json #or cjson
import re
from stemming.porter2 import stem
from operator import itemgetter
import csv
class Hw1(object):
    def __init__(self):
        pass
    @staticmethod
    def read_line(a_json_string_from_document):
        #sample answer:
        return json.loads(a_json_string_from_document)
    @staticmethod
    def tokenize(string):
        unicode_word=re.findall(r'\w+',string['text'].lower())
        return [str(word) for word in unicode_word ]
    #return a list of words
    @staticmethod
    def tokenize1(string):
        unicode_word=re.findall(r'\w+',string.lower())
        return [str(word) for word in unicode_word ]
    #return a list of words
    @staticmethod
    def word_freq(word,a_list_of_words):
        count =0
        for line in a_list_of_words:
            if (line == word):
                count=count+1       
        return count
    def word_check(good , list2):
        count =0
        for line in list2:
            for word in good:
                if (line ==word):
                    count=count+1
        return count

    
    @staticmethod
    def stopword(a_list_of_words):
        stopword = []
        for line in open('stop_word','r'):
            stopword.append(re.split('\n',line)[0])
        new_list=[word for word in a_list_of_words if word not in stopword]
        return new_list
    #or alternatively use new_list=filter(lambda x: x not in stopword, a_list_of_words)
    #return a list of words
    @staticmethod
    def stemming(a_list_of_words):
        stems=[stem(word) for word in a_list_of_words]
        return stems
    #return a list of words
    
if __name__ == '__main__':
    #run this script to get top twenty bigrams
    hw=Hw1()
    count=0
    words = []
    bath_set= []
    bathdict = {}
    reviewdict = {}
    for line in open('./review_KcSJUq1kwO8awZRMS6Q49g.txt','r'):
         cur_review= hw.read_line(line)
         words=hw.tokenize(cur_review)
         count =0
         for word in words:
                count=count+1
                if (word=="bathroom" or word=="restroom" or word=="restrooms" or word=="toliet" or word=="washrooms" or word=="restrooms" or word=="bathrooms"):     
                        #need tof etch words before and after
                    string = " REVIEW "
                    array = []
                    array.append(cur_review['text'])
                    array.append(cur_review['business_id'])
                    reviewdict[cur_review['review_id']]=array

    #THIS PEICE OF CODE GOES THROUGH AND TOKENIZE OUR TEXT REVIEW TO RETURN N WORDS IN AN ARRAY
    for line in reviewdict:
        count=1
        index=0
        goal = 30  # YO WHATS UP I AM GOAL IF YOU CHANGE ME YOU GET MORE WORDS 
        
        tokens= hw.tokenize1(reviewdict[line][0])
        append_review=[]
        for word in tokens:
            count1=0
            count2=1
            if (word=="bathroom" or word=="restroom" or word=="restrooms" or word=="toliet" or word=="washrooms" or word=="restrooms" or word=="bathrooms"): 
                index=count
                while( len(tokens)-(index+count1) > 0 and count1 < 3):
                    append_review.append(tokens[index+count1])
                    count1=count1+1
                    goal = goal-1
                while( index-count2 >= 0 and goal > 0 and len(tokens) > index-count2 ):
                    append_review.append(tokens[index-count2])
                    count2=count2+1
                    goal = goal-1
                reviewdict[line][0]= append_review
                break
            count=count+1

    for line in reviewdict:
        print " "
        print line
        print reviewdict[line][0]
        print reviewdict[line][1]
        print" " 

    # REVIEW DICT ---NOTE THIS STRUCT IS A DICTONARY
    # THIS DICTONARY STORE THE REVIEW ID AS THE KEY THIS IS UNIQUE
    # reviewdict[key][0] this is the text review of the n closest words to bathroom
    # reviewdict[key][1] this is the buisness id this will be needed later when we fetch the location and buisness name
    # reviewdict[key][2] indicates if the bathroom is good or bad
    # if you wish to look for more words on either side the variable goal will need to be changed it is marked 


    # started building good/bad list needs to be added too 
    good_list = []
    bad_list = []
    for line in open("good.txt"):
        good_list.append(line.rstrip('\n'))

    print good_list
    
    for line in open("bad.txt"):
        bad_list.append(line.rstrip('\n'))
    for k in reviewdict:
        reviewdict[k].append(0)

    print bad_list
    # frequecny function just for fun
    print hw.word_freq("good",good_list)
    # here we need to check reviews against bad and good list and run naive bayes

    #for k in reviewdict:
        #for j in reviewidct
    good_total = len(good_list)
    bad_total = len(bad_list)
    #add a scoring index to the array [2]
    
    for k in reviewdict:
        for j in reviewdict[k][0]:
            for h in good_list:
                if(j == h):
                    reviewdict[k][2] = reviewdict[k][2] +float((float(1)/float(good_total)))
            for h in bad_list:
                if(j == h):
                    reviewdict[k][2] = reviewdict[k][2] - float((float(1)/float(bad_total)))


    for k in reviewdict:
        print reviewdict[k]
    c = 0
    for k in bad_list:
        c = 0
        for z in bad_list:
            if(k == z):
                c = c + 1
        if(c > 1):
            print k
                

        

    

                
