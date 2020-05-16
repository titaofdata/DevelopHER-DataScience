mkdir -p ~/.streamlit/

echo "[generate]
email = \"shanelle.grace.recheta@eee.upd.edu.ph\"
" > ~/.streamlit/credentials.toml

echo "[server]
enableCORS = false
port = $PORT
headless = true
" > ~/.streamlit/config.toml
