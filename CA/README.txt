Wild Atlantic Way – Multilingual Travel Website
This is a Flask-based web application showcasing the Wild Atlantic Way route in Ireland.
It provides a culturally tailored experience through internationalisation and localisation features,
catering to different user personas such as Freja (eco-conscious, minimalist)
and Philip (structure-seeking, safety-focused).


SETUP INSTRUCTIONS
1. Clone the repository or unzip the project files into your working directory.

2. Navigate into the app folder:
   cd app

3. (Optional) Create a virtual environment:
   python -m venv venv
   On Windows: venv\Scripts\activate
   On Mac/Linux: source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Navigate back to the CA folder
   cd ..

6. Run the Flask app:
   flask run

7. Visit in your browser:
   http://127.0.0.1:5000


INTERNATIONALISATION STRATEGY
- Languages supported: English (default), Greek (el), Danish (da).
- Language is selected using a dropdown menu in the navigation bar.
- Language preference is stored in the session and persists across page loads.
- Translatable text is wrapped in _( ) using Jinja2 and Babel.
- .pot file serves as the master template for translation strings.
- .po files store language-specific translations (e.g., messages.po).
- .mo files are compiled from .po files for runtime use.


CHANGING LANGUAGE
To change the language, click the dropdown in the navbar and select English, Greek, or Danish.
This will trigger the route /setlang/<lang_code> to set the session language and reload the page with the correct translations.


TESTING INSTRUCTIONS
1. Navigate through all pages in each language using the dropdown.
2. Confirm that:
   - Navigation text and content are translated.
   - Language-specific icons and styles are applied.
   - The URL remains the same while the content changes.
3. Use browser developer tools to check for missing images or untranslated text.


FILE STRUCTURE OVERVIEW
app/
├── static/
│   ├── css/
│   └── assets/img/<lang_code>/
├── templates/
│   └── includes/<lang_code>/
├── translations/
│   ├── el/
│   └── da/
├── routes.py
├── __init__.py


NOTES
- Remember to compile your translation files before running:
  pybabel compile -d translations

- Each design and layout reflects cultural values for better engagement.
