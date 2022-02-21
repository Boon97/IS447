<<<<<<< HEAD
from flask import Blueprint, render_template
from website import create_app

app = create_app()

if __name__ == '__main__':
=======
from flask import Blueprint, render_template
from website import create_app

app = create_app()

if __name__ == '__main__':
>>>>>>> c1daa13c026cdd946bd8e6e9a09f8e91c83910e4
	app.run(debug=True)