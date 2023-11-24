# The Weather Data Analysis group project for CS110E Intro to CS, AUA

## Participants

Ani Ghazanchyan, Milena Manukian, Gor Parisakoyan

## Instructions

To stage files:

```
git add .
```

To check status of staged and changed files:

```
git status
```

To commit staged files:

```
git commit -m 'your comment here'
```

To get the code from the repository:

```
git pull
```

To upload your code to the repository

```
git push
```

## Set up

Clone the repository:

```
git clone https://github.com/gor-par/cs110-group-project
```

Set a remote:

```
git remote add origin https://github.com/gor-par/cs110-group-project
```

Create and set upstream for the development branch:

```
git chekcout -b development
git push -u origin development
```

## Ideas | To do

#1 Dataset Reasearch

- Write a doc that describes the Datasets and their structure

#2 Data Reading

- ~~Python class to read the CSV and return an object containing the files~~

- ~~Table drawer program (didn't have time to refactor as a class)~~

  - ~~Add horizontal shortening~~

#3: Data Sanitization

- ~~Sanitizer, takes two paths, reads csv from first and writes into second~~

  - BEWARE: only deals with numerical data, DO NOT pollute text data

- filter (queries to filter the data)

- mean | median | range.... stuff like this

- find_results (function, column, filters)

- add the docstrings and stuff written in the requirements

def filter

def mean

def find_mean in this for this days
filter countr
filter date
mean | median |

def findresults (mean or media, column, filters)
filter 1
filter 2
mean

filters = {
country: albania
start_day: march 31

}

findresutls(mean, max_temerature, filters)

read
