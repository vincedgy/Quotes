# Quotes project

## Presentation

This project is linked to the presentation named "Microservices  using AWS ECS"

## Objectives 

The aim of this project is to build a smal Quote of the day application using AWS assets, microservices developped
with SprindBoot, put into Docker Container and managed by ECS and ECR in AWS giving us scalling capabilities.
the applicayion read and write into a DynamoDB table names Quotes

The project propose : 
 - Python scripts using boto3 for DynamodDB, SNS and all AWS assets 
 - SpringBoot apps connected to DynamoDB with AWS Java SDK
 - HTML page and a JS script whith interacts with AWS Cognito for Authentication and DynamoDB for Reading the quotes

### Functions

We will develop a simple “quotes of the day” app using SpringBoot and a simple Static Web Page.
The quotes are proposed by someone identified by an email, but it’s one quote per day, not more.
A notification system is used for publisher and a moderator will validate or not a new quote. 

We need :
A simple Web Static Page connected to a DynamoDb table
A HTML FORM to “POST” a new quote (one per day per user)
The quote will be saved to DynamoDB thank to a set of microservices : 
A broker that will verify that only one quote has been posted per day, verify that the quote is not already in DynamoDB
A notification service using SNS to send email to the moderator and to the user
User give its email address for identification
 

## TODOS

### Create Scripts
- [x] DynamoDB table creation
- [x] DynamoDB table deletion

### Create HTML page : 
- [x] install live-server ```sudo npm i -g live-server``` 
- [x] create an index.html page with jQuery (https://code.jquery.com/) 
- [ ] create the js script wich interacts with Cognito for authentication and DynamoDB for reading data
- [ ] test it on my local machine
- [ ] push it to an S3 bucket with WebServer and version enabled with appropriate permissions and policy

### CORS configuration for S3 (if needed)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
  <CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
    <ExposeHeader>ETag</ExposeHeader>
    <ExposeHeader>x-amz-meta-custom-header</ExposeHeader>
  </CORSRule>
</CORSConfiguration>
```
