from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import random
import faker

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/security_guards'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize Faker
fake = faker.Faker()

# Define models
class Guard(db.Model):
    __tablename__ = 'guards'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    badge_number = db.Column(db.String(10), unique=True, nullable=False)
    contact = db.Column(db.String(50))
    status = db.Column(db.String(20))

class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200))
    contact_person = db.Column(db.String(100))
    contact_number = db.Column(db.String(50))

class Shift(db.Model):
    __tablename__ = 'shifts'
    id = db.Column(db.Integer, primary_key=True)
    guard_id = db.Column(db.Integer, db.ForeignKey('guards.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20))

class Report(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True)
    guard_id = db.Column(db.Integer, db.ForeignKey('guards.id'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'), nullable=False)
    incident_date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20))

def generate_sample_data():
    # Create database tables
    with app.app_context():
        db.create_all()
        
        # Generate Guards
        print("Generating Guards...")
        for i in range(25):
            guard = Guard(
                name=fake.name(),
                badge_number=f"B{str(i+1).zfill(4)}",
                contact=fake.phone_number(),
                status=random.choice(['active', 'inactive', 'on_leave'])
            )
            db.session.add(guard)
        
        # Generate Locations
        print("Generating Locations...")
        for i in range(25):
            location = Location(
                name=fake.company(),
                address=fake.address(),
                contact_person=fake.name(),
                contact_number=fake.phone_number()
            )
            db.session.add(location)
        
        db.session.commit()

        # Generate Shifts
        print("Generating Shifts...")
        guards = Guard.query.all()
        locations = Location.query.all()
        
        for i in range(25):
            shift = Shift(
                guard_id=random.choice(guards).id,
                location_id=random.choice(locations).id,
                start_time=datetime.now() + timedelta(days=i),
                end_time=datetime.now() + timedelta(days=i, hours=8),
                status=random.choice(['scheduled', 'completed', 'cancelled'])
            )
            db.session.add(shift)

        # Generate Reports
        print("Generating Reports...")
        for i in range(25):
            report = Report(
                guard_id=random.choice(guards).id,
                location_id=random.choice(locations).id,
                incident_date=datetime.now() - timedelta(days=random.randint(1, 30)),
                description=fake.text(),
                status=random.choice(['open', 'closed', 'investigating'])
            )
            db.session.add(report)

        db.session.commit()
        print("Sample data generation completed!")

if __name__ == '__main__':
    generate_sample_data() 