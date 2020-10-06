CREATE TABLE ekadasi_dates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    day VARCHAR(10),
    month VARCHAR(10),
    year VARCHAR(4),
    start VARCHAR(5),
    end VARCHAR(5));

CREATE TABLE iskcon_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(100),
    month VARCHAR(10),
    day VARCHAR(10),
    year VARCHAR(4)
);
