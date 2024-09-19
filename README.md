# FreeSearcher 
```
___________________________________________ ____________________   _____ ___________________   ___ ________________________  
\_   _____/\______   \_   _____/\_   _____//   _____/\_   _____/  /  _  \\______   \_   ___ \ /   |   \_   _____/\______   \ 
 |    __)   |       _/|    __)_  |    __)_ \_____  \  |    __)_  /  /_\  \|       _/    \  \//    ~    \    __)_  |       _/ 
 |     \    |    |   \|        \ |        \/        \ |        \/    |    \    |   \     \___\    Y    /        \ |    |   \ 
 \___  /    |____|_  /_______  //_______  /_______  //_______  /\____|__  /____|_  /\______  /\___|_  /_______  / |____|_  / 
     \/            \/        \/         \/        \/         \/         \/       \/        \/       \/        \/         \/
```

A simple windows CLI application for accessing ripped media. These are all checked by us, and are 100% safe.

-THIS IS A WORK IN PROGRESS!-

## RUN search-help FOR MORE INFO

## Installation

OS X:

> Not Currently Supported

Linux:

Download the files and extract them to your desired location

Then cd into the linux folder

Then make the file executable using
```
chmod u+x Main.sh
```
To run the program, while in the directory of install, run:
```
./Main.sh
```
Or open Main.sh in your file manager

Windows:

Unzip the file. Run "run.ps1" in powershell. You must have 'Bypass' Exec Policy. 
```
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope LocalMachine -Force
```
(or run start.bat as admin, this file is hidden)

To create an executable file for regualr usage, install NSIS
(https://nsis.sourceforge.io/Main_Page), then open source.nsi in the NSIS exe compiler.

WINDOWS MAY REQUIRE A CLOUD SECURITY SCAN, THIS IS FINE

Example command:
```
search-manga-one-piece.volumes-1
```
This will download One Piece volume 1.

ChromeBook:

Enable Linux Dev Enviroment.

Drag the files for the linux port into the new 'linux files' folder. Open your linux terminal and run 
```
chmod u+x Main.sh
```
Then run ./Main.sh YOU MUST DO THIS EVERY TIME YOU WISH TO USE THE PROGRAM!
## Usage 

Variable 1 is the action. Currently this includes

>Search

Variable 2 is the type of media. Currently, this includes

>Manga
>Novel
>Show
>Movie
>Text

Variable 3 is the name of the media. multiple words are separated by a dash.

Variable 4 is the section of media. This is seperated by a dot. This includes:

>Episodes
>Volumes
>Chapters
>Parts
>Sections
>Books

Variable 5 is the number of media. Usually this is a number, but special variables include:

>All
>Season(number)
>Or some type of other catergorization.

## TO MANUALLY UPDATE RUN search-update

## Changelog

8/sep/24: Linux ported by XanderIsBored

6/sep/24: Version 1.0 release.

5/sep/24: Created Repo

Distributed under the GNU 3.0 license. Please by using this software, you agree to this.

Linux port by XanderIsBored

## Contributing

> Send files as a catbox or fileditch link, in an ISSUE request.
> You may also help support the project by refining code.
Help create batch scripts in the links repo here: https://github.com/TheFreeWeb/freesearcherlinkdir
