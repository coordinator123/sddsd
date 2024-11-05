from flask import Flask, render_template, request
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json
app = Flask(__name__)
firebase_credentials_json = '''{
  "type": "service_account",
  "project_id": "rderderedede",
  "private_key_id": "f32b3e9e92def8055654606ad4fb251f327a1a28",
  "private_key": "-----BEGIN PRIVATE KEY-----\\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDfJsIe542qJHss\\naPwv1R70phy0ALRmD7MIJtORVvDp6rztOBvdG09u9/DZGFfXSsarBphx7frfAOcj\\n5hU3ISfHyq+UrI61ViyqPRUQD0a+/Agqfxs9v6zPzOEwrygf9y1vKTIJDWXP3x34\\n9dLNvRZJ6DR9p59kkPjRQ8nuHp6r7Wm0CyZCJCfr5LQaZTliPjJz4q9fHTNaZJ8L\\nPhY5yZaI96ND5A2Oia5t0a02JU5SLu45vGBYLk9DBNctukRD2C9Lj281gF0xESEv\\ncb2Cw1Z1/NWDlFW5iBRxT28bT6xvKi/GB/rVqHw21S4t6lNIuzzuO+Yi9SEeRlRm\\ncKlmDfWNAgMBAAECggEAD9aU5ZOiuuY+9c53w79ZJJ0boW0BYNMRbm0vC/xDOh8G\\njMG0PJPBJgukBQyUw3uTsTTVIhT1ftl2Dla4v8JzK9uHbcJ3mIhGwEh4k7y51TlX\\nLQj7enz9u3v7qbRs4SPujhq66eiRBtl7q51q+l5G1DUOcLKyffVKK7Qng2aZ9XLQ\\n1wXV140m8z2m8lFVKeXjVLrRxWkPi+PvDy2U/I602CMaA0tDPhzCii02yoLg2tro\\nxbpthoYjGzLV+uF3rFFS1v2Fd3Wvf2YdqxzcZNXf6BiVtFpHIhFPS6ARBWUleCi9\\nl3cmChlzkGMGi/JQrb0OIhRSx+p1IGniVIkX97B+cwKBgQD9Se5IZpxM1YdeM4bW\\nKzY509KtIG4nVm1jvoTmwWecE5ljr3g/YWkAWE7Jc/e/5NxxKLmfDO3UqLliCrVK\\nqYP+jlvWjcjeAsWR/sJAW5NsxfqQEiryyQUW0NQDS+++LB6YhyIj8GL0dax097Oj\\ngQ3qS3vgOEx0BvTKmW+ZW2DwRwKBgQDhij6ARmkzXvqeP5JGFpWmF563k2vEjc31\\nGFlNu30PvQ43vi2j41MAiA4FwiQgAw+HvGHCwUuPvt6PGhQ3jsWAOKerbGg4QyXF\\n/lNw13rw7SeDnBDHf7Dl9wipuklmougNHxnuRbH4Qc0Cd1s5QcoA7WipQBbUEE0D\\nDK9cjb8JiwKBgQCbtrG47Ow2CCe6b+77B4HEt0aTjJZrtKR3Z48I1em+eAYa1KsW\\nO+pzfdah3pt261nib2j+MNKdpESj03V0uxYcjqRDGNNeOVIA2R/OtP3DJ0tM+v5Q\\nV+i7CBLvG+X9gd4lYx5H/ea35wfouMdFQ3esjE9RnwrRYd1oGEAVhanozQKBgQCh\\n1SFtx5ga3U71F+ZsVi5BBHfFf4l3eszKzhLePObK0TwPcW2sSCQ5oGZ3aUukkK2n\\nFtwK88m1Nh7aDbtt9grvKzfcQCg0HrJO9GOI94TmtTSCMgy0KYKUMALOTrX2aHQb\\nXjKsDuRZn1VsLJqPZg59RdywfSUkOyIXSxXVUnw+awKBgQDwouLpP+laMn0PBjaa\\nKlOEYIRl/N2f3vE7NjRnsaDuomXxLj0LAQENV+KrbXP9M4uUhP4WnQwdtaCu1V+c\\nyHuJtwR5UWk/HegPgv/issbEYSuwf/SSK8UhubhJErCEAafE3TZ621g7EMY72RjW\\nRpyVwKztjx+N/935DSSYIM4GXQ==\\n-----END PRIVATE KEY-----\\n",
  "client_email": "firebase-adminsdk-dcag5@rderderedede.iam.gserviceaccount.com",
  "client_id": "109754858243242536590",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-dcag5%40rderderedede.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}'''

# Initialize Firebase credentials and app
cred = credentials.Certificate(json.loads(firebase_credentials_json))
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://rderderedede-default-rtdb.firebaseio.com/'
})
db = firestore.client()


# Route for faculty event form
@app.route('/')
def faculty_event_form():
    return render_template('ftftf.html', success_message=None)

# Route for form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Fetch form data
        data = {
            'faculty_id': request.form.get('faculty_id'),
            'name': request.form.get('name'),
            'designation': request.form.get('designation'),
            'department': request.form.get('department'),
            'event_type': request.form.get('event_type'),
            'participation_type': request.form.get('participation_type'),
            'event_title': request.form.get('event_title'),
            'month_year': request.form.get('month_year'),
            'event_dates_from': request.form.get('event_dates_from'),  
            'event_dates_to': request.form.get('event_dates_to'),     
            'mode': request.form.get('mode'),
            'organization': request.form.get('organization'),
            'sponsoring_agency': request.form.get('sponsoring_agency'),
            'certificate_upload': request.form.get('certificate_upload'),
            'report_on_learning_outcomes_upload': request.form.get('report_on_learning_outcomes_upload'),  
            'proceedings_upload': request.form.get('proceedings_upload')
        }

        # Handle optional number of participants
        data['num_participants'] = request.form.get('num_participants') if data['participation_type'] == 'Organized' else None

        # Calculate total days between event dates
        date_format = "%Y-%m-%d"
        try:
            start_date = datetime.strptime(data['event_dates_from'], date_format)
            end_date = datetime.strptime(data['event_dates_to'], date_format)
            data['total_days'] = (end_date - start_date).days  # Calculate difference in days
        except ValueError:
            return render_template('faculty_event_form.html', success_message='Invalid date format. Please use YYYY-MM-DD.')

        try:
            # Save data to Firestore collection
            db.collection('faculty_event_submissions').add(data)
            success_message = 'Event submission successful!'  # Success message
        except Exception as e:
            print(f"Firestore error: {e}")
            success_message = 'There was an issue with the database.'

        # Redirect back to the form with a success message
        return render_template('ftftf.html', success_message=success_message)

if __name__ == '__main__':
    app.run(debug=True)
