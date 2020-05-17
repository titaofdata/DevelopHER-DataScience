mkdir -p ~/streamlit/

echo "\
[generate]\n\
email = \"shanelle.grace.recheta@eee.upd.edu.ph\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml