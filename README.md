# DJANGO GENETICA TEST [![CircleCI Status](https://circleci.com/gh/vanhiepdam/genetica.svg?style=svg)](https://github.com/vanhiepdam/genetica) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/30c17db9e96449a18428a9a47b7aa793)](https://www.codacy.com/manual/vanhiepdam/genetica?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=vanhiepdam/genetica&amp;utm_campaign=Badge_Grade) [![codecov](https://codecov.io/gh/vanhiepdam/genetica/branch/master/graph/badge.svg)](https://codecov.io/gh/vanhiepdam/genetica) [![Known Vulnerabilities](https://snyk.io/test/github/vanhiepdam/genetica/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/vanhiepdam/genetica?targetFile=requirements.txt)

## Introduction

This project is used only for test at Genetica

## Quickstart

##### PREREQUISITE

- Postgresql was already installed
- For testing correctly, please make sure the postgres process is running at localhost:5432. username=postgres, password=:BLANK
- python 3.6

1. Clone this repository `git clone https://github.com/vanhiepdam/genetica.git`
2. Run script `./quickstart.sh`

## Usage

### Accounts

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
