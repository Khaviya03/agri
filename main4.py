from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template with placeholders
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome App</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
        input, button { padding: 10px; font-size: 16px; }
        .message { margin-top: 20px; font-size: 20px; color: green; }
        .error { margin-top: 20px; font-size: 18px; color: red; }
    </style>
</head>
<body>
    <h1>Welcome Message App</h1>
    <form method="POST">
        <label for="name">Enter your name:</label><br><br>
        <input type="text" id="name" name="name" placeholder="Your name" required>
        <button type="submit">Submit</button>
    </form>
    {% if message %}
        <div class="message">{{ message }}</div>
    {% elif error %}
        <div class="error">{{ error }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def welcome():
    message = None
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()

        # Input validation
        if not name:
            error = "Name cannot be empty."
        elif not name.replace(" ", "").isalpha():
            error = "Name must contain only letters and spaces."
        else:
            message = f"Welcome, {name}!"

    return render_template_string(HTML_TEMPLATE, message=message, error=error)

if __name__ == "__main__":
    # Run the app in debug mode for development
    app.run(debug=True)


