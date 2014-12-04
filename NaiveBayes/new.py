import json  # or cjson
import re
from stemming.porter2 import stem


class Helper(object):
    def __init__(self):
        pass

    @staticmethod
    def read_line(a_json_string_from_document):
        # sample answer:
        return json.loads(a_json_string_from_document)

    @staticmethod
    def tokenize(string):
        unicode_word = re.findall(r'\w+', string['text'].lower())
        return [str(word) for word in unicode_word]

    # return a list of words
    @staticmethod
    def tokenize1(string):
        unicode_word = re.findall(r'\w+', string.lower())
        return [str(word) for word in unicode_word]

    # return a list of words
    @staticmethod
    def word_freq(word, a_list_of_words):
        count = 0
        for line in a_list_of_words:
            if line == word:
                count += 1
        return count

    @staticmethod
    def word_check(good, list2):
        count = 0
        for line in list2:
            for word in good:
                if line == word:
                    count += 1
        return count


    @staticmethod
    def stopword(a_list_of_words):
        stopword = []
        for line in open('stop_word', 'r'):
            stopword.append(re.split('\n', line)[0])
        new_list = [word for word in a_list_of_words if word not in stopword]
        return new_list

    # or alternatively use new_list=filter(lambda x: x not in stopword, a_list_of_words)
    # return a list of words
    @staticmethod
    def stemming(a_list_of_words):
        stems = [stem(word) for word in a_list_of_words]
        return stems
        # return a list of words


if __name__ == '__main__':
    # run this script to get top twenty bigrams
    help_me = Helper()
    count = 0
    words = []
    bath_set = []
    bathdict = {}
    reviewdict = {}
    bathroom_words = []
    with open("bathroom.txt", 'r') as f:
        for line in f:
            bathroom_words.append(line.split('\n')[0])

    for line in open('bathroom_review.json', 'r'):
        cur_review = help_me.read_line(line)
        words = help_me.tokenize(cur_review)
        count = 0
        for word in words:
            count += 1
            string = " REVIEW "
            array = [cur_review['text'], cur_review['business_id']]
            reviewdict[cur_review['review_id']] = array

    # THIS PEICE OF CODE GOES THROUGH AND TOKENIZE OUR TEXT REVIEW TO RETURN N WORDS IN AN ARRAY
    for line in reviewdict:
        count = 1
        index = 0
        goal = 8  # YO WHATS UP I AM GOAL IF YOU CHANGE ME YOU GET MORE WORDS

        tokens = help_me.tokenize1(reviewdict[line][0])
        append_review = []
        for i, word in enumerate(tokens):
            if any([x == word for x in bathroom_words]):
                start = 0
                end = len(tokens)
                if not (i-goal) < start:
                    start = i-goal
                if not i+goal > end:
                    end = i+goal
                reviewdict[line][0] = tokens[start:end]

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
        reviewdict[k].append(1)
        reviewdict[k].append(1)

    print bad_list
    # frequecny function just for fun
    print help_me.word_freq("good", good_list)
    # here we need to check reviews against bad and good list and run naive bayes

    # for k in reviewdict:
    # for j in reviewidct
    good_total = len(good_list)
    bad_total = len(bad_list)
    # add a scoring index to the array [2]

    for k in reviewdict:
        for j in reviewdict[k][0]:
            for h in good_list:
                if j == h:
                    reviewdict[k][2] *= float((float(1) / float(good_total)))
            for h in bad_list:
                if j == h:
                    reviewdict[k][3] = reviewdict[k][3] * -1 * float((float(1) / float(bad_total)))

    for k in reviewdict:
        if reviewdict[k][2] == 1:
            if reviewdict[k][3] == 1:
                reviewdict[k].append("Neutral")
            else:
                reviewdict[k].append("Bad")
        elif reviewdict[k][3] == 1:
            reviewdict[k].append("Good")
        else:
            if reviewdict[k][2] > abs(reviewdict[k][3]):
                reviewdict[k].append("Good")
            else:
                reviewdict[k].append("Bad")

    for k in reviewdict:
        print reviewdict[k]
    c = 0
    for k in bad_list:
        c = 0
        for z in bad_list:
            if k == z:
                c += 1
        if c > 1:
            print k
    business_dict = {}
    with open("bathroom_business.json", 'r') as f:
        for line in f:
            business_obj = json.loads(line)
            business_obj["reviews"] = []
            business_dict[business_obj["business_id"]] = business_obj

    for item in reviewdict.values():
        business_dict[item[1]]["reviews"].append(item)

    for item in business_dict.values():
        bad_count, good_count, neut_count = 0, 0, 0
        if not len(item["reviews"]):
            del business_dict[item["business_id"]]
            continue
        for review in item["reviews"]:
            if review[-1] == 'Bad':
                bad_count += 1
            if review[-1] == 'Good':
                good_count += 1
            if review[-1] == 'Neutral':
                neut_count += 1
        bad_score = bad_count / len(item["reviews"])
        good_score = good_count / len(item["reviews"])
        neut_score = neut_count / len(item["reviews"])
        item["good"] = good_score
        item["bad"] = bad_score
        item["neutral"] = neut_score

    with open("../scored_review.json", 'w') as f:
        json.dump(business_dict, f)