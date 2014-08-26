from app import app

@app.route('/')
@app.route('/index')
def index():
	return "<h3>Hello World!</h3><p>lipsumss</p>"
