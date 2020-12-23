


from flask import Flask, render_template, request
from quad import quadratic_equation1, quadratic_equation2

app = Flask(__name__)


@app.route('/quad', methods=['POST'])
def do_search() -> 'html':
    a = float(request.form[ 'phrase1' ])
    b = float(request.form[ 'phrase2' ])
    c = float(request.form[ 'phrase3' ])

    title = 'Here are your results for the two roots of the quadratic equation:'
    results1 = quadratic_equation1(a,b,c)
    results2 = quadratic_equation2(a,b,c)
    return render_template('results.html',
                           the_title=title,
                           the_phrase1=a,
                           the_phrase2=b,
                           the_phrase3=c,
                           
                           the_results1=results1,
                           the_results2=results2,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to Quadratic Equation Solution on the web!')


if __name__ == '__main__':
    app.run(debug=True)
