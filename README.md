# 🧑‍⚕️🏥 Patient Vitals Monitoring Web Application with Arduino

This web application, built with Django, allows for the real-time monitoring of patient vital signs collected by Arduino sensors. It provides a simple and intuitive interface to track patient data.

## ✨ Cool Overview

The application centers around managing patients and their associated Arduino devices. It logs crucial vital signs, enabling healthcare professionals or caregivers to monitor health metrics effectively.

* **🧑‍⚕️ Patient Management:** Easily register and manage patient information, including their first and last names and registration date.
* **Arduino Integration:** Link Arduino devices to specific patients for seamless data association. Each Arduino is identified by a unique ID.
* **❤️ Vital Signs Logging:** Records key vital signs such as:
    * 🩸 **SpO2 (Oxygen Saturation):** Percentage of oxygen in the patient's blood.
    * 💓 **Heart Rate:** Beats per minute.
    * ⏱️ **Log Timestamp:** Date and time when the vital signs were recorded.
* **📊 Data Association:** All logged vital signs are directly associated with a specific patient and the Arduino device that collected the data.

## 🚀 Getting Started

Follow these steps to get your local instance of the patient vitals monitoring web application up and running.

### Prerequisites

Ensure you have the following installed on your system:

* **Python:** (version 3.x recommended)
* **pip:** (Python package installer)
* **Django:** (latest stable version recommended)

### Installation

1.  **Clone the repository (if you have the code on GitHub):**
    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the project dependencies:**
    ```bash
    pip install django
    # Install any other Django packages you might be using
    ```

4.  **Make migrations:**
    ```bash
    python manage.py makemigrations
    ```

5.  **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

6.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

    Open your web browser and navigate to `http://127.0.0.1:8000/` to access the application. You can access the Django admin interface at `http://127.0.0.1:8000/admin/`.

### Arduino Setup (Conceptual)

This README focuses on the Django web application. The Arduino setup would involve:

1.  **Connecting sensors** (SpO2, heart rate) to your Arduino board.
2.  **Programming the Arduino** to read sensor data.
3.  **Establishing communication** between the Arduino and your Django application (e.g., via serial communication, network requests). You would need to implement the backend logic in Django to receive and process the data sent by the Arduino.

## 🛠️ Models Overview

Here's a brief explanation of the Django models used in this application:

* **`Patient`:** Represents a patient in the system.
    * `first_name`: Patient's first name (CharField, max length 12).
    * `last_name`: Patient's last name (CharField, max length 12).
    * `register_date`: Date and time when the patient was registered (DateTimeField).
    * `was_published_recently()`: Method to check if the patient was registered within the last day.
    * `__str__`: Returns the full name of the patient.

* **`Arduino`:** Represents an Arduino device associated with a patient.
    * `patient`: Foreign key linking the Arduino to a `Patient` (on_delete=models.CASCADE). If a patient is deleted, their associated Arduinos are also deleted.
    * `arduino_id`: Unique identifier for the Arduino device (CharField, max length 12).
    * `__str__`: Returns the Arduino ID.

* **`ArduinoLog`:** Represents a log entry of vital signs recorded by an Arduino for a patient.
    * `patient`: Foreign key linking the log to a `Patient` (on_delete=models.CASCADE).
    * `arduino`: Foreign key linking the log to an `Arduino` (on_delete=models.CASCADE).
    * `spo2`: Oxygen saturation level (FloatField).
    * `heart_rate`: Heart rate in beats per minute (FloatField).
    * `log_date`: Date and time when the vital signs were logged (DateTimeField).
    * `__str__`: Returns a string representation of the log entry, including the patient's name and Arduino ID.

## 🤝 Contributing

Contributions to this project are welcome! If you have ideas for improvements or find any issues, please feel free to:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them.
4.  Push your changes to your fork.
5.  Submit a pull request.

## 📜 License

GPLv3
