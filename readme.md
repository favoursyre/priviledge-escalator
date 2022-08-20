# Priviledge Escalator

## Disclaimer

This script is for educational purposes only, I don't endorse or promote it's illegal usage

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Languages](#languages)
4. [Installations](#installations)
5. [Usage](#usage)
6. [Run](#run)

## Overview

This script allows an attacker to get admin priviledges on a windows system

## Features

- It requests for admin priviledges
- It clears event from the event viewer log

## Languages

- Python 3.9.7

## Installations

```shell
git clone https://github.com/favoursyre/priviledge-escalator.git && cd priviledge-escalator
```

## Usage

Instantiating the class

```python
priv = Escalate()
```

Requesting for admin priviledges

```python
priv.set_admin()
```

Clearing event on the windows event viewer log

```python
priv.clear_event()
```

## Run

```bash
python priviledge_escalator.py
```
