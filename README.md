# # **Crackstation Through AWS** 
This library accepts encrypted strings with the SHA-1 or SHA-256 algorithm as input and outputs a decrypted string. The application is hosted as a service with the help of AWS.

## **Overview**<hr></hr>
The library can decrypt strings that have been SHA-1 or SHA-256 encrypted. It decrypts all possible combinations from the list matching the regular expression `[A-Za-z0-9?!] {1,3}`
The application uses API Gateway, Lambda and S3. API Gateway and lambda for the REST API and S3 for data storage.

### Version 1.0.0 
The most recent iteration can decrypt three character strings. The revised list of characters now also includes the letters "?" and "!" as well as the numbers 0 through 9 and alphabets. It includes every feasible combination. 

## Mission Statement<hr></hr>
The mission of this library is an effort to bring in the awareness that [unsalted](https://en.wikipedia.org/wiki/Salt_(cryptography)) passwords can be crackedm easily, hence people need to create more secure passwords, and everyone has access to our decrypter service.

## Author
Harsha Chaitanya. N
