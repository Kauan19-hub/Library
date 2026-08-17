**<h2>BookStore</h2>**

Feat: Initial setup with `env` virtual environment, automatic spreadsheets and organized projects! 

**<h2>🔗 Connection Back-End ↔ Front-End</h2>**

- The Back-End (`API`) provides data in format JSON - (Documentation);
- The Front-End consumes this data via requests `HTTP` using `fetch` or `axios`.

---

**<h2>Organization:</h2>**

- `spreadsheets/`: Has files  `.xlsx` generated;
- `scripts/`: scripts for automations of spreadsheet;
- `api/`: Example of API with Django.

---

**Tools for Tests**: [Insomnia](https://insomnia.rest/download) and/or [Postman](https://www.postman.com/downloads/)

| ITEM                  | RESPONSIBLE FOR DEPENDENCIES              |
|-----------------------|-------------------------------------------|
| `env` (Python)        | Python Packages                           |
| `node_modules` (Node) | JS/Angular Packages                       |
| `requirements.txt`    | List of what to install on `env`          |
| `package.json`        | List of what to install on `node_modules` |


The flow of the application follows the model below: the user interacts through the Front-End, which consumes the data via API (Back-End),
responsible for processing and querying the database. The response is sent in JSON, displayed again in the interface.