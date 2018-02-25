RAND_STR=`head /dev/urandom | LC_CTYPE=C tr -dc A-Za-z0-9 | head -c 13`
echo SECRET_KEY=\'"$RAND_STR"\' > todolist/secret_settings.py 
