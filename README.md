# <br />
<div align="center">
  <a href="https://github.com/trevtravtrev/CoinSense">
    <img src="logo.png" alt="CoinSense" width="500" height="100">
  </a>

  <p align="center">
    Real-time cryptocurrency portfolio tracker.
    <br/>
  </p>
  <p align="center">
  <a href="https://github.com/trevtravtrev/CoinSense">
    <img src="demo.gif" alt="CoinSense" width="" height="">
  </a>
  </p>
</div>
<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#prerequisites">Prerequisites</a></li>
    <li><a href="#clone-the-repository">Clone the Repository</a></li>
    <li><a href="#run-the-code">Run the Code</a></li>
    <li><a href="#additional-tools">Additional Tools</a></li>

  </ol>
</details>

# Prerequisites
- [Python](https://www.python.org/downloads/) (latest version)  
  - If using windows, in the python installer make sure to select the "Add Python to PATH" option  
- [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) (optional)


# Clone the Repository
## Option 1: via Command Line Interface
- Install [GitHub CLI](https://cli.github.com/) (if not already installed)
  ```
  git clone https://github.com/trevtravtrev/CoinSense
  ```
## Option 2: via GitHub Desktop
1. Install [GitHub Desktop](https://desktop.github.com/) (if not already installed)  
2. Follow instructions [here](https://docs.github.com/en/desktop/contributing-and-collaborating-using-github-desktop/adding-and-cloning-repositories/cloning-a-repository-from-github-to-github-desktop) to clone
# Run the Code
## Option 1: Poetry (recommended)
1. Install Poetry (if not already installed)
```
pip install poetry
```
2. Install CoinSense dependencies
```
cd CoinSense
poetry install
```
3. Run CoinSense
```
poetry run python main.py
```
## Option 2: Docker
Docker is the easiest way to get CoinSense running, but you lose the pretty colors and formatting in the CLI. Docker, by default, just pipes the raw CLI data to its own unformatted CLI output in the docker desktop interface. For the best experience, option 1 (via poetry) is recommended.  
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/) (if not already installed)
2. Open Docker Desktop
3. Build the Docker image:
```
cd CoinSense
docker build -t coinsense .
```

4. Run the Docker container:
```
docker run coinsense
```
## Option 3: requirements.txt
1. Create the virtual environment:
```
cd CoinSense
python -m venv venv
```
2. Activate the virtual environment:
- For Windows:
```
venv\Scripts\activate
```
- For macOS/Linux:
```
source venv/bin/activate
```
Once activated, you will notice that the prompt in your terminal or command prompt changes to indicate that you are now working within the virtual environment.  
3. Install CoinSense dependencies
```
pip install -r requirements.txt
```
4. Run CoinSense
```
python main.py
```

# Additional Tools
All CoinSense code was formatted, linted, and secured with the following tools:
- [black](https://black.readthedocs.io/en/stable/)
- [flake8](https://flake8.pycqa.org/en/latest/)
- [radon](https://radon.readthedocs.io/en/latest/)
- [bandit](https://bandit.readthedocs.io/en/latest/)
- [isort](https://pycqa.github.io/isort/)
- [mypy](https://mypy.readthedocs.io/en/stable/)

