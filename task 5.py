def word_count_distribution(search_queries):
    word_counts = [len(query.split()) for query in search_queries]
    word_count_freq = {}
    
    for count in word_counts:
        word_count_freq[count] = word_count_freq.get(count, 0) + 1
    total_queries = len(search_queries)
    word_count_percent = {}
    
    for count, freq in word_count_freq.items():
        percent = (freq / total_queries) * 100
        if count == 1:
            word_count_percent[f"{count} слово"] = f"{percent:.2f}%"
        elif 2 <= count <= 4:
            word_count_percent[f"{count} слова"] = f"{percent:.2f}%"
        else:
            word_count_percent[f"{count} слов"] = f"{percent:.2f}%"

    return word_count_percent
search_queries = [
    "watch new movies", "coffee near me", "how to find the determinant", "python", 
    "data science jobs in UK", "courses for data science", "taxi", "google", 
    "yandex", "bing", "foreign exchange rates USD/BYN", "Netflix movies watch online free",  
    "Statistics courses online from top universities"
]

distribution = word_count_distribution(search_queries)
for description, percent in distribution.items():
    print(f"{description} : {percent}")
    