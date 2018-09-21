from flask import Flask
import csv

app = Flask(__name__)

def find_in_csv(code):
    with open("zcta_crosswalk.csv") as f:
        r = csv.reader(f)
        for row in r:
            if row[0] == code:
                return row[1]
@app.route("/<zip>")
def index(zip):
    print(find_in_csv(zip))
    return ""

if __name__ == "__main__":
    app.run()