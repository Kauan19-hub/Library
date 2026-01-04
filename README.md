**<h2>Library SENAI</h2>**

###
Feat: Initial setup with `env` virtual environment, automatic spreadsheets and organized projects! 

###

**<h2>🔗 Connection Back-End ↔ Front-End</h2>**

- The Back-End (`API`) provides data in format JSON - (Documentation);
- The Front-End consumes this data via requests `HTTP` using `fetch` or `axios`.

---

`endpoint` example:

###
```js
GET http://localhost:3000/api/livros
```

Consumes example in the Front-End

###
```js
fetch("http://localhost:3000/api/livros")
  .then(res => res.json())
  .then(data => console.log(data));
```

###

✅ Env development;<br>
✅ Installation of libraries: pandas and openpyxl for data manipulation and table creation with Excel;<br>
✅ Folder structure in Insonmia or Postman for API testing;<br>
✅ Automation scripts for generating spreadsheet readings using pandas and openpyxl;<br>
✅ File and directory organization;<br>
✅ Using Front-End and Back-End;<br>
✅ Examples with Node.JS, Angular.JS and Express;<br>
✅ Examples of how to use Django and JSON for API integration;<br>
✅ Documentation explaining the project.<br>

---

Spreadsheet automation using `pandas` and `openpyxl` 

###

Creation of the virtual environment: 

###
```powershell
python -m venv env
```

###
```powershell
source env/bin/activate ## MacOS/Linux
```
###
```powershell
.\env\Scripts\activate ## Windows
```

---

**<h2>Organization:</h2>**

###

- `spreadsheets/`: Has files  `.xlsx` generated;
- `scripts/`: scripts for automations of spreadsheet;
- `api/`: Example of API with Django.

---

###

**<h2>Quick tip :</h2>**

###
```python
var1 = dir (link)  ## xlsx table path 
var2 = pd.read_csv(var)  ## Call the path in another variable 

print(file.head()) ## Start of spreadsheet 
print(file.shape()) ## Middle of the spreadsheet 
print(file.dtypes()) ## End of spreadsheet 

path_file = r'T:\ (full path of files) 
print('Currently Used Directory :', os.getcwd())   ## Remember to import the  (OS) - import os
print('This file exists?', os.path.isfile(arquivo_caminho)  ## if exist, print 'TRUE', else, 'FALSE'
```

---

Back-End (`Node.js` + `Express`)

###
```powershell
cd backend
```

###
```powershell
npm install
```

###
```powershell
npm start
```

###

Front-End (`Angular` or `React`)

###
```powershell
cd frontend
```

###
```powershell
npm install
```

###
```powershell
npm start
```

###

API `Django` (Optional)

###
```powershell
cd api
```

###
```powershell
pip install -r requirements.txt
```

###
```powershell
python manage.py runserver
```

###

**<h2>Versions</h2>**

###

- Python: `3.13`;
- Node.js: `node -v`;
- NPM: `npm -v`.

###

**<h2>Main Dependencies:</h2>**

###

- `pandas`, `openpyxl`, `Pillow`;
- `Django Rest Framework`;
- `Express`.

---

`py manage.py runserver`</br>
`ng serve`

###

**Tools for Tests**: [Insomnia](https://insomnia.rest/download) and/or [Postman](https://www.postman.com/downloads/)

###

---

**<h2>Contributions**

###

Issues and contributions are welcome! Feel free to suggest improvements or contribute to the project!

---

| ITEM                  | RESPONSIBLE FOR DEPENDENCIES              |
|-----------------------|-------------------------------------------|
| `env` (Python)        | Python Packages                           |
| `node_modules` (Node) | JS/Angular Packages                       |
| `requirements.txt`    | List of what to install on `env`          |
| `package.json`        | List of what to install on `node_modules` |

###

The flow of the application follows the model below: the user interacts through the Front-End, which consumes the data via API (Back-End),
responsible for processing and querying the database. The response is sent in JSON, displayed again in the interface.

---

OBS.: Depending on your version `Node.js`, `TypeScript`, `Django`, `TailwindCSS`, `Angular.JS` e `npm`, the bookstore may not be open. Below will be noted the 
versions of all extensions and languages used to function correctly:

###

**The versions of all extensions and dependencies are in the requirements.txt**
