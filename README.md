# HybridCloudApplication-using-Openstack
Cloud-based classroom assistant application will be developed using a hybrid cloud environment that combines resources from AWS and OpenStack
Read the Design and implementation part in the report to set up OpenStack in your local using devstack.
For the purpose of this application, we are running a Python script called controller.py
inside the OpenStack VM. This script uses the boto3 library to connect to S3 and AWS
lambda resources. In the controller.py script, the trigger_lambda() function will
continuously monitor the input S3 bucket for the availability of videos. Any videos available in the input S3 bucket will trigger the AWS lambda function
“cc_project,” we created as part of our second project. The input S3 bucket
and video file names identified will be passed on as JSON to the handler event. 
The lambda function invocation is then obtained as a response and
printed in the console for verification.
The download_csv() function, on the other hand, will look for any objects available
in the output S3 bucket, and it downloads those files and saves them in a folder names
“results” inside the OpenStack VM. Additionally, both functions keep tabs on the
objects that are already processed, which will prevent duplication of AWS triggers and
Duplicate objects from output S3 are being copied to the results folder.
