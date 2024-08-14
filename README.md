# Youtube Api

Youtube Api for data processing

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.0+
- Virtualenv (optional but recommended)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Hudehtech/youtube-data-api.git
    cd youtube-data-api
    ```

2. **Create a virtual environment (optional but recommended):**

    ```bash
    virtualenv venv
    ```

3. **Activate the virtual environment:**

    - **Windows**

        ```bash
        venv\Scripts\activate
        ```

    - **Linux/macOS**

        ```bash
        source venv/bin/activate
        ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. **Run migrations to set up the database:**

    ```bash
    python manage.py migrate
    ```

### Running the Server

Start the development server:
obtain your API-KEY from https://developers.google.com/youtube/v3
YOUTUBE_API_KEY=''

```bash
python manage.py runserver
