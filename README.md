# Argument Mining Framework (AMF)

## Introduction
The Argument Mining Framework (AMF) is a collection of components designed to identify argument relations between propositions. This README provides an overview of the components and their functionalities.

## Components

### DAM-01
- **Endpoint:** `/dam-01`
- **Description:** DAM-01 is an implementation of decompositional argument mining (DAM) that decomposes propositions into four functional components. The compoenents are identified using dependecy based rules. It utilizes semantic similarity and sentiment categories between these components to detect argument relations.
- **Methods:** 
  - `POST`: Accepts a file containing propositions and returns the argument structure.
  - `GET`: Provides information about the component and its functionality.

### DAM-02
- **Endpoint:** `/dam-02`
- **Description:** DAM-02 is an AMF component that identifies argument relations between propositions. It combines DAM-01 and textual entailement to improve performance. The compoenents are identified using dependecy based rules.  It takes xIAF as input and returns xIAF as output.
- **Methods:** 
  - `POST`: Accepts a file containing propositions and returns the argument structure.
  - `GET`: Provides information about the component and its functionality.

### DAM-03
- **Endpoint:** `/dam-03`
- **Description:** DAM-03 is an AMF component that identifies argument relations between propositions. It combines DAM-01 and DAM-02 and  to improve performance. The compoenents are identified using BERT fine-tuned on token classification task.  It takes xIAF as input and returns xIAF as output.
- **Methods:** 
  - `POST`: Accepts a file containing propositions and returns the argument structure.
  - `GET`: Provides information about the component and its functionality.

## How to Use
1. Ensure that the required dependencies are installed.
2. Run the Flask application.
3. Access the desired endpoint using HTTP methods (`POST` for processing files, `GET` for information).


## Running the Application
```bash
python app.py
