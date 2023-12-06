# OffersAscenda

This project uses Python 3.11.3.

The output is save in output.json 

## Clone this project 

```bash
$: git clone https://github.com/nguyengoc16/OffersAscenda.git

$: cd OffersAscenda
```

## Create and activate virtual environment

### If you are using Wins

```bash
$: py -m venv venv

$: venv/scripts/activate
```
### If you are using Macs

```bash
$: python3 -m venv virtualenv

$: source venv/bin/activate
```
## Install dependencies

```bash
(venv)$: pip install -r requirements.txt
```

## Launch the app

```bash
(venv)$: cd myapp

(venv)$: waitress-serve --listen=127.0.0.1:5000 server:app
```

You should see something like this:

```bash
[INFO]:waitress:Serving on http://127.0.0.1:5000
```

Then you will need to input date in order to find offers.