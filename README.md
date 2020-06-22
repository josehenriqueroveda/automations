# Automation of tasks in Python

List of scripts to automate some daily tasks, making it easy and fast to do.

### Features

> - [Convert JPG images to PNG](https://github.com/josehenriqueroveda/automations/blob/master/JPGtoPNG.py) Convert immediately a lot of .jpg images in a folder to .png images.
Run the command:  **`python JPGtoPNG.py OriginalImagesFolderName NewFolderName`** it's going to read all .jpg images inside the original folder, create a new folder and save each image converted to .png inside it.
> - [Create thumbnail images](https://github.com/josehenriqueroveda/automations/blob/master/create-thumbnail.py) Generates a reduced version of all images in a directory, maintaining the proportions, making them much lighter to be saved in the cloud.
Run the command:  **`python create-thumbnail.py OriginalImagesFolderName NewFolderName`** it's going to create a new folder with the resized images on it.
> - [Email sender](https://github.com/josehenriqueroveda/automations/blob/master/email_sender.py) Send email via GMAIL automatically based in html template.
Run the command:  **`python email_sender.py`** to automate the sending of emails.
> - [PDF merger](https://github.com/josehenriqueroveda/automations/blob/master/pdf_merger.py) Script to be used when you have a lot of .pdf files and want to merge them all immediately.
Run the command: **`python pdf_merger.py MyFile1.pdf MyFile2.pdf MyFile3.pdf MyFileN.pdf`** this is going to merge all the .pdf files passed in the command.
> - [Add watermarker to PDF](https://github.com/josehenriqueroveda/automations/blob/master/pdf_watermarker.py) Script that allows the watermark to be inserted on all pages of the file automatically.
Run the command: **`python pdf_watermarker.py MyFile.pdf Watermark.pdf`** to add a watermark to your .pdf file.
> - [File translator](https://github.com/josehenriqueroveda/automations/blob/master/translator.py) It works reading text files, translating it and saving as a new file. All of the ISO 639-1 languages are available. Works offline.
Run the command: **`python translator.py FileToBeTraslated.txt Language`** (Example of language input: pt, ja, en) 500 character text limit per file.
> - [Twitter bot](https://github.com/josehenriqueroveda/automations/blob/master/twitter_bot.py) Bot to follow-back people and like tweets.
Always read the Twitter API docs before start to use it to know the DO's and DON'T's. Run the command: **`python twitter_bot.py`** 

#### Requirements
- [Python3](https://www.python.org/)

**Liked it?**
Find me on [LinkedIn](https://www.linkedin.com/in/jhroveda/)
