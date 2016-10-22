FROM python:2.7-alpine

# Update
RUN apk add --update python py-pip

# Install app dependencies
RUN pip install beautifulsoup4 requests

# Bundle app source
RUN mkdir checklinks
COPY app checklinks/app

WORKDIR "/checklinks/app"

CMD ["python", "extractlinks.py"]



