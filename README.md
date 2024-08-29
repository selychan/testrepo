<h1 align="center">InternShip Project</h1>
<p align="center"><i>⭐Learning CI/CD pipeline,Enhance DevSecOps Skills⭐</i></p>
<h2>Vulnerable Flask Web Application</h2>

This project demonstrates a Flask web application intentionally built with security vulnerabilities. The purpose is to illustrate how to use GitHub Actions to create a secure CI/CD pipeline.

![Ekran görüntüsü 2024-08-01 062514-Photoroom](https://github.com/user-attachments/assets/6a681dd6-fc21-402b-8499-ed1ad37f4418)



## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Security Vulnerabilities](#security-vulnerabilities)
- [CI/CD Pipeline](#cicd-pipeline)


## Overview

This repository contains a simple Flask web application designed with security vulnerabilities. The objective is to leverage GitHub Actions for setting up a secure pipeline that detects and mitigates these vulnerabilities.

## Features

- User input form vulnerable to XSS attacks.
- Dockerized application.
- GitHub Actions for CI/CD.
- Security tools integration (e.g., Semgrep, Dependabot,Gitleaks,Trivy).

## Installation

### Prerequisites

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/selychan/testrepo.git
    cd testrepo
    ```

2. Build the Docker image:

    ```bash
    docker-compose build
    ```

3. Run the Docker container:

    ```bash
    docker-compose up
    ```

4. Open your browser and navigate to `http://localhost:5000`.

## Usage

Enter your name in the input field and submit the form. Note that the application contains a vulnerability that allows XSS attacks. You can test this by entering a script tag, such as `<script>alert(1)</script>`, and observing the behavior.

## Security Vulnerabilities

### Cross-Site Scripting (XSS)

The application does not properly sanitize user input, allowing for XSS attacks. This can be exploited by entering malicious scripts into the input field.

## CI/CD Pipeline

The project integrates several security tools into its CI/CD pipeline using GitHub Actions:

- **Semgrep**: Scans the code for security vulnerabilities and coding best practices.
- **Dependabot**: Automatically checks for dependency updates and security vulnerabilities.
- **Trivy**: Scans the code for container security.
- **Gitleaks**: Automatically checks for cleartext key.
