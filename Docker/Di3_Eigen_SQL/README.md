# Di3 – Eigen image-experiment 2 (SQL)

## Doel
Een eigen Docker image maken dat een SQL database gebruikt.
In dit experiment wordt SQLite gebruikt (SQL database) binnen een container.

## Wat doet de container?
- Maakt een SQLite database `di3.db`
- Maakt een tabel `notes`
- Voegt sample records toe (INSERT)
- Leest records uit (SELECT) en print de resultaten

## Build
```bash
docker build -t di3-sql:1.0 .
Run (test)
docker run --rm --name di3-run di3-sql:1.0
Verwacht output:

"Di3 SQL RESULT (SELECT)" + records (bewijs dat SQL werkt)
