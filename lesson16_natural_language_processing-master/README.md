# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Natural Language Processing

## Learning Objectives

By the end of this lesson, students should be able to:
- Explain some of the challenges that make natural language processing difficult.
- Perform common text preprocessing techniques.
- Perform text classification.

---

## Student Requirements

Before this lesson, students should already be able to:
- Use Anaconda for package management
- Use train/test/split to create a set of features and target values
- Read data into a Pandas DataFrame
- Build and evaluate predictive models using scikit-learn

---

## Installation Notes
To proceed through the lesson, first install `TextBlob` as explained below. We tend to prefer Anaconda-based installations, since they tend to be tested with our other Anaconda packages. However, in this case TextBlob is not available on some platforms with Anaconda (e.g. Win64). To install textblob:

1. `conda install -c conda-forge textblob`

**Or:**

1. `pip install textblob`
2. `python -m textblob.download_corpora lite`

---

## Additional Resources
For more information, we recommend the following resources:

- Check out this [Yelp blog post](http://engineeringblog.yelp.com/2015/09/automatically-categorizing-yelp-businesses.html) how they completed a classification task (with over 1000 response variables!) using restaurant review text
- Always check documentation: [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html), [HashingVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.HashingVectorizer.html), [TF-IDF](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html)
- Wikpedia's [feature hashing](https://github.com/generalassembly-studio/DSI-course-materials/tree/master/curriculum/04-lessons/week-06/4.1-lesson) and [hash functions](https://en.wikipedia.org/wiki/Hash_function) is a great place to turn for more info on hashing
- Charlie Greenbacher's [Intro to NLP](http://spark-public.s3.amazonaws.com/nlp/slides/intro.pdf)
- Wikipedia includes a [walkthrough](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) of TF-IDF
- Google's [ngram tool](https://books.google.com/ngrams/graph?content=data+science&year_start=1800&year_end=2000&corpus=15&smoothing=3&share=&direct_url=t1%3B%2Cdata%20science%3B%2Cc0)
- An experiment using NLP and Eigenfaces (Eigenvalues for face recognition) [for Tinder](http://dataconomy.com/hacking-tinder-with-facial-recognition-nlp/)
