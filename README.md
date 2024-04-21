# Checkpasswords

A simple pythonprogram that checks passwords againts https://api.pwnedpasswords.com/range
as documentet here: https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange

## AUTHOR 

Phazor / Cascade 1733 

## INSPIRATION

Got inspiration and examples from other coders on Github.

## LICENSE

Please feel free to copy, distribute and change this program in any way you like.

## INSTALLATION

1. virtualenv venv

2. source venv/bin/activate

3. pip install -r requirements.txt

Example:

    ./checkpasswords.py -p qwerty
    WARN: password found: <qwerty> times: 10713794 range: B1B37 api.hash: 73A05C0ED0176787A4F1574FF0075F7521E

## CONFIGURATION

None.

## TODO

Nothing yet.
