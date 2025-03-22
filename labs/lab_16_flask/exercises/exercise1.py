"""Basic Flask operations module."""

import os
from typing import Any, Dict, List, Optional
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    send_from_directory,
    jsonify
)
from rich.console import Console
from rich.table import Table


# Load environment variables
load_dotenv()


# Initialize Rich console
console = Console()


class FlaskApp:
    """Basic Flask application."""

    def __init__(self):
        """Initialize the Flask application."""
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'dev')
        self.app.config['UPLOAD_FOLDER'] = os.path.join(
            os.path.dirname(__file__),
            'static',
            'uploads'
        )
        self._setup_routes()
        self._ensure_upload_folder()

    def _ensure_upload_folder(self) -> None:
        """Ensure the upload folder exists."""
        Path(self.app.config['UPLOAD_FOLDER']).mkdir(
            parents=True,
            exist_ok=True
        )

    def _setup_routes(self) -> None:
        """Set up application routes."""
        # Basic routes
        self.app.route('/')(self.index)
        self.app.route('/about')(self.about)
        self.app.route('/contact')(self.contact)

        # Dynamic routes
        self.app.route('/user/<username>')(self.user_profile)
        self.app.route('/post/<int:post_id>')(self.show_post)

        # Form handling
        self.app.route('/contact', methods=['POST'])(self.handle_contact)

        # File upload
        self.app.route('/upload', methods=['GET', 'POST'])(self.handle_upload)
        self.app.route('/uploads/<filename>')(self.uploaded_file)

        # API endpoints
        self.app.route('/api/hello')(self.api_hello)
        self.app.route('/api/data')(self.api_data)

        # Error handlers
        self.app.errorhandler(404)(self.page_not_found)
        self.app.errorhandler(500)(self.internal_server_error)

    def index(self) -> str:
        """Render the index page.

        Returns:
            str: Rendered template
        """
        return render_template(
            'index.html',
            title='Home',
            current_time=datetime.utcnow()
        )

    def about(self) -> str:
        """Render the about page.

        Returns:
            str: Rendered template
        """
        return render_template(
            'about.html',
            title='About'
        )

    def contact(self) -> str:
        """Render the contact page.

        Returns:
            str: Rendered template
        """
        return render_template(
            'contact.html',
            title='Contact'
        )

    def user_profile(self, username: str) -> str:
        """Render a user's profile page.

        Args:
            username: Username to display

        Returns:
            str: Rendered template
        """
        return render_template(
            'profile.html',
            title=f'Profile - {username}',
            username=username
        )

    def show_post(self, post_id: int) -> str:
        """Render a blog post page.

        Args:
            post_id: ID of the post to display

        Returns:
            str: Rendered template
        """
        # Simulated post data
        post = {
            'id': post_id,
            'title': f'Post {post_id}',
            'content': f'This is the content of post {post_id}.',
            'author': 'John Doe',
            'date': datetime.utcnow()
        }
        return render_template(
            'post.html',
            title=f'Post {post_id}',
            post=post
        )

    def handle_contact(self) -> str:
        """Handle contact form submission.

        Returns:
            str: Redirect URL
        """
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        if not all([name, email, message]):
            flash('Please fill in all fields.', 'error')
            return redirect(url_for('contact'))

        # Here you would typically send an email or save to database
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('index'))

    def handle_upload(self) -> str:
        """Handle file upload.

        Returns:
            str: Rendered template or redirect URL
        """
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part', 'error')
                return redirect(request.url)

            file = request.files['file']
            if file.filename == '':
                flash('No selected file', 'error')
                return redirect(request.url)

            if file:
                filename = file.filename
                file.save(os.path.join(self.app.config['UPLOAD_FOLDER'], filename))
                flash('File uploaded successfully', 'success')
                return redirect(url_for('uploaded_file', filename=filename))

        return render_template('upload.html', title='Upload File')

    def uploaded_file(self, filename: str) -> Any:
        """Serve uploaded files.

        Args:
            filename: Name of the file to serve

        Returns:
            Any: File response
        """
        return send_from_directory(
            self.app.config['UPLOAD_FOLDER'],
            filename
        )

    def api_hello(self) -> Dict[str, str]:
        """Simple API endpoint.

        Returns:
            Dict[str, str]: JSON response
        """
        return jsonify({
            'message': 'Hello, World!',
            'status': 'success'
        })

    def api_data(self) -> Dict[str, Any]:
        """Data API endpoint.

        Returns:
            Dict[str, Any]: JSON response
        """
        return jsonify({
            'items': [
                {'id': 1, 'name': 'Item 1'},
                {'id': 2, 'name': 'Item 2'},
                {'id': 3, 'name': 'Item 3'}
            ],
            'total': 3,
            'timestamp': datetime.utcnow().isoformat()
        })

    def page_not_found(self, error: Exception) -> tuple[str, int]:
        """Handle 404 errors.

        Args:
            error: Error object

        Returns:
            tuple[str, int]: Rendered template and status code
        """
        return render_template('404.html', title='Page Not Found'), 404

    def internal_server_error(self, error: Exception) -> tuple[str, int]:
        """Handle 500 errors.

        Args:
            error: Error object

        Returns:
            tuple[str, int]: Rendered template and status code
        """
        return render_template('500.html', title='Internal Server Error'), 500

    def run(self, debug: bool = True) -> None:
        """Run the Flask application.

        Args:
            debug: Whether to run in debug mode
        """
        self.app.run(debug=debug)


# Example usage
if __name__ == "__main__":
    try:
        # Create templates directory if it doesn't exist
        templates_dir = Path(__file__).parent / 'templates'
        templates_dir.mkdir(exist_ok=True)

        # Create basic templates
        index_template = templates_dir / 'index.html'
        if not index_template.exists():
            index_template.write_text('''
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome to Flask</h1>
    <p>Current time: {{ current_time }}</p>
    <nav>
        <a href="{{ url_for('index') }}">Home</a>
        <a href="{{ url_for('about') }}">About</a>
        <a href="{{ url_for('contact') }}">Contact</a>
    </nav>
</body>
</html>
            ''')

        # Initialize and run the application
        app = FlaskApp()
        console.print("[green]Starting Flask application...[/]")
        app.run()

    except Exception as e:
        console.print(f"[red]Error: {e}[/]") 