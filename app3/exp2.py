"""
    EXECUTION TIMES
        1) 7mb.gz   =>  1723.5470000000205 ~ 30 MINUTE
        2) 9gb.gz   =>  2308.9689999999246 ~ 40 MINUTE
"""

import gzip
import time
import pandas as pd
import matplotlib.pyplot as plt
from transformers import pipeline

def openGzip(path):
    g = gzip.open(path, 'rb')
    for l in g:
        yield eval(l)

def getDF(path):
    i = 0
    df = {}
    for d in openGzip(path):
        df[i] = d
        i += 1
    return pd.DataFrame.from_dict(df, orient='index')

def manipulateReviews(reviews):
    manipulated_reviews = []
    for review in reviews:
        new_review = review if len(review) <= 512 else review[0:512]
        manipulated_reviews.append(new_review)
    return manipulated_reviews

def runExp(path):
    df = getDF(path)
    #sentiment_pipeline = pipeline("sentiment-analysis")
    reviews = df.reviewText.tolist()
    #reviews = manipulateReviews(reviews)

    #sentiment_pipeline(reviews)
    # for _, row in df.iterrows():
    #     review = row['reviewText']
    #     review = review if len(review) <= 512 else review[0:512]
    #     result = sentiment_pipeline(review)
    #     label = result[0]
    #     print(f"{_+1}. {label} - {review}")

# def benchmarkExp(path, ranges: list, attempts: int):
#     benchmark_timings = []
#     for _ in ranges:
#         times = []
#         for _ in range(attempts):
#             start_time = time.monotonic()
#             runExp(path)
#             end_time = time.monotonic()
#             times.append(end_time - start_time)
#         benchmark_timings.append(sum(times)/attempts)
#     return benchmark_timings


if __name__ == '__main__':
    # attempts for experiment times
    # attempts = 5

    # powers of 2 for benchmarking
    # ranges = [2**i for i in range(25)]

    # paths of datas
    paths = ['../datas/18gb.json.gz']
  
    start_time = time.monotonic()    
    runExp(paths[0])
    end_time = time.monotonic()
    print(f"END = {end_time - start_time}")

    # for path in paths:
    # benchmark_results = benchmarkExp(paths[0], ranges, attempts)
    # print(benchmark_results)        
    # plt.title('Dask Experiment. Time vs Increasing Input Size')
    # plt.xlabel('n (input size)')
    # plt.ylabel('time (seconds)')
    # plt.plot(ranges, benchmark_results)
    # plt.grid(True)
    # plt.show()


