# Simple Web Application for VGS Test

## What is this?

This is a very simple web application for demonstrating compatibility with VGS systems. 

## Resources

How to set up VGS routes:
[https://www.verygoodsecurity.com/docs/overview#learn-the-basics]

Python:
[https://python.io]

Docker:
[https://docker.io]

Ngrok:
[https://ngrok.io]

## What does it do?

After the application is running, you can send fake credit card data to VGS's echo server. This data goes through an inbound route set up within your VGS dashboard. After successfully sending the data, the app returns alias tokens in clean text representing your data. You can then send the tokens through the app, and the process repeats itself, this time going through a configured outbound route and returning the card data from the echo server.

## How do I add my credentials and get started?

You will need to populate the .env file, located within the app/ folder. You will need the following:

###1. Your vault id. This is located at the top of the page at 
        dashboard.verygoodsecurity.com

###2. HTTPS proxy username and password. These can also be located on dashboard.verygoodseurity.com by navigating the left sidebar to 

**Administration > Vault Settings**, 

and then selecting the **Access Credentials** tab. Once there, simply select **Generate Credentials** to retrieve a working set of credentials to reach your vault.

###Example:

Your .env file will look like this:


`HTTPS_PROXY_USERNAME="generatedusername"`
`HTTPS_PROXY_PASSWORD="generatedpassword"`
`VAULT="vaultidhere"`

##What else do I need?

The application assumes you have familiarity with Python, Docker, and ngrok, and have these environments set up.

You can run the docker file using:

`docker build -t vgstest:latest .`

Once running, you can start the container with the following:

`docker run -it -p 5000:5000 vgstest:latest`

You can choose to use -d for decoupled mode rather than -it.

Next, open a new terminal and run:

`ngrok http 5000`


Once running, select the generated address that utilizes https. Run the address in a web browser, and you're all set.