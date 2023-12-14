from application import app as ap;

app = ap();

if __name__ == "__main__":
    ap.run();
else:
    print(f'\n***ERROR:: {__name__} ***\n');