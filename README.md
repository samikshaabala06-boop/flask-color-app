# Flask Color App

## Description

This is a simple Flask web application that displays a webpage with a background color based on the environment variable `APP_COLOR`.

If `APP_COLOR` is not set, the application uses **white** as the default color.

---

## Features

* Built using Python Flask
* Reads color from environment variable `APP_COLOR`
* Supports colors such as:

  * red
  * green
  * blue
  * yellow
  * white
* Uses a default color when the variable is not provided

---

## Requirements

* Python 3.13
* Flask

---

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Navigate to the project folder:

```bash
cd flask-color-app
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

Windows:

```bash
.\venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Set the environment variable:

```powershell
$env:APP_COLOR="red"
```

Run the application:

```bash
python app.py
```

Open the browser and visit:

```text
http://127.0.0.1:5000
```

---

## Environment Variables

| Variable  | Description                     | Default |
| --------- | ------------------------------- | ------- |
| APP_COLOR | Background color of the webpage | white   |

---

## Authors

Samikshaa and Nasrin
