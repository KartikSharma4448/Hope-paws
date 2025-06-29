from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'kartikuma9261@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'nass litu tusc pekp')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME', 'kartikuma9261@gmail.com')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about-us')
def about_us():
    return render_template('AboutUs.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            data = request.get_json()
            name = data['name']
            email = data['email']
            number = data['number']
            message = data['message']

            # Send admin notification email
            admin_msg = Message(
                subject=f"New Contact Form Submission from {name}",
                sender=('HopePaws', 'kartikuma9261@gmail.com'),
                recipients=['gta.thelegend@gmail.com', 'kartikuma9261@gmail.com'],
                body=f"""
                New Contact Form Submission:
                
                Name: {name}
                Email: {email}
                Phone: {number}
                Message: {message}
                
                Please respond to this inquiry as soon as possible.
                """
            )

            # Send sender confirmation email
            sender_msg = Message(
                subject="Thank you for contacting HopePaws",
                sender=('HopePaws', 'kartikuma9261@gmail.com'),
                recipients=[email],
                body=f"""
                Dear {name},
                
                Thank you for reaching out to HopePaws! We have received your message and will get back to you as soon as possible.
                
                Here's a copy of your message:
                {message}
                
                If you have any urgent concerns, please feel free to call us at +91-XXXXXXXXXX.
                
                Best regards,
                The HopePaws Team
                """
            )

            # Send both emails
            mail.send(admin_msg)
            mail.send(sender_msg)

            print(f"Attempting to send email to: {email}")  # Debug line
            return jsonify({"success": True, "message": "Email sent successfully"})
        
        except Exception as e:
            print(f"Error sending email: {str(e)}")  # Debug line
            return jsonify({"success": False, "error": str(e)}), 500

    return render_template('contact.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        try:
            data = request.get_json()
            name = data['name']
            transaction_number = data['transaction_number']
            mobile_number = data['Mobile_Number']
            amount = data['Amount']

            # Send admin notification email
            admin_msg = Message(
                subject=f"New Donation Received from {name}",
                sender=('HopePaws', 'kartikuma9261@gmail.com'),
                recipients=['gta.thelegend@gmail.com', 'kartikuma9261@gmail.com'],
                body=f"""
                New Donation Details:
                
                Donor Name: {name}
                Transaction Number: {transaction_number}
                Mobile Number: {mobile_number}
                Amount: ₹{amount}
                
                Please verify the transaction and update the records.
                """
            )

            # Send donor confirmation email
            donor_msg = Message(
                subject="Thank you for your donation to HopePaws",
                sender=('HopePaws', 'kartikuma9261@gmail.com'),
                recipients=[f"{mobile_number}@jio.com"],  # Using Jio email since UPI ID is Jio
                body=f"""
                Dear {name},
                
                Thank you for your generous donation of ₹{amount} to HopePaws!
                
                Your donation will help us continue our mission of rescuing and caring for stray animals.
                
                Transaction Details:
                - Transaction Number: {transaction_number}
                - Amount: ₹{amount}
                
                We will send you a tax receipt for your donation shortly.
                
                If you have any questions, please feel free to contact us.
                
                Best regards,
                The HopePaws Team
                """
            )

            # Send both emails
            mail.send(admin_msg)
            mail.send(donor_msg)

            return jsonify({"success": True, "message": "Donation processed successfully"})
        
        except Exception as e:
            print(f"Error processing donation: {str(e)}")
            return jsonify({"success": False, "error": str(e)}), 500

    return render_template('donate.html')

@app.route('/report-emergency', methods=['GET', 'POST'])
def report_emergency():
    if request.method == 'POST':
        try:
            data = request.get_json()
            name = data['Name']
            email = data['Email']
            phone = data['Phone']
            location = data['Location']
            description = data['Description']

            # Send admin notification email
            admin_msg = Message(
                subject=f"Emergency Report from {name}",
                sender=('HopePaws', 'kartikuma9261@gmail.com'),
                recipients=['gta.thelegend@gmail.com', 'kartikuma9261@gmail.com'],
                body=f"""
                Emergency Report Details:
                
                Reporter Name: {name}
                Email: {email}
                Phone: {phone}
                Location: {location}
                
                Emergency Description:
                {description}
                
                Please respond to this emergency as soon as possible.
                """
            )

            # Send reporter confirmation email
            reporter_msg = Message(
                subject="Emergency Report Received - HopePaws",
                sender=('HopePaws', 'kartikuma9261@gmail.com'),
                recipients=[email],
                body=f"""
                Dear {name},
                
                Thank you for reporting this emergency to HopePaws. We have received your report and our team will respond as soon as possible.
                
                Emergency Details:
                - Location: {location}
                - Description: {description}
                
                Our team will contact you shortly at {phone} for any additional information needed.
                
                If this is a life-threatening emergency, please call our emergency hotline at +91-XXXXXXXXXX immediately.
                
                Best regards,
                The HopePaws Team
                """
            )

            # Send both emails
            mail.send(admin_msg)
            mail.send(reporter_msg)

            return jsonify({"success": True, "message": "Emergency report submitted successfully"})
        
        except Exception as e:
            print(f"Error processing emergency report: {str(e)}")
            return jsonify({"success": False, "error": str(e)}), 500

    return render_template('Report Emergency.html')

@app.route('/veterinary-directory')
def veterinary_directory():
    return render_template('Veterinary Directory.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    try:
        data = request.get_json()
        
        # Create admin notification email
        admin_msg = Message(
            subject=f"New Contact Form Submission from {data['name']}",
            recipients=['gta.thelegend@gmail.com'],  # Send to admin email
            body=f"""
            New Contact Form Submission:
            
            Name: {data['name']}
            Email: {data['email']}
            Phone: {data['number']}
            Message: {data['message']}
            
            Please respond to this inquiry as soon as possible.
            """
        )
        
        # Create sender confirmation email
        sender_msg = Message(
            subject="Thank you for contacting HopePaws",
            recipients=[data['email']],  # Send to the person who filled the form
            body=f"""
            Dear {data['name']},
            
            Thank you for reaching out to HopePaws! We have received your message and will get back to you as soon as possible.
            
            Here's a copy of your message:
            {data['message']}
            
            If you have any urgent concerns, please feel free to call us at +91-XXXXXXXXXX.
            
            Best regards,
            The HopePaws Team
            """
        )
        
        # Send both emails
        mail.send(admin_msg)
        mail.send(sender_msg)
        
        return jsonify({"success": True, "message": "Email sent successfully"})
    
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)