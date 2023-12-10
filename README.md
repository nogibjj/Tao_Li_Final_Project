[![format](https://github.com/nogibjj/Tao_Li_Final_Project/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Tao_Li_Final_Project/actions/workflows/format.yml)
[![install](https://github.com/nogibjj/Tao_Li_Final_Project/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Tao_Li_Final_Project/actions/workflows/install.yml)
[![lint](https://github.com/nogibjj/Tao_Li_Final_Project/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Tao_Li_Final_Project/actions/workflows/lint.yml)
[![test](https://github.com/nogibjj/Tao_Li_Final_Project/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Tao_Li_Final_Project/actions/workflows/test.yml)

# python-template
The purpose of this project is to make a python template for use in IDS 706 for all subsequent python-based projects. The following are the important files contained in this repo:

1. `main.yml` - Github Actions for install, test, format, and lint.
2. `Makefile` - `make` commands for install, test, format, and lint
3. `first.py` - python script containing a function definition
4. `test_first.py` - python script containing tests for `first.py`
5. `requirements.txt` - contains names of required packages for installation.

## Project Requirements

- Microservice
    - Build a microservice that interfaces with a data pipeline. You can choose Python or Rust for development. The microservice should include logging and be containerized using the Distroless Docker image. A Dockerfile must be included in your repository.
- Load Test
    - The microservice must be capable of handling 10,000 requests per second. A load test verifying this performance should be included.
- Data Engineering
    - Your project should involve the use of a library specializing in data engineering such as Spark, Pandas, SQL, a vector database, or any other relevant library.
- Infrastructure as Code (IaC)
    - Your project must utilize an IaC solution for infrastructure setup and management. You can choose among AWS CloudFormation, AWS SAM, AWS CDK, or the Serverless Framework.
- Continuous Integration and Continuous Delivery (CI/CD)
    - Implement a CI/CD pipeline for your project. It could be through GitHub Actions or AWS Cloud Build or any other relevant tool.
- README.md
    - A comprehensive README file that clearly explains what the project does, its dependencies, how to run the program, its limitations, potential areas for improvement, and how AI Pair Programming tools (GitHub Copilot and one more tool of your choice) were used in your development process.
- Architectural Diagram
    - A clear diagram representing the architecture of your application should be included in your project documentation.
- GitHub Configurations
    - Your GitHub repository must include GitHub Actions and a .devcontainer configuration for GitHub Codespaces. This should make the local version of your project completely reproducible. The repository should also include GitHub Action build badges for install, lint, test, and format actions.
- Teamwork Reflection
    - Each team member should submit a separate 1-2 page management report reflecting on the team's functioning according to the principles discussed in your teamwork book. This report should not be part of the GitHub README but rather a separate document. It should include a peer evaluation in which each team member is graded on their performance, stating three positive attributes and three areas for improvement as the basis for the grade. Note that each student will share the teamwork reflection with their team and discuss it in a session before turning in the report. The outcome of this feedback session must be included in the report for full credit.
- Quantitative Assessment
    - The project must include a quantitative assessment of its reliability and stability. You must use data science fundamentals to describe system performance, e.g., average latency per request at different levels of requests per second (100, 1000, etc.). Think of the software system as a data science problem that needs to be described using data science principles.

## Architecture

* Microservice: The microservice is developed using FastAPI.
* Containerization with Distroless: By using distroless containers, the FastAPI application is not only efficiently packed with its required environments but also gains an enhanced level of security.
* Cloud infrastructure with IaC: Azure Functions enable the application to scale dynamically based on demand, ensuring cost-effective resource utilization. The integration of IaC with Azure Functions enhances service reliability and performance, allowing for seamless scaling and management of resources in response to varying loads.

## Project structure

* CI/CD: leveraging GitHub Actions for continuous integration and delivery, ensuring code quality and seamless deployment.
* Data interaction: we follow the ETL process in `mylib`: extract from an online database, transform&load into a sqlite3 database `GroceryDB.db`. Then we query data from the `GroceryDB` database using `query.py`, and transform the query results to `.json` format for front-end deployment.
* Front-end: `template/home.html` offers a clean interface to interact with the service, using Bootstrap as a responsice design.

## Workflow

* Users interact with the `index.html` page, which is served by the FastAPI application. Domain: grocery-online.azurewebsites.net
* 
