Create environtment wineq

```bash
conda create -n wineq python=3.7 -y
```

activate env
```bash
conda activate wineq
```

create reuirements file
```bash
touch requirements.txt
```

install requirements
```bash
pip install -r requirements.txt
```

download the data from link

git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m "first commit"

git add . && git commit -m "update Reame.md"

git remote add origin https://github.ccom/farhadulh98/dvcdemo.git

git branch -M main

git push origin main

git add . && git commit -m "update Reame.md"

git push origin main

git add . && git commit -m "paramerts added"

git push origin main


tox command -
``` bash
tox
```

for rebuilding -
```bash
tox -r
```
pytest command
```bash
pytest -v
```

setup commands -
```bash
pip install -e .
```

build your own package commands-
```bash
python setup.py sdist bdist
```

