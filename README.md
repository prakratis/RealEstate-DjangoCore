# RealEstate-DjangoCore

A premium, luxury Real Estate web application built with **Django** and **Bootstrap 5**. This project features a high-contrast Black & Gold theme inspired by the "SOS Infrabulls" aesthetic (Security, Opportunity, Sincerity).

---

##  Project Overview
This application allows administrators to manage and display property listings dynamically. It focuses on clean UI/UX and a robust backend for handling property data and image uploads.

###  Key Features
* **Luxury Theme:** Deep black background with gold (`#d4af37`) accents.
* **Dynamic Listings:** Projects are pulled directly from the database and rendered using Django Templating Language (DTL).
* **Responsive Design:** Fully mobile-friendly layout using the Bootstrap 12-column grid system.
* **Image Handling:** Built-in support for uploading and displaying project site images.
* **Secure Forms:** Protected with CSRF tokens and backend validation.

---

##  Technical Architecture (MVT)

This project follows the **Model-View-Template** pattern:



### 1. Model (`models.py`)
Defines the database schema for property listings.
* **Fields:** Colony Name, Area Name, Rate, PinCode, and Image.
* **ORM:** Uses Django's Object-Relational Mapper to handle SQL operations without raw queries.

### 2. View (`views.py`)
The logic controller of the application.
* **`home`:** Fetches all project objects and passes them to the frontend.
* **`addProperties`:** Handles both `GET` (display form) and `POST` (process data) requests.

### 3. Template (`templates/`)
The dynamic HTML layer.
* **`index.html`:** Uses a `{% for %}` loop to display property cards.
* **`addProperties.html`:** A styled Bootstrap form for data entry.

---

##  Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/yourusername/RealEstate-DjangoCore.git](https://github.com/yourusername/RealEstate-DjangoCore.git)
