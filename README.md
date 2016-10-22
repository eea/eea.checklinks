# eea.docker.checklinks

Simple dockerised python application that takes in a list of urls, extract urls and checks the links for http status code by
retrieving the HEAD data from the host.

## How to use it

it requires [docker engine](https://docs.docker.com/engine/installation/) installed.

1. git clone this repo
2. cd &lt;reponame&gt;
3. docker build -t link-checker .
4. docker run -it --rm -v  &lt;path-to-data-folder&gt:/checklinks/app/data:z -e "EXCLUDE_LINKS=.europa.eu" --name my-running-linkchecker linkchecker

The "path-to-data-folder" is a path to a folder on your host where you must make
available a file (urls-to-analyze.txt) with urls. The file must contain one page url 
per line.

The tool will scan each page html and extract links from the page. 

If a EXCLUDE_LINKS variable is passed the urls under that domain wil be skipped 
for checking. This can be useful if you want to extract and check only external 
links from your site. In this last case you
pass the environment variable EXCLUDE_LINKS=yourdomain.com.

At the end the tool reports each link status code (200, 301, 404 etc.).
