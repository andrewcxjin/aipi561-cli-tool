# CLI and Automation 
This mini-project is a command-line interface (CLI) tool that will go through a selected log file and summarize is based on the key labels. It will also provide example logs for each type of label found. A script has also been created to automate this tool. A demo video is attached in the repository. 

### User Manual
Install independecies
```
pip install -r requirements.txt
```
Run manually
```
python app.py logs/{insert log file name}
```
Run with automation script
```
chmod +x run.sh
./run.sh
```


### Test Report
```
================================ tests coverage ================================
_______________ coverage: platform linux, python 3.11.12-final-0 _______________

Name     Stmts   Miss  Cover   Missing
--------------------------------------
app.py      28      3    89%   33-34, 38
--------------------------------------
TOTAL       28      3    89%
Required test coverage of 80% reached. Total coverage: 89.29%
============================== 1 passed in 0.04s ===============================
```