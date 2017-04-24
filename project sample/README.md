Team 19: Boston by Omar El Samad (749907), Samuel Josei Jenkins (389975), Mubashir Munawar (713627), Xuan Fan (653226), Dinni Hayyati (666967)
# Boston twitter harvest and analysis
For cloud and cluster computing By Team 19
###### External HTTP link -  [http://144.6.226.184:5000](http://144.6.226.184:5000)
-----------------------------------------------------------------------------------------------------------------
### Root
- */cloudsent/*           Main analysis part files , folder *analysis* is not using anymore
- */web-svc/*             web service testing codes , not using in running server
- */devops/*              Hostfile manage nodes
- */example-s3/*          Example of configuration
- */twitter-harvesters/*  The application harvesting codes into couch db


### Important Update log
- 27/4/2015 : tweetsmining.py created , Tweets mining started.
- 30/4/2015 : Three more nodes added to mine tweet
- 5/5/2015  : Web service established
- 10/5/2015 : Analysis part added
- 15/5/2015 : Lots of functions updated

------------------------------------------------------------------------------------------------------------------
### Twitter Harvest 
`/twitter-harvesters/`
##### Prerequisites:
  - `python, tweepy, couchdb, textblob`

- **TweetMining.py** : Main harvest app for loading data into Couch database 'twitter'(lighter db) and 'twitter_user'(full data volume db )applies in 4 instances with 8GB RAM, 2 Virtual CPU, 10 GB                   disk and 60GB Ephemeral Disk
  - **mylogsfile** : record logs in file for monitering status
  - **Twitter API Authentication** : We used 4 access tokens to harvest in the same time in different machines
  - **Analyse_text** : Use TextBlob to analysis specific tweet is negative or positive depends on polarity and store into field sentiment at couchdb
  - **get_location_tweets** : we use geographic coordinates which is Boston acutally located

------------------------------------------------------------------------------------------------------------------
### Remote configuration
`/devops/platform/`
##### Prerequisites:
- Bash 4.3+
- Ansible 1.9+
- Terraform 0.5+
- j2cli 0.3+
- Ensure the SSH keypair assigned to the cluster is available via ssh-agent.
  This is required for Ansible.
- Expose OpenStack credentials as environment variables.
- Expose DNSimple credentials as environment variables.

#####To configure:
- Adjust `./platform-config.sh` to the platform to be built.
- Adjust `$PLATFORM/cluster-config.sh` where `$PLATFORM` is the desired platform
  found in `./platform-config.sh`.

#####To launch or update existing build (idempotent):
- Run `./build-cluster.sh`.

#####To remove:
- Run `./destroy-cluster.sh`.

------------------------------------------------------------------------------------------------------------------
### Sentiment Analysis with ReST web service
`/cloudsent/`
##### Prerequisites:
  - `python 3, couchdb, flask, textblob`

- **flask_server.py** : Main application file
  - return sentiment json : '/api/v1/sentiment/<message>', e.g. `http://localhost:5000/api/v1/sentiment/obama`
  - return graph object : `http://localhost:5000/api/v1/graph/obama`
  - return particular tweet : `http://localhost:5000/rawtwitter/591823382628413440`
  - return text of 404 error : 404 NOT FOUND handling 
`/cloudsent/templates`
- **index.html**
  - Main coding file in represental layer
  - All request except sentiment and graph in URL will be redirect to this homepage
  - Using javascript to implement via Flask
`/clousent/static/assets`
- **/bootstrap/** : use to generate website in quick way
- **/css/**       : Casde style sheet for controlling web page appearance
- **/img/**       : All image resources
- **/js/**        : Lots of Javascript called here

##### Launch
Copy team19.pem to working directory as access key and use ssh:
`ssh -i team19.pem -N -L 8000:localhost:5000 ubuntu@144.6.226.184`
And in web browser type http://localhost:8000 to visit our homepage
