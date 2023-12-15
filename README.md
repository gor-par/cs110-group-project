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

#4: Data Analysis

- ~~filter (queries to filter the data)~~

  - ~~FilterOption class to help writing the queries~~

...

- add the docstrings and stuff written in the requirements

- Add general statistics (range, median) to the table.py

- Global warming for nordic countries
  - correlation of snow with rain [and average temperatures]
  - Average temperature in Norway during winter months, through years, and it's change + average lowest and highest
  - compare global average temperatures over the same time in the world, but this can be just the temperature (check all the region, as in [norway, sweden, finland])
  - Compare those three things with other countries to see if the trend is keeping up and it is indeed warming up
  - maybe shift in snow?
    - like, calculate the amount or median snow depth of snow during oct-may per month, and graph the annual change in each month to see whether snow is getting delayed or starts to come early
