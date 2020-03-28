# DJANGO GENETICA TEST [![CircleCI Status](https://circleci.com/gh/vanhiepdam/genetica.svg?style=svg)](https://github.com/vanhiepdam/genetica) [![Known Vulnerabilities](https://snyk.io/test/github/vanhiepdam/genetica/badge.svg?targetFile=requirements.txt)](https://github.com/vanhiepdam/genetica)

## Introduction

This project is used only for test at Genetica

## Quickstart

PREREQUISITE: 
- Postgresql was already installed
- For testing correctly, please make sure the postgres process is running at localhost:5432. username=postgres, password=:BLANK
- python 3.6

Run script `./quickstart.sh`

## Usage
### Accounts:
- admin: admin/admin
- user: user/admin

### Get token

Method `POST`

URL `api/1/login`

data `{"username": "user", "password": "admin"}`


### List reports

Method `GET`

URL `api/1/reports?state=[prepare|ready]`

headers `Authorization: Bearer :access_token`

- Another special api: 

Method `GET`

URL `api/1/reports/ready`

headers `Authorization: Bearer :access_token`
