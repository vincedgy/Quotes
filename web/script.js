



AWS.config.apiVersions = {
  dynamodb: '2012-08-10',
  // other service API versions
};
var dynamodb = new AWS.DynamoDB();
dynamodb.batchGetItem(params, function (err, data) {
  if (err) console.log(err, err.stack); // an error occurred
  else     console.log(data);           // successful response
});