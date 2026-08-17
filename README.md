## SPINNE

Feat: Initial setup with `env` virtual environment, automatic spreadsheets and organized projects! 

## Connection Back-End ↔ Front-End

- The Back-End (`API`) provides data in format JSON - (Documentation);
- The Front-End consumes this data via requests `HTTP` using `fetch` or `axios`.

---

## Organization:

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

## Login

- **Username**: spinne123;
- **Password**: spinne123.

The flow of the application follows the model below: the user interacts through the Front-End, which consumes the data via API (Back-End),
responsible for processing and querying the database. The response is sent in JSON, displayed again in the interface.

<div align="left">
  <img src="https://skillicons.dev/icons?i=angular" height="40" alt="angularjs logo" title="Angular" />
  <img src="https://skillicons.dev/icons?i=django" height="40" alt="django logo" title="Django" />
  <img src="https://skillicons.dev/icons?i=py" height="40" alt="python logo" title="Python" />
  <img src="https://skillicons.dev/icons?i=tailwind" height="40" alt="tailwindcss logo" title="Tailwind" />
  <img src="https://skillicons.dev/icons?i=ts" height="40" alt="typescript logo" title="TypeScript" />
</div>
