# Checkpasswords

A simple python program that checks passwords againts the free API as documentet here: https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange

Padding is added according to this blog: https://www.troyhunt.com/enhancing-pwned-passwords-privacy-with-padding/

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

Examples:

    ./checkpasswords.py -p qwerty
    WARN: password found: <qwerty> times: 10713794 range: B1B37 api.hash: 73A05C0ED0176787A4F1574FF0075F7521E
    
    ./checkpasswords.py -f passwords.txt 
    WARN: password found: <qwerty> times: 10713794 range: B1B37 api.hash: 73A05C0ED0176787A4F1574FF0075F7521E
    WARN: password found: <qwerty123456> times: 194488 range: F3BA3 api.hash: 81B6BAEF526BF70FF220B1DA4906989224B
    WARN: password found: <qwerty654321> times: 13253 range: E89EF api.hash: 3115D9DAB4E38C58F1E0122EDDE96C5502A

## CONFIGURATION

None.

## TODO

Nothing yet.
