# Description
1. This repo can help you deploy python application to AWS Lambda by AWS CDK, and enable function url for external access.
2. I wrote two endpoint in this example, one is GET /testGet and another is POST /testPost.

# How to use
1. Go to AWS IAM and create a new User, and give it AdministratorAccess permission, and get Access Key ID and Secret Access Key, copy them and set them to github secrets.
* If you are in PROD environment, please do not give AdministratorAccess permission
2. When you merge other branch to development or test or main branch, it will auto deploy to AWS Lambda.
3. Go to AWS Lambda console, you can see the deployed function, and you can see the function url.
4. You can use Postman or curl to access the function url, and test the two endpoint I wrote.