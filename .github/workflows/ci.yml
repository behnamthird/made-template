name: CI Pipeline for Project

on:
  push:
    branches:
      - main

jobs:
  run-test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install Dependencies
        run: |
          pip install pytest
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

      - name: Run Test
        run: |
          chmod +x test.sh
          ./test.sh
