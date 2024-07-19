'''Write a program that searches through reviews list and looks for keywords such as "good", "excellent", "bad", "poor", and "average". We want you to capitalize those keywords then print out each review. Print out each review with the keywords in uppercase so they stand out.
    reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
'''
#task1

string1 = ' good ' 
string2 = " excellent " 
string3 = " bad "
string4 = " poor "
string5 = " This product is really good. I'm impressed with its quality."
string6 = " The performance of this product is excellent. Highly recommend! "
string7 = " I had a bad expierience with this product. It didn't meet my expectations."
string8 = " Poor qaulity product. Wouldn't recommend it to anyone. "
string9 = " The product was average. Nothing extraordinary about it. "

concatenated = string1 + string5
concatenated = string2 + string6
concatenated = string3 + string7
concatenated = string4 + string8
concatenated = string1 + string9

print(concatenated)

#task2
'''Develop a function that tallies the number of positive and negative words in each review.  The function should return the total count of positive and negative words.
    positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
    negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]
'''


def tally_sentiments(reviews, positive_words, negative_words):
   
    results = []
    for review in reviews:
        review_lower = review.lower()  # Convert review to lowercase to make the search case-insensitive
        positive_count = sum(review_lower.count(word) for word in positive_words)
        negative_count = sum(review_lower.count(word) for word in negative_words)
        results.append({'positive': positive_count, 'negative': negative_count})
    return results

# Example usage:
reviews = [
    "The product was amazing and the service was superb!",
    "It was a terrible experience, very disappointing.",
    "Overall, the experience was good, but some aspects were poor.",
    "Absolutely fantastic service, I'm extremely happy!",
    "The quality was subpar and the wait time was horrible."
]

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

# Call the function
results = tally_sentiments(reviews, positive_words, negative_words)

# Print the results
for i, result in enumerate(results):
    print(f"Review {i + 1}: {result}")
    
#task3
#Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. Ensure that the summary does not cut off in the middle of a word. 

def summarize_review(review, max_length=30):
   
    if len(review) <= max_length:
        return review

    # Find the last space within the max_length
    cut_off = review.rfind(' ', 0, max_length)
    if cut_off == -1:  # No spaces found within max_length
        cut_off = max_length
    
    return review[:cut_off] + "…"

# Example usage:
reviews = [
    "The product was amazing and the service was superb!",
    "It was a terrible experience, very disappointing.",
    "Overall, the experience was good, but some aspects were poor.",
    "Absolutely fantastic service, I'm extremely happy!",
    "The quality was subpar and the wait time was horrible."
]

# Create summaries for each review
summaries = [summarize_review(review) for review in reviews]

# Print the summaries
for i, summary in enumerate(summaries):
    print(f"Summary {i + 1}: {summary}")
