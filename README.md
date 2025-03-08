# Project

[Look Project](https://computer-vision-pro.streamlit.app/)

# Commands

- To run the project:

```bash
streamlit run ./app.py
```

> You need create 2 directories called `model` and `params`.


```bash
chmod +x .devcontainer/setup.sh
```

---

# Use Docker

```bash
docker build -t computer-vision .
```

```bash
docker run -v .:/app -p 8080:8080 computer-vision 
```
