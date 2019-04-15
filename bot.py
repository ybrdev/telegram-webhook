from bottle import run, post


@post('/')  # our python function based endpoint
def main():
    return


if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
