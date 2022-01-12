docker build -t edr-data-expedition-ui .
docker run --restart always -d -p 5008:80 edr-data-expedition-ui
