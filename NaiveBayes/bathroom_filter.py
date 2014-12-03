__author__ = 'milesh'
import json

if __name__ == '__main__':
    br_stop_words = []
    with open("bathroom.txt", 'r') as br:
        for line in br:
            br_stop_words.append(line.split('\n')[0])
    print br_stop_words
    br_reviews = []
    br_businesses = []
    with open("review.json", 'r') as review:
        for line in review:
            if any([x in line for x in br_stop_words]):
                br_reviews.append(line)

    with open("business.json", 'r') as business:
        for line in business:
            if line == "":
                continue
            business_obj = json.loads(line)
            for review in br_reviews:
                if review == "":
                    continue
                rev_obj = json.loads(review)
                if rev_obj["business_id"] == rev_obj["business_id"]:
                    br_businesses.append(line)
                    break

    with open("bathroom_business.json", 'w') as br_bus_file:
        for line in br_businesses:
            br_bus_file.write(line)

    with open("bathroom_review.json", 'w') as br_review_file:
        for line in br_reviews:
            br_review_file.write(line)