from flask import Flask, render_template
quiz = Flask(__name__)

@quiz.route('/')
def main():
	return render_template("bucket_list.html")

if __name__ == "__main__":
	quiz.run(debug = True)