from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Retrieve data from the request
    data = request.json
    
    # Generate PDF using the data (this is where you would write your PDF generation logic)
    # For demonstration purposes, we'll just return a dummy response
    pdf_url = 'http://example.com/path/to/generated_pdf.pdf'
    
    # Return the URL of the generated PDF
    return jsonify({'pdf_url': pdf_url})

@app.route('/download_pdf', methods=['GET'])
def download_pdf():
    # Assuming you have the PDF file stored locally
    pdf_path = 'C:/Users/ASUS/Downloads/mongodb_for_lab.pdf'
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
