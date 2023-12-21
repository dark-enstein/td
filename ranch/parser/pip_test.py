title: "Python Application Testing"
wrangler: "emily"
stock: "pythonapp/src"
#flags:
#    - "use-virtualenv"
rodeos:
  - rodeo:
      - ranch:
          name: "Setup Virtual Environment"
          cmd: [ "python", "-m", "venv", "venv" ]
      - ranch:
          name: "Install Dependencies"
          cmd: [ "pip", "install", "-r", "requirements.txt" ]
      - ranch:
          name: "Run Lint"
          cmd: [ "flake8", "." ]
      - ranch:
          name: "Run Unit Tests"
          cmd: [ "pytest", "tests/" ]
