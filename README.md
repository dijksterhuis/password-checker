# password-checker-api

API to check user passwords against known commonly used passwords (e.g. qwerty123). Only for testing purposes. Please don't use for any other (nefarious) actions.
TODOs - expose local unix machine to conections OR deploy to cloud (AWS/Azure)

### Usage

- See curl_test.sh for examples of how to provide POST data to return True/False results
- There are multiple files available to check:
  - most commonly used hundred, to most commonly used million
  - See here (https://github.com/danielmiessler/SecLists/tree/master/Passwords) for full list
  - N.B. only the 10 million txt files have been implemented