# Custom blog
Typically a simple blog written in flask - python micro-web framework. Enjoy it!

## Run a blog
Execute next command in your shell
```bash
~ python blog.py
```

## Structure
### Home Page
![Screenshot](server/images/home.png)
### Login Page
![Screenshot](server/images/login.png)
### Register Page
![Screenshot](server/images/register.png)

## Contributing

### Setup
- clone the repository
- configure Git for the first time after cloning with your name and email
  ```bash
  git config --local user.name "Volodymyr Yahello"
  git config --local user.email "vjagello93@gmail.com"
  ```
- `python3.6` is required to run the code
- run `pip install -r requirements.txt` to install all require python packages

### Run automated tests
- To run all tests please execute `./run-tests all` from shell in the root directory of the repository.
- To run basic smoke tests please execute `./run-tests smoke` from shell in the root directory of the repository.
- To run performance tests please execute `./run-tests performance` from shell in the root directory of the repository.
- To run unittests please execute `./run-tests unittest` from shell in the root directory of the repository.
