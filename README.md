# Agristore

Agristore is a python based program which aims to store greenhouse data using ethereum blockchain.
Please follow the steps to setup the program

## Required programs
The entire program is developed on windows, therefore all programs below are installed on windows platform

Install node.js (v14.18.1), the website can be found:
```
https://nodejs.org/en/
```

Install Ganache(v2.5.4), the website can be found:

```
https://trufflesuite.com/ganache/
```

Install Ganache-cli (v6.12.2, ganache-core: 2.13.2) for commandline style operations for ganache:
```
Using npm:

npm install -g ganache-cli

Using yarn:

yarn global add ganache-cli
```

Install conda for windows to manage other packages:
```
https://www.anaconda.com/products/individual
```
and use conda envirment file to install conda envirement with the correct packages: 
```
conda env create -f blockchain.yml
```
## Setup
Visual studio code is used for development of this program.
A .env file needs to be created for sensitive data such as private keys and passwords in order for brownie config file to work. An example can be:
```
export PRIVATE_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxx
export WEB3_INFURA_PROJECT_ID = xxxxxxxxxxxxxxxxxxxxxxxxxxx
export ETHERSCAN_TOKEN = xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
###First 
Download the correct version of solidity in visual studio code by pressing shift+control+p to open the search bar. Select "Solidity: change global compiler version" and install version 0.8.10.
Select the correct python envirement with correct package by pressing shift+control+p and select "Python x.x.xx 64-bit('Blockchainv2':conda).

###Second
Run the correct conda interpreter by click on run for a random python script then type in the console:
```
brownie compile
```
to compile the contract and download its required packages

###Third
Currently using dropbox as cloud storage, therefore a dropbox token needs to be required, follow the instrustion on the following link:
```
https://www.dropbox.com/developers/apps/create
```

###fourth (if running on testnet or publicnet)
Make a account for metamask and infura for deploying/interacting the contract. This step can be skipped if the program is ran locally using ganache.

## Demo run
To use the program (if tested locally, open the ganache app first) run the main script under folder AgriStore/scripts/main.py. The settings needs to be changed to ur local paths
```python
# settings---------------------------------------------------------------------
# path that the system will scan for greenhouse data
scanpath = {path/to/datascan}
# path that the modified/original data will be saved
savepath = {path/to/datasave/locally}
# path in the cloud of which the data can be saved
cloud_path = {path/to/datasave/cloud}
# dropbox token, which is required to use the dropbox
with open("{path/to/cloudtoken.txt}", "r") as file:
    token = file.read()
# level that can be used to divide the data
levels = 10
# settings---------------------------------------------------------------------
```

## More info
For more information for smartcontract and brownie usage please watch the following youtube link:
```
https://www.youtube.com/watch?v=M576WGiDBdQ
```
